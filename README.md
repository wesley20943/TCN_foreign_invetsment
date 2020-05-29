# TCN_foreign_invetsment
This TCN model are based on the repo from https://github.com/philipperemy/keras-tcn /n
Our propose is to predict the percentage of the shareholding ratio of the foreign investors


# Model
Using TCN structure reference from https://arxiv.org/pdf/1803.01271.pdf
included casual convolutions and dilated convolutions and FC-NN(sigmoid as activation)
The hyper parameters are num_feat=28, nb_filters=24, kernel_size=8, dilations=[0,2,4,8....,64]..... (detailed in model.ipynb)

## Data preprcessing
each input with shape (1,28,15)  ==  (num of dataset, num of variables, num of days looking before) 
eacg putput with shape (1,1)     ==  (num of dataset, next day shareholdings ratio of foreign invetors )

preprocess the data:
list_rescale = [1, 2, 3, 4, 5, 6, 32, 57, 58, 63, 67] by rescalinging each input's first date data as 1, others as 1+ incresed rate
list_n_rescale = [13, 15, 17, 19, 21, 23, 26, 29, 31, 34, 35, 37, 39, 41, 43, 59, 62] do not rescale cause its already presented as inceased rate
for total_issued variables, rescale by using median normaliztion ( x - median / MAD )
    -> all_issued_median = 458112177.99999994
    -> MAD = 457654065.8219999  

# Data included
variables inculding:
macro --> VIX, increase rate of domestic/government expenditure, capital construction, GDP, CPI........ 
micro --> Open, High, Max, Min, Close price, ratio of volume traded, put/call ratio of taiwan 50 index.......
(detailed can be viewed in variables.txt)

77526 in total ,54268(60%) in training ,others in testing 

data from:
https://www.stat.gov.tw/
https://index.ndc.gov.tw/n/zh_tw
https://www.twse.com.tw/zh/
https://www.cnyes.com/
https://www.cbc.gov.tw/tw/mp-1.html
https://finance.yahoo.com/quote/%5EVIX/history/

# Result
Reach loss = 0.0173 in training dataset and loss = 0.0177 (MSE) in testing dataset. (MSE) 
batch_size -> 50->100->200->200
epochs     -> 20->10->5->10
More detailed information can be seen in model.ipynb
