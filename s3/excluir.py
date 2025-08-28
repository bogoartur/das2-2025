import boto3

s3 = boto3.client('s3')

bucket = s3.Bucket('arturbogo2003')

obj = bucket.Object('exemplo.txt')
obj.delete()
print("Arquivo excluído com sucesso!")