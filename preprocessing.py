import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer


def features_remove(met_data):
    """
    Input: DNA methylation data
    Output: DNA methylation data loại bỏ đi feature bị thiếu hơn 20% giá trị
    """
    missing_percentage = met_data.isna().mean(axis=1) * 100
    features_to_remove = list(missing_percentage[missing_percentage > 20].index)
    filtered_data = met_data.drop(index = features_to_remove)
    filrered_data = filtered_data.reset_index(drop=True)
    return filtered_data


def KNNimpute(met_data, neighbors = 3):
    """
    Input: DNA methylation data
    Output: DNA methylation data sau khi được thêm các feature bị thiếu bằng phương pháp KNN
    """
    pass


def fill_missing_data(data):
    """
    Input: DNA methylation data
    Output: DNA methylation data fill missing value bằng mean
    """
    temp = data.copy()
    df_num = temp.drop(columns='Composite Element REF')
    data_numpy = df_num.to_numpy(dtype="float32")
    row_means = np.nanmean(data_numpy, axis=1)
    inds = np.where(np.isnan(data_numpy))
    data_numpy[inds] = np.take(row_means, inds[0])
    df_num_filled = pd.DataFrame(data_numpy, columns=df_num.columns)
    filled_data = pd.concat([temp['Composite Element REF'].reset_index(drop=True),
                             df_num_filled.reset_index(drop=True)],
                             axis=1)
    return filled_data


def highest_scoring_features(data, features_num=1, threshold=0.5):
    """
    Input: data từng gene
    Ouput: expression_difference val của từng feature: wi = (mi,1 - mi,0) / (sigmai,1 + sigmai,0)
    """
    identifiers = data.iloc[:, 0]
    data_val = data.iloc[:, 1:].astype(float)
    result = {}
    for idx in data.index:
        row = data_val.loc[idx]
        high = row[row >= threshold]
        low = row[row < threshold]
        mean_high, mean_low = high.mean(), low.mean()
        std_high, std_low = high.std(), low.std()
        expression_difference_val = (mean_high - mean_low) / (std_high + std_low)
        result[idx] = expression_difference_val
    diff = pd.Series(result)
    top_indices = diff.sort_values(ascending=False).head(features_num).index
    pp_data = data.loc[top_indices].copy()
    return pp_data