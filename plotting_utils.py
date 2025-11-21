"""
Plotting utilities for EDA visualizations.
"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_price_comparison(df, column_name, ax, title, zero_label, non_zero_label):
    """
    Plot price comparison for missing, zero, and non-zero values of a column.
    
    Parameters:
    -----------
    df : DataFrame
        The dataframe containing the data
    column_name : str
        Name of the column to analyze
    ax : matplotlib.axes.Axes
        The axis to plot on
    title : str
        Title for the plot
    zero_label : str
        Label for the zero value category
    non_zero_label : str
        Label for the non-zero value category
    """
    # Filter data
    missing = df[df[column_name].isnull()]
    zero = df[df[column_name] == 0]
    non_zero = df[df[column_name] > 0]
    
    # Calculate average prices
    avg_price_missing = missing['price'].mean()
    avg_price_zero = zero['price'].mean()
    avg_price_non_zero = non_zero['price'].mean()
    
    # Prepare data for plotting
    categories = ['Missing', zero_label, non_zero_label]
    prices = [avg_price_missing, avg_price_zero, avg_price_non_zero]
    colors = ['#ffb703', '#8ecae6', '#06d6a0']
    
    # Create bar chart
    bars = ax.bar(categories, prices, color=colors, edgecolor='black', linewidth=1.5)
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    ax.set_ylabel('Average Price ($)', fontsize=10)
    ax.set_ylim(0, max(prices) * 1.15)
    
    # Add value labels on bars
    for bar, price in zip(bars, prices):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'${price:,.0f}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.grid(axis='y', alpha=0.3, linestyle='--')

