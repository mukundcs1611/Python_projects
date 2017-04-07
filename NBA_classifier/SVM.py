import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score

#read from the csv file and return a Pandas DataFrame.
nba = pd.read_csv('NBAstats.csv')


def detectOutlier(data):
# Checking for outliers
    isValid=[]
     
    nba_games_set=data[['G','MP','3P%','FT%','Pos']]
      
     
    for i in nba_games_set.values:
        if(i[0]<3 or i[1]<5 or ( i[2]==0 and(i[3]=='SG' or i[3]=='PG')) ):
            isValid.append(False)
         
        else:
            isValid.append(True) 
         
     
    return isValid 

def crossValidation():
    # DO a 10 fold Cross validation 
    #Approach:
#    1.For Each iteration of 10 fold , separate train and test 
#    2.From Train remove outliers
#    3.Apply classifier on the train and test data
# 
# 
 
    all_col=['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', \
    '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', \
    'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PS/G','Pos']
  
    nba_feature=nba[all_col]
    print("\nSelf Implemented Cross Validation:")
    totalAccuracy=0.0
    for i in range(1,10):
        
        
        train_feature, test_feature, train_class, test_class = \
            train_test_split(nba_feature,nba_class, stratify=nba_class, \
            train_size=1-(0.1*i), test_size=i*0.1)
        #Remove Outliers         
        isValid=detectOutlier(train_feature)
        train_feature=train_feature[isValid]
        train_class=train_class[isValid]
#       #Only Select Interesting Features     
        train_feature=train_feature[feature_columns]
        test_feature=test_feature[feature_columns]
        
        linearsvm = LinearSVC().fit(train_feature, train_class)
        print("Fold No : ",i,"Test set score: {:.3f}".format(linearsvm.score(test_feature, test_class)))
        totalAccuracy=linearsvm.score(test_feature, test_class)+totalAccuracy
     
     
    print("Average Accuracy Using 10 fold cross validation:",totalAccuracy/10)        
    

# "Position (pos)" is the class attribute we are predicting. 
class_column = 'Pos'

#The dataset contains attributes such as player name and team name. 
#We know that they are not useful for classification and thus do not 
#include them as features. 
feature_columns=['DRB','TRB','AST','BLK','STL','FG','3P','2PA','ORB','3PA','FT%','PS/G']

    

#Pandas DataFrame allows you to select columns. 
#We use column selection to split the data into features and class. 
nba_feature = nba[feature_columns]
nba_class = nba[class_column]



train_feature, test_feature, train_class, test_class = \
    train_test_split(nba_feature,nba_class, stratify=nba_class, \
    train_size=0.75, test_size=0.25)

training_accuracy = []
test_accuracy = []

linearsvm = LinearSVC().fit(train_feature, train_class)
print("Test set score using 25/75 Split and LinearSVC: {:.3f}".format(linearsvm.score(test_feature, test_class)))


prediction=linearsvm.predict(test_feature)
print("Confusion matrix:")
print(pd.crosstab(test_class, prediction, rownames=['True'], colnames=['Predicted'], margins=True))

#The Following method has to be tuned more,it gives low accuracy rates
crossValidation()


#Scikit Provided Cross_validation
scores = cross_val_score(LinearSVC(), nba_feature, nba_class, cv=10)
print("Cross-validation scores: {}".format(scores))
print("Average cross-validation score: {:.2f}".format(scores.mean()))


