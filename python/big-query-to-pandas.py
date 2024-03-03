# modules
from google.cloud import bigquery

params = {'project': 'osk-demo-277900'}
client = bigquery.Client(**params)

query = """select * 
, 'random text' as new_col 
from osk.sample"""


def bq2pd(sql):
    query_job = client.query(sql)
    results = query_job.result()
    return results.to_dataframe()


df = bq2pd(query)
print(df)
