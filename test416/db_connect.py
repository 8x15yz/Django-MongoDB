
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from django.conf import settings

KEY = settings.MD_KEY
uri = f"mongodb+srv://hjk:{KEY}@cluster0.yr3gh6o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['Cluster0']
