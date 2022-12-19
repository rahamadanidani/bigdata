from io import BytesIO
import pandas as pd
from minio import Minio
#MenghubungKan ke server minio
minioClient = Minio('127.0.0.1:9000',
            access_key='minioadmin',
            secret_key='minioadmin',
            secure=False)

df = pd.DataFrame()
csv_bytes = df.to_csv().encode('utf-8')
csv_buffer = BytesIO(csv_bytes)
#Mengupload dataset ke bucket minio 
minioClient.result = minioClient.fput_object("tugasbigdata", "amazon", "amazon.csv", content_type="application/csv",)
