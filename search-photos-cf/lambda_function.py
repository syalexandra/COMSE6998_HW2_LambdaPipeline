import json
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    #event is {"q":"show me dogs and cats"}
    # s3: photo-album-b2
    #output should be the photo id in the photo-album-b2
    """
    client = boto3.client('lexv2-runtime')
    
    #botId, botAliasId, localeId, sessionId, text, sessionState, requestAttributes
    
    BOTID = "YAWFAYPXFD"
    BOTALIASID = "TSTALIASID"
    SESSIONID = 'user'
    LOCALEID= 'en_US'
    INPUTTEXT1 = 'Show me photos'
    
    INPUTTEXT2 = 'Give me photos with Cats and Trees'
    
    response = client.recognize_text(
        botId=BOTID,
        botAliasId=BOTALIASID,
        localeId=LOCALEID,
        sessionId=SESSIONID,
        text=INPUTTEXT1,
        #sessionState='',
        #requestAttributes=''
        )
    
    response2 = client.recognize_text(
        botId=BOTID,
        botAliasId=BOTALIASID,
        localeId=LOCALEID,
        sessionId=SESSIONID,
        text=INPUTTEXT2,
        #sessionState='',
        #requestAttributes=''
        )
    
    print(response['messages'])
    print(response2['sessionState']["intent"]["slots"]["PhotoTypes"])
    """
    return {
        'statusCode': 200,
        'body': ["https://photo-album-b2.s3.amazonaws.com/1.jpg","https://photo-album-b2.s3.amazonaws.com/24_3_2022_21_29_23.jpg"]
    }
