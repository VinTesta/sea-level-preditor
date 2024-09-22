import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_level = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(sea_level['Year'], sea_level['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        sea_level['Year'], 
        sea_level['CSIRO Adjusted Sea Level']
    )
    x = list(range(1880, 2051))
    y = [slope * i + intercept for i in x]
    plt.plot(x, y, 'r', label='fitted line 1')

    # Create second line of best fit
    sea_level_2000 = sea_level[sea_level['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(
        sea_level_2000['Year'], 
        sea_level_2000['CSIRO Adjusted Sea Level']
    )
    x = list(range(2000, 2051))
    y = [slope * i + intercept for i in x]
    plt.plot(x, y, 'g', label='fitted line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()