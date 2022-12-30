import pymongo

def connect_db():
    client = pymongo.MongoClient("mongodb+srv://ali:ali@node-jwt-api.y5yg8.mongodb.net/test")

    # Memilih database
    db = client["uas_daspro"]

    # Memilih koleksi
    collection = db["uas_daspro"]
    return collection