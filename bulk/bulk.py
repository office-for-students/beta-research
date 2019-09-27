import uuid
from utils import get_collection_link, get_cosmos_client

client = get_cosmos_client()
print(client)

collection_link = get_collection_link(
    "AzureCosmosDbDatabaseId", "AzureCosmosDbCoursesCollectionId"
)
print(collection_link)

sproc_link = collection_link + "/sprocs/spBulk"


def create_cosmos_entity(id):
    return {"id": id, "test": "1"}


new_docs = []
counter = 0
while counter < 50:
    new_docs.append(create_cosmos_entity(str(uuid.uuid4())))
    counter += 1

options = {"partitionKey": "1"}
client.ExecuteStoredProcedure(sproc_link, [new_docs], options)
