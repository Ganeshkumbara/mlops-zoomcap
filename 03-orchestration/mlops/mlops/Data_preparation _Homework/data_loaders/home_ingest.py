import requests
from io import BytesIO
from typing import List

import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def ingest_files(**kwargs) -> pd.DataFrame:
    # dfs: List[pd.DataFrame] = []

    # for year, month in [(2023, 3)]:
    #     for i in range(month):
    #         response = requests.get(
    #             'https://github.com/mage-ai/datasets/raw/master/taxi/green'
    #             f'/{year}/{i:02d}.parquet'
    #         )
    response = requests.get(
        "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet"
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.text)

    df = pd.read_parquet(BytesIO(response.content))
    # dfs.append(df)

    return df