import boto3
import json
import os


def lambda_handler(event, context):
    client = boto3.client('lambda')

    function = {
        "ApplicantEvent": os.environ["LAMBDA_APPLICANT_EVENT"],
        "JobEvent": os.environ["LAMBDA_JOB_EVENT"],
        "MatchingEvent": os.environ["LAMBDA_MATCHING_EVENT"]
    }

    for record in event['Records']:
        if record['eventName'] == "INSERT":
            keys = record['dynamodb']['Keys']
            payload = {"uuid": keys['uuid']['S']}
            client.invoke(FunctionName=function[keys['type']['S']], InvocationType='Event', Payload=json.dumps(payload))
