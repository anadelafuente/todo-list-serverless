#Código función lambda Translate
#devuelve una entrada de la ToDo list, traducida al idioma que se solicite a través del API
import json
import time
import logging
import os

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')
