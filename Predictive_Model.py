import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data1 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data2 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data3 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data4 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data5 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data6 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data7 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data8 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data9 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data10 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data11 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')
data12 = pd.read_csv('/Users/scotttow123/Personal -- Projects/Location.csv')