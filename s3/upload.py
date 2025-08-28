import boto3

s3 = boto3.client('s3', region_name='us-east-1')

s3.upload_file('s3/exemplo.txt', 'arturbogo2003', 'exemplo.txt')
print("Upload realizado com sucesso!")