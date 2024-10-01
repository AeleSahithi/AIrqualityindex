# -*- coding: utf-8 -*-
"""Air Quality Forecasting Using ML .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AqKtR9SIWEqpL92dXw6e0A6yNmw2sH06

Importing the Dependencies
"""

import numpy as np
import pandas as pd

"""Data Collection and Processing"""

#loding the data from CSV file to pandas dataframe
air_quality_data=pd.read_csv("/content/AirQualityUCI.csv")

"""The final Unnamed columns are with duplicate values means Not A Number"""

#printing the first five rows of the data frame
air_quality_data.head()

"""all the values in the CSV files are separated by ';'
Few columns have comma in the place of decmal point
"""

#loding the data fron CSV file to pandas data structure
air_quality_data=pd.read_csv("/content/AirQualityUCI.csv",sep=';',decimal=',')

#printing the firs 5rows of the dataflow
air_quality_data.head()

#removing the last 2 columns from th edataframe
air_quality_data = air_quality_data.iloc[:, :-2]

# printing th efirst five rows of the data frame
air_quality_data.head()

#printing the last five rows of the data flow
air_quality_data.tail()

air_quality_data.shape

air_quality_data.loc[[9356]]

"""9356 represents the last dat point in the data frame &remaining rows are just null values

index =9356
row =9357th row
take the first 9357 rows alone from the dataframe
"""

air_quality_data=air_quality_data.head(9357)

air_quality_data.head()

air_quality_data.tail()

air_quality_data.shape

"""getting information about the data set"""

air_quality_data.info

# counting th enumber of times -200 appears in the data
air_quality_data.isin([-200]).sum(axis=0)

"""**Handling the missing numbers**

Convert all -200 to NaN

Replace all NaN values with mean of that specific values
"""

air_quality_data=air_quality_data.replace(to_replace=-200,value=np.NaN)

#checking the number of missing values in the data frame
air_quality_data.isnull().sum()

"""This shows the actual number of missing values"""

air_quality_data.tail()

air_quality_data.mean()

#repalcing the missing values with mean value
air_quality_data=air_quality_data.fillna(air_quality_data.mean())

air_quality_data.tail()

#checking the number of missing values in the data frame
air_quality_data.isnull().sum()

"""two tasks that can be performed on this data frame

1.Forecasting(based on th epevious trends this predicts the future trends) 2.Regressiom

**Fore casting wit fbProphet Algorithm **
"""

#converting the data from  DD/MM/YYYY To  YYYY-MM-DD
date_info=pd.to_datetime(air_quality_data['Date'])
print(date_info)

time_info=air_quality_data['Time']
print(time_info)

time_info=time_info.apply(lambda x:x.replace('.',':'))
print(time_info)

print(type(date_info))
print(type(time_info))

#combining 2 series to a pandas dataframe
date_time=pd.concat([date_info,time_info],axis=1)

date_time.head()

date_time.shape

#combining date and time

date_time['ds']=date_time['Date'].astype(str)+' '+ date_time['Time'].astype(str)

date_time.head()

date_time.info()

"""We have to convert ds from object to date time format"""

data=pd.DataFrame()

data['ds']=pd.to_datetime(date_time['ds'])

data.head()

data['y']=air_quality_data['RH']

data.head()

pip install Prophet

from prophet import Prophet

# training the prophet model

model = Prophet()
model.fit(data)

future=model.make_future_dataframe(periods=365,freq='H')
future.tail()

forecast=model.predict(future)
forecast[['ds','yhat','yhat_lower','yhat_upper']].tail()

fig1=model.plot(forecast)

fig2=model.plot_components(forecast)