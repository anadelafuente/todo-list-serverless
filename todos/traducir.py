#Código función lambda Translate
#devuelve una entrada de la ToDo list, traducida al idioma que se solicite a través del API
import json
import logging
import boto3
import os
import time
from todos import decimalencoder
translate = boto3.client('translate')
#dynamodb = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
#TABLE_NAME = os.getenv('TABLE_NAME')
#logger = logging.getLogger()
#logger.setLevel(logging.INFO)



def traducir(event, context):
    source_language = "auto"#reconocimiento automático con Comprehend
    target_language = event['pathParameters']['lang']
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    response = table.get_item(
        Key={
           'id': event['pathParameters']['id']
        }
    )
    #review = response['item']['text']
    result = {
        'TranslatedText': translate.translate_text(Text=response['Item']['text'], SourceLanguageCode='auto', TargetLanguageCode=target_language)
    }

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['TranslatedText'])
    }

    return response