import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

# load the data
oecd_bli = pd.read_csv("../datasets/oecd_bli_2015.csv")
gdb_per_capita = pd.read_csv("../datasets/gdp_per_capita.csv", thousands=',',
                             sep='\t', encoding='latin1', na_values='n/a')

def prepare_count_stats(oecd_bli, gdp_per_capita):
    """
This function just merges the OECD's life satisfaction data and the IMF's GDP per capita data.
It's a bit too long and boring and it's not specific to Machine Learning, which is why I left it out of the book.
    """
    oecd_bli = oecd_bli[oecd_bli['INEQUALITY'] == 'TOT']
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdb_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdb_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdb_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", "Life satisfaction"]].iloc[keep_indices]

    # Prepare the data
