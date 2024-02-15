import numpy as np  #Mathematical Caluculations
import matplotlib.pyplot as mtp #2D Plotting of Data. Data Visulization 
import pandas as pd #Importing and Managing Datasets.

data_set=pd.read_csv("C:/Users/JABIR/OneDrive/Desktop/Datasets.csv") #Reading of Data From .csv File and Stored in Variable data_set.
print(data_set) #prints dataset

data_set.head() #prints the first 5 rows of the dataset.
data_set.shape #print No of Rows and Columns. 
data_set.drop(['Unnamed: 4'], axis=1) #Drop the Column Named "Unnamed:4" From the Dataset. 
