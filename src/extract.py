import pandas as pd 
import zipfile
import requests
from io import BytesIO

def get_openpowerlifting_data():
    url = "https://openpowerlifting.gitlab.io/opl-csv/files/openpowerlifting-latest.zip"
    response = requests.get(url)
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        csv_filename = [f for f in z.namelist() if f.endswith('.csv')][0]
        with z.open(csv_filename) as csvfile:
            chunk_iter = pd.read_csv(csvfile, chunksize=500000)
            chunk_one = next(chunk_iter)
            print(chunk_one.head())


get_openpowerlifting_data()