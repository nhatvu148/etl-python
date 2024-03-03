from google.cloud import bigquery

client = bigquery.Client(project='osk-demo-277900')
table_id = 'osk-demo-277900.osk.city_house_prices'


job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True
)

filename = '/Users/oscar/github/mysql-2-gbq/data_files/city_house_prices.csv'

with open(filename, 'rb') as source_file:
    load_job = client.load_table_from_file(
        source_file,
        table_id,
        job_config=job_config
    )

load_job.result()

destination_table = client.get_table(table_id)  # Make an API request.
print("You have {} rows in your table.".format(destination_table.num_rows))

# Exercise: a file of your own using auto-detect. What are the results?
