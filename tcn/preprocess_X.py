import pandas as pd
import numpy as np

def preprocess_x(X):
    X.columns = X.loc[0]

    Delete_list_1 = [7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 25, 27, 28, 30, 33, 36, 38, 40, 42]
    Delete_list_2 = list(range(45, 57))
    Delete_list_3 = [60, 61, 64, 65, 66, 68, 69]

    D = Delete_list_1 + Delete_list_2 + Delete_list_3

    ## remove index

    for i in range(len(D)):
        X = X.drop(D[i], axis=0)
    ## remove comma

    for i in range(1,16):
        try:
            X.loc[63][i] = X.loc[63][i].replace(",", "")
        except:
            print(f"comma remove fail in index {i} ")

    ## rescale list
    list_rescale = [1, 2, 3, 4, 5, 6, 32, 57, 58, 63, 67]
    list_n_rescale = [13, 15, 17, 19, 21, 23, 26, 29, 31, 34, 35, 37, 39, 41, 43, 59, 62]
    list_i = [44]

    ## replace to float
    for i in list_rescale + list_n_rescale:
        for j in range(1, 16):
            try:
                X.loc[i][j] = float(X.loc[i][j])
            except:
                print(f"Fail to convert to float{i}")

    ## median normalization(TO DO: exponential transfer?)
    all_issued_median = 458112177.99999994
    MAD = 457654065.8219999
    X.loc[63][1:] = (X.loc[63][1:] - all_issued_median)/(MAD)

    list_rescale.remove(63)
    ## rescale left
    X_re = X.loc[list_rescale]

    ## extract every first nonzero value in each row
    norm = X_re.replace(0, np.nan).bfill(1).iloc[:, 1]

    ## divide
    X_re = X_re.iloc[:, 1:].divide(norm, axis=0)
    X_re = X_re.fillna(0)


    ## for non rescale part
    X_n = X.loc[list_n_rescale]
    X_n = X_n.replace(0, np.nan)
    X_n = X_n.iloc[:, 1:] / 100
    X_n.loc[59] = X_n.loc[59] - 1
    X_n.loc[62] = X_n.loc[62] - 1
    X_n = X_n.fillna(0)

    ## for interest
    X_i = X.loc[[44]].iloc[:, 1:]

    X = pd.concat([X_re,X_n,X_i],axis = 0)

    return X


if __name__ == '__main__':

    X = pd.read_csv("train1-0.csv")
    Y = pd.read_csv("answer1-0.csv")

    df = preprocess_x(X)

