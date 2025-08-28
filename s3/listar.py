import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = boto3.resource('s3').Bucket('arturbogo2003')
for obj in bucket.objects.all():
    print(obj.key)


