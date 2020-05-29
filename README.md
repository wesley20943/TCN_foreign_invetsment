# TCN_foreign_invetsment
This TCN model are based on the repo from https://github.com/philipperemy/keras-tcn <br/> <br/>
Our propose is to predict the percentage of the shareholding ratio of the foreign investors <br/> <br/>


# Model
Using TCN structure reference from https://arxiv.org/pdf/1803.01271.pdf <br/> <br/>
included casual convolutions and dilated convolutions and FC-NN(sigmoid as activation) <br/> <br/>
The hyper parameters are num_feat=28, nb_filters=24, kernel_size=8, dilations=[0,2,4,8....,64]..... (detailed in model.ipynb) <br/> <br/>

## Data preprcessing
each input with shape (1,28,15)  ==  (num of dataset, num of variables, num of days looking before) <br/>  <br/>
eacg putput with shape (1,1)     ==  (num of dataset, next day shareholdings ratio of foreign invetors ) <br/> <br/>

preprocess the data: <br/> <br/>
list_rescale = [1, 2, 3, 4, 5, 6, 32, 57, 58, 63, 67] by rescalinging each input's first date data as 1, others as 1+ incresed rate <br/> <br/>
list_n_rescale = [13, 15, 17, 19, 21, 23, 26, 29, 31, 34, 35, 37, 39, 41, 43, 59, 62] do not rescale cause its already presented as inceased rate <br/> <br/>
for total_issued variables, rescale by using median normaliztion ( x - median / MAD ) <br/> <br/>
    -> all_issued_median = 458112177.99999994 <br/> <br/>
    -> MAD = 457654065.8219999   <br/> <br/>

# Data included
variables inculding: <br/> <br/>
macro --> VIX, increase rate of domestic/government expenditure, capital construction, GDP, CPI........  <br/> <br/>
micro --> Open, High, Max, Min, Close price, ratio of volume traded, put/call ratio of taiwan 50 index....... <br/> 
(detailed can be viewed in variables.txt) <br/> <br/>

77526 in total ,54268(60%) in training ,others in testing  <br/> <br/>

data from: <br/> <br/>
https://www.stat.gov.tw/ <br/>
https://index.ndc.gov.tw/n/zh_tw <br/>
https://www.twse.com.tw/zh/ <br/>
https://www.cnyes.com/ <br/>
https://www.cbc.gov.tw/tw/mp-1.html <br/>
https://finance.yahoo.com/quote/%5EVIX/history/ <br/>

# Result
Reach loss = 0.0173 in training dataset and loss = 0.0177 (MSE) in testing dataset. (MSE)  <br/> <br/>
batch_size -> 50->100->200->200 <br/> <br/>
epochs     -> 20->10->5->10 <br/> <br/>
More detailed information can be seen in model.ipynb <br/> <br/>
