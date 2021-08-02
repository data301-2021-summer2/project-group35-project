import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas_profiling

def load_and_process_df_Method_Chain_by_Year(path_to_csv_file):

    df_Method_Chain_by_Year1 = (
        pd.read_csv("/Users/stevenzonneveld/Desktop/data301/project-group35-project/data/raw/MileStone1.csv")
        .drop(columns = ['Unnamed: 0', 'price', 'title_status', 'color', 'state', 'mileage'], axis = 0)
        .sort_values(by = ['brand'])
        #.drop( df_cleaned [ df_cleaned ['brand'] == 'peterbilt'].index, inplace=True)  #could not figure out how to use .drop in method chaining.
        .rename(columns = {"brand": "Manufacturer", "year": "Model Year"})   
        )
    df_Method_Chain_by_Year2 = df_Method_Chain_by_Year1.drop( df_Method_Chain_by_Year1 [ df_Method_Chain_by_Year1 ['Manufacturer'] == 'peterbilt'].index)
    
    return df_Method_Chain_by_Year2

def load_and_process_df_Method_Chain_by_Mileage(path_to_csv_file):

    df_Method_Chain_by_Mileage1 = (
        pd.read_csv("/Users/stevenzonneveld/Desktop/data301/project-group35-project/data/raw/MileStone1.csv")
        .drop(columns = ['Unnamed: 0', 'price', 'title_status', 'color', 'state', 'year'], axis = 0)
        .sort_values(by = ['brand'])
        #.drop( df_cleaned [ df_cleaned ['brand'] == 'peterbilt'].index, inplace=True) #could not figure out how to use .drop in method chaining.
        #.drop( df_cleaned [ df_cleaned ['mileage'] == 0.0 ].index, inplace=True)      #could not figure out how to use .drop in method chaining.    
        .rename(columns = {"brand": "Manufacturer", "mileage": "Mileage"})
    )
    df_Method_Chain_by_Mileage2 = df_Method_Chain_by_Mileage1.drop( df_Method_Chain_by_Mileage1 [ df_Method_Chain_by_Mileage1 ['Manufacturer'] == 'peterbilt'].index)
    df_Method_Chain_by_Mileage3 = df_Method_Chain_by_Mileage2.drop( df_Method_Chain_by_Mileage2 [ df_Method_Chain_by_Mileage2 ['Mileage'] == 0.0 ].index)
    
    return df_Method_Chain_by_Mileage3    