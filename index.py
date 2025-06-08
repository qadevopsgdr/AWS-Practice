import json
import boto3
from help import print_name

s3 = boto3.resource('s3')
def handler(event, context):
    # TODO implement
    bucketlist = []
    print_name("GDR")
    print("Durga-zipfile")
    for bucket in s3.buckets.all():
        
        print(bucket.name)
        bucketlist.append(bucket.name)
        print(json.dumps(bucketlist))
    return {
        'statusCode': 200,
        #'body': json.dumps('Hello from Lambda!')
        "body": bucketlist
    }