import pyodbc
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# SQL Server connection parameters
server = "serveraguiar.database.windows.net"
database = "dbaguiar"
username = "aguiarpaulo"
password = "xxxxxx"
driver = "{ODBC Driver 17 for SQL Server}"

# Azure Blob Storage connection parameters
azure_storage_connection_string = "https://cloudshell188987196.blob.core.windows.net/raw"  #"your_azure_storage_connection_string"
container_name = "raw"

# Create SQL Server connection
sql_connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
sql_conn = pyodbc.connect(sql_connection_string)

# Query data from SQL Server
query = "SELECT * FROM dbo.Orders"
cursor = sql_conn.cursor()
cursor.execute(query)
data = cursor.fetchall()

# Close SQL Server connection
sql_conn.close()

# Create Azure Blob Storage client
blob_service_client = BlobServiceClient.from_connection_string(azure_storage_connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Upload data as a CSV file to Azure Blob Storage
csv_data = "\n".join([",".join(map(str, row)) for row in data])
blob_name = "data.csv"
blob_client = container_client.get_blob_client(blob_name)
blob_client.upload_blob(csv_data, overwrite=True)

print(f"Data uploaded to Azure Blob Storage: {blob_name}")
