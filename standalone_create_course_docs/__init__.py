import logging
import os

import azure.functions as func
import azure.cosmos.cosmos_client as cosmos_client

from . import course_docs


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    cosmosdb_uri = os.environ['AzureCosmosDbUri']
    cosmosdb_key = os.environ['AzureCosmosDbKey']
    cosmosdb_database_id = os.environ['AzureCosmosDbDatabaseId']
    cosmosdb_collection_id = os.environ['AzureCosmosDbCollectionId']
    xml_filename = 'kis.xml'
    xml_path = os.path.join(context.function_directory, xml_filename)
    course_docs.create_course_docs(xml_path)

    return func.HttpResponse("Hello there!")
