import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('places')

def findPlaces(distance):
    response=table.get_item(Key={'distance': distance})
    if 'Item' in response:
        return{'fulfillmentText':response['Item']['place']}
    else:
        return{'fulfillmentText':'No Places within given distance'}
        

    
def main(event, context):
    distance=event['queryResult']['parameters']['distance']
    return findPlaces(int(distance))
