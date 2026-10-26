import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg://root:root@localhost:5432/ny_taxi")
df = pd.read_csv("taxi_zone_lookup.csv")
df.to_sql("zones2", con=engine, if_exists="replace")