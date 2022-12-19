import pymongo
from io import BytesIO
import pandas as pd

#menghubungkan ke server mongodb
clientMongo = pymongo.MongoClient("mongodb://localhost:27017")
db = clientMongo["dbTugasBigData"]
col = db["colTugasBigData"]
#mengambil data dalam bentuk dataframe
data = pd.DataFrame(list(col.find()))
#menampilkan dataframe
print(data)