from schema.aws.s3.objectcreated import Marshaller
from schema.aws.s3.objectcreated import AWSEvent
from schema.aws.s3.objectcreated import ObjectCreated
import boto3
import json
import psycopg2

s3 = boto3.client('s3')

# Initiate the connection to the DB
conn = psycopg2.connect(host='', database='', user='', password='', sslmode='require')

def lambda_handler(event, context):
    # Deserialize event into strongly typed object
    awsEvent:AWSEvent = Marshaller.unmarshall(event, AWSEvent)
    eventDetail:ObjectCreated = awsEvent.detail

    try:
        if (awsEvent.detail_type == 'Object Created'):
            data = getIDSTFromS3Object(eventDetail)
            pushIDSTToAliceaDB(data)
    except Exception as e:
        print(e)

# Fetch details from S3 Bucket and parse the JSON
def getIDSTFromS3Object(detail):
    object = s3.get_object(Bucket=detail.bucket.name, Key=detail.object.key)
    return json.loads(object['Body'].read().decode('utf-8'))

# Push the data to the Postgres DB on Heroku
def pushIDSTToAliceaDB(data):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO public.test_idst_fetch_aws (id, name, data) VALUES(%s,%s,%s)", (data["id"], data["name"], json.dumps(data)))

        cur.execute("SELECT * FROM public.test_idst_fetch_aws")
        result = cur.fetchone()
        print(result)

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(e)