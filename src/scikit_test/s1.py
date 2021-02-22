import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

# 加载数据
oecd_bli = pd.read_csv("../datasets/oced_bli_2015.csv", thousands=',')
gdp_per_capita = pd.read_csv("../datasets/gdp_per_capita.csv", thousands=",", delimiter='\t',
                             encoding='latin1', na_values="n/a")
# 准备数据

