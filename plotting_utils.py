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


def plot_comparison_bar_chart(ax, categories, values, colors=None, title='', ylabel='', 
                               value_format='${:,.0f}', add_grid=True, y_limit_factor=1.15):
    """
    Create a comparison bar chart with standardized styling.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes
        The axis to plot on
    categories : list
        List of category labels
    values : list
        List of values corresponding to categories
    colors : list, optional
        List of colors for each bar. Defaults to ['steelblue', 'coral', ...]
    title : str, optional
        Title for the plot
    ylabel : str, optional
        Label for the y-axis
    value_format : str, optional
        Format string for value labels on bars (default: '${:,.0f}')
    add_grid : bool, optional
        Whether to add grid lines (default: True)
    y_limit_factor : float, optional
        Factor to multiply max value for y-axis limit (default: 1.15)
        
    Returns:
    --------
    bars : BarContainer
        The bar container object from matplotlib
    """
    # Default colors if not provided
    if colors is None:
        default_colors = ['steelblue', 'coral', 'lightgreen', 'salmon', 'skyblue']
        colors = default_colors[:len(categories)]
    
    # Create bar chart
    bars = ax.bar(categories, values, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
    
    # Set title and labels
    if title:
        ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=10)
    
    # Set y-axis limit
    if values and max(values) > 0:
        ax.set_ylim(0, max(values) * y_limit_factor)
    
    # Add value labels on bars
    for bar, value in zip(bars, values):
        height = bar.get_height()
        # Format the value label
        try:
            label = value_format.format(value)
        except (ValueError, KeyError):
            label = str(value)
        
        ax.text(bar.get_x() + bar.get_width()/2., height,
                label,
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Add grid if requested
    if add_grid:
        ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    return bars

