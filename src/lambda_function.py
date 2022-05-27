import json
import boto3
import re

def lambda_handler(event, context)
    # TODO implement
    client = boto3.client(rekognition)
    s3 = boto3.client(s3)
    fileObj = s3.get_object(Bucket = imgdetector, Key = imgstar01.jpeg)
    file_content = fileObj[Body].read()
    # response = client.detect_text(Image = {S3Object{Bucketimgdetector,Nameimgstar01.jpeg}})
    response = client.detect_text(Image = {S3Object{Bucketimgdetector204646-dev,Namepublicmy-photo.jpg}})
    
    textDetections=response['TextDetections']
    nTarjeta = ''
    nVal = ''
    fExpira = ''
    fVal = ''
    print ('Detected textn----------')
    for text in textDetections
            dt = text['DetectedText']
            val = {.2f}.format(text['Confidence']) + %
            print ('Detected text' + text['DetectedText'])
            print ('Confidence ' + {.2f}.format(text['Confidence']) + %)
            print ('Id {}'.format(text['Id']))
            if 'ParentId' in text
                print ('Parent Id {}'.format(text['ParentId']))
            print ('Type' + text['Type'])
            print()
            
            if re.search(([0-9]{4})+[' ']+([0-9]{4})+[' ']+([0-9]{4})+[' ']+([0-9]{4}), dt)
                print ('Numero tarjeta {}'.format(dt))
                nTarjeta = dt
                nVal = val
            if re.search(([0-9]{2})+['']+([0-9]{2}), dt)
                print ('Fecha Expira {}'.format(dt))
                fExpira = dt
                fVal = val
            
            
    return {Tarjeta{nTarjetanTarjeta,nValnVal,fExpirafExpira,fValfVal}}
    
    
    return {
        'statusCode' 200,
        'body' json.dumps('Hello from Lambda!')
    }
