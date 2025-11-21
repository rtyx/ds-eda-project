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


def calculate_profit_margins(properties_df, renovated_reference, renovation_cost_per_sqft=75):
    """
    Calculate profit margins for renovation candidates.
    
    Parameters:
    -----------
    properties_df : DataFrame
        The dataframe containing properties to analyze
    renovated_reference : DataFrame
        The dataframe containing renovated properties for price reference
        Must have 'zipcode' and 'price_per_sqft' columns
    renovation_cost_per_sqft : float, optional
        Cost per square foot for renovation (default: 75)
        
    Returns:
    --------
    DataFrame
        Copy of properties_df with additional columns:
        - renovation_cost: total renovation cost
        - total_investment: purchase price + renovation cost
        - estimated_value: estimated value after renovation
        - profit_margin_pct: profit margin percentage
    """
    properties_df = properties_df.copy()
    properties_df['renovation_cost'] = properties_df['sqft_living'] * renovation_cost_per_sqft
    properties_df['total_investment'] = properties_df['price'] + properties_df['renovation_cost']
    
    post_renovation_values = []
    for idx, row in properties_df.iterrows():
        zipcode = row['zipcode']
        renovated_in_zipcode = renovated_reference[renovated_reference['zipcode'] == zipcode]
        if len(renovated_in_zipcode) > 0:
            avg_price_per_sqft = renovated_in_zipcode['price_per_sqft'].mean()
        else:
            avg_price_per_sqft = renovated_reference['price_per_sqft'].mean()
        post_renovation_values.append(row['sqft_living'] * avg_price_per_sqft * 0.9)
    
    properties_df['estimated_value'] = post_renovation_values
    properties_df['profit_margin_pct'] = ((properties_df['estimated_value'] - properties_df['total_investment']) / 
                                          properties_df['total_investment']) * 100
    return properties_df

