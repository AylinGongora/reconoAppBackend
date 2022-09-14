import json
import boto3
import re

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client("rekognition")
    s3 = boto3.client("s3")
    fileObj = s3.get_object(Bucket = "imgdetector", Key = "imgs/tar01.jpeg")
    file_content = fileObj["Body"].read()
    # response = client.detect_text(Image = {"S3Object":{"Bucket":"imgdetector","Name":"imgs/tar01.jpeg"}})
    response = client.detect_text(Image = {"S3Object":{"Bucket":"imgdetector204646-dev","Name":"public/my-photo.jpg"}})
    
    textDetections=response['TextDetections']
    nTarjeta = ''
    nVal = ''
    fExpira = ''
    fVal = ''
    stringsValues = []
    print ('Detected text\n----------')
    for text in textDetections:
            dt = text['DetectedText']
            val = "{:.2f}".format(text['Confidence']) + "%"
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            print()
            
            if re.search("([0-9]{4})+[' ']+([0-9]{4})+[' ']+([0-9]{4})+[' ']+([0-9]{4})", dt):
                print ('Numero tarjeta: {}'.format(dt))
                nTarjeta = dt
                nVal = val
            elif re.search("([0-9]{2})+['/']+([0-9]{2})", dt):
                print ('Fecha Expira: {}'.format(dt))
                fExpira = dt
                fVal = val
            else:
                nombres = {
                          "nombre": dt,
                          "porcentaje": val
                        }
                stringsValues.append(nombres)
                
    response = client.detect_text(Image = {"S3Object":{"Bucket":"imgdetector204646-dev","Name":"public/cvc.jpg"}})
    
    textDetections=response['TextDetections']
    nCvc = ''
    pCvc = ''
    print ('Detected text\n----------')
    for text in textDetections:
            dt = text['DetectedText']
            val = "{:.2f}".format(text['Confidence']) + "%"
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            print()
            
            if re.search("[0-9]{3}", dt):
                if len(dt) == 3:
                    if val == "100.00%":
                        print ('Cvc: {}'.format(dt))
                        nCvc = dt
                        pCvc = val
            
    return {"Tarjeta":{"nTarjeta":nTarjeta,"nVal":nVal,"fExpira":fExpira,"fVal":fVal, "nCvc":nCvc, "pCvc":pCvc, "stringsValues":stringsValues}}
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
