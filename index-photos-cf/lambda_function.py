import json
import os
import boto3
s3_client=boto3.client('s3')
rek_client=boto3.client('rekognition')
import requests
import datetime


def lambda_handler(event, context):
    # TODO implement
    temp=event["Records"][0]["s3"]
    bucket_name=temp["bucket"]["name"]
    object_key=temp["object"]["key"]
    
    
    response = rek_client.detect_labels(Image={'S3Object':{'Bucket':bucket_name,'Name':object_key}},MaxLabels=5)
    custom_labels=s3_client.head_object(Bucket='photo-album-b2',Key='1.jpg')['ResponseMetadata']['HTTPHeaders']['x-amz-meta-customlabels']
    detect_labels=[]
    for l in response['Labels']:
        detect_labels.append(l['Name'])
    
    
    for l in custom_labels.split(","):
        detect_labels.append(l)
    
    result_dict={"objectKey":object_key,\
                 "bucket":bucket_name,\
                 "createdTimestamp":datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),\
                 "labels":detect_labels
    }
    print(result_dict)
    
    master = "COMSE6998"
    password = "Comse6998!"
    host_url = "https://search-photo-search-cxrf6gegik5b3jqre7fgna4gga.us-east-1.es.amazonaws.com/photo-search/_doc/"+object_key
    headers={"Content-Type": "application/json"}
    response = requests.put(host_url, auth=(master,password),json=result_dict)
    query = {
            'size': 1,
            'query': {
                'multi_match': {
                'query': 'Outer Space',
                'fields': ['labels']
                }
                  
            }
                
        }
    host_url = "https://search-photo-search-cxrf6gegik5b3jqre7fgna4gga.us-east-1.es.amazonaws.com/photo-search/_search"
    
    response = requests.get(host_url, auth=(master,password),json=query)
    data = response.json()
    #print(data)
    n=len(data['hits']['hits'])
    file_name=[]
    for i in range(n):
        file_name.append(data['hits']['hits'][i]['_id'])
    
    print(file_name)
    
    
    
    
    
