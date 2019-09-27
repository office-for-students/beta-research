import uuid
from utils import get_collection_link, get_cosmos_client

client = get_cosmos_client()
print(client)

collection_link = get_collection_link(
    "AzureCosmosDbDatabaseId", "AzureCosmosDbCoursesCollectionId"
)
print(collection_link)

with open("spBulkCreate.js") as file:
    file_contents = file.read()

sproc_definition = {"id": "spBulk", "serverScript": file_contents}
sproc = client.CreateStoredProcedure(collection_link, sproc_definition)
