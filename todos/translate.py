#Código función lambda Translate
#devuelve una entrada de la ToDo list, traducida al idioma que se solicite a través del API
import logging
import json
import boto3
import os
import time
from todos import decimalencoder
translate = boto3.client('translate')
dynamodb = boto3.client('dynamodb')
TABLE_NAME = os.getenv('TABLE_NAME')
logger = logging.getLogger()
logger.setLevel(logging.INFO)



def traducir(event, context):
    data = json.loads(event['body'])
    source_language = "auto"#reconocimiento automático con Comprehend
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    response = table.get_item(
        Key={
           'id': event['pathParameters']['id']
        }
    )
    result = translate.translate_text(response['text'], source_language, data['language'])

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result.get('TranslatedText'),
                           cls=decimalencoder.DecimalEncoder)
    }

    return response