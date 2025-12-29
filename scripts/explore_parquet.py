# import duckdb

# df = duckdb.query("""
#     SELECT *
#     FROM 'yellow_tripdata_2025-01.parquet'
#     LIMIT 10
# """).df()

# print(df)


# import pandas as pd

# df = pd.read_parquet("yellow_tripdata_2025-01.parquet", engine="pyarrow")
# print(df.head(50))
# print(df.shape)

import pandas as pd

df = pd.read_parquet("yellow_tripdata_2025-01.parquet", engine="pyarrow")
df.to_csv("yellow_tripdata_2025-01.csv", index=False)
