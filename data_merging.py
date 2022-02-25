"""
Script to Merge all the CSV files into one.
The final merged file is located in: "./data/final_data.csv"
"""
import pandas as pd
import glob
import os

# path and files, cleaning the data to make the :
path = "./data/quarterly_data/"
df1 = pd.read_csv(path + 'Divvy_Trips_2019_Q1.csv')
df2 = pd.read_csv(
    path + 'Divvy_Trips_2019_Q2.csv',
    header=None, skiprows=1,
    names=[
        'trip_id', 'start_time', 'end_time', 'bikeid', 'tripduration', 'from_station_id',
        'from_station_name', 'to_station_id', 'to_station_name', 'usertype', 'gender', 'birthyear'
    ]
)
df3 = pd.read_csv(
    path + 'Divvy_Trips_2019_Q3.csv',
    header=None, skiprows=1,
    names=[
        'trip_id', 'start_time', 'end_time', 'bikeid', 'tripduration', 'from_station_id',
        'from_station_name', 'to_station_id', 'to_station_name', 'usertype', 'gender', 'birthyear'
    ]
)
df4 = pd.read_csv(
    path + 'Divvy_Trips_2019_Q4.csv',
    header=None, skiprows=1,
    names=[
        'trip_id', 'start_time', 'end_time', 'bikeid', 'tripduration', 'from_station_id',
        'from_station_name', 'to_station_id', 'to_station_name', 'usertype', 'gender', 'birthyear'
    ]
)
print(df1.shape, df2.shape, df3.shape, df4.shape)

# merging the files
df = pd.concat([df1, df2, df3, df4], ignore_index=True)
print("Final Shape:", df.shape)
df.to_csv('./data/final_data.csv', index=False)
print('Done Merging the Files...')
