


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns







def barplot_of_missing_values(df):
    
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]

    if missing_values.empty:
        print("There are no missing values")
        return
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=missing_values.index, y=missing_values.values)
    
    
    plt.title("Number of missing values")
    plt.xlabel("Column")
    plt.ylabel("Missing values")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()
