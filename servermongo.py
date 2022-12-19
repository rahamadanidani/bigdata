import pymongo
from io import BytesIO
import pandas as pd
from minio import Minio
# Menghubungkan ke server minio
client = Minio('127.0.0.1:9000',
            access_key='minioadmin',
            secret_key='minioadmin',
            secure=False)
#Menghubungkan ke server mongoDb
clientMongo = pymongo.MongoClient("mongodb://localhost:27017")
db = clientMongo["dbTugasBigData"]  #Nama database mongodb
col = db["colTugasBigData"] # nama collection 

# untuk mengambil objek dari minio
response = client.get_object("tugasbigdata", "amazon")
data = pd.DataFrame(pd.read_csv(response)) # mengkonversi objek ke dataframe
#proses upload data ke mongodb
data = data.to_dict(orient="records") 
col.insert_many(data)

if col.inserted_ids is not None:
    print("Object disimpan di mongoDB!")
else:
    print("Object gagal disimpan di mongoDB!")

