from google.cloud import bigquery

client = bigquery.Client(project='osk-demo-277900')
table_id = 'osk-demo-277900.osk.profiles'


job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV
)

filename = '/Users/oscar/github/mysql-2-gbq/data_files/profiles_001.csv'

with open(filename, 'rb') as source_file:
    load_job = client.load_table_from_file(
        source_file,
        table_id,
        job_config=job_config
    )

load_job.result()

destination_table = client.get_table(table_id)
print("You have {} rows in your table.".format(destination_table.num_rows))

# Exercise: write additional code that will loop through profile_xx.csv files and
# load them into the profiles table
