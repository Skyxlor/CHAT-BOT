from pymongo import MongoClient

import config

ROCKYdb = MongoClient(config.MONGO_URL)
ROCKY = ROCKYdb["ROCKYDb"]["ROCKY"]


from .chats import *
from .users import *
