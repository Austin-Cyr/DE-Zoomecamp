#!/usr/bin/env python
# coding: utf-8

import pandas as pd

#enter parameters
year = 2021
month = 1

prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow'
#replace the below with the parameters for year/month
#url = f'{prefix}/yellow_tripdata_2019-12.csv.gz'
url = f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'
url


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates
)

df.head()

pg_user
pg_pass
pg_host
pg_db

from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')


# In[14]:


df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[9]:


len(df)


# In[20]:


df_iter = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000
)


# In[21]:


from tqdm.auto import tqdm


# In[22]:


for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')


# In[ ]:


df = next(df_iter)


# In[ ]:


df


# In[ ]:




