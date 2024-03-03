# modules
from google.cloud import bigquery

client = bigquery.Client(project='osk-demo-277900')

query = """select * from osk.sample"""

query_job = client.query(query)
results = query_job.result()
# df = results.to_dataframe()

# print(df)
for r in results:
    print(r.id, r.label, r.value)