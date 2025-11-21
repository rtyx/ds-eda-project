"""
Data processing utilities for EDA.
"""

import pandas as pd


def detect_outliers_iqr(df, column):
    """
    Detect outliers using IQR method.
    
    Parameters:
    -----------
    df : DataFrame
        The dataframe containing the data
    column : str
        Name of the column to analyze
        
    Returns:
    --------
    dict
        Dictionary containing:
        - column: column name
        - Q1: first quartile (25th percentile)
        - Q3: third quartile (75th percentile)
        - IQR: interquartile range
        - lower_bound: lower bound for outliers
        - upper_bound: upper bound for outliers
        - outlier_count: number of outliers detected
        - outlier_percentage: percentage of outliers
        - min_value: minimum value in the column
        - max_value: maximum value in the column
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    outlier_count = len(outliers)
    outlier_percentage = (outlier_count / len(df)) * 100
    
    return {
        'column': column,
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'outlier_count': outlier_count,
        'outlier_percentage': outlier_percentage,
        'min_value': df[column].min(),
        'max_value': df[column].max()
    }

