import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"C:\Users\dhruv\PycharmProjects\TheDeigningSphere\thedesigningsphere\designing_sphere\key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
name = {
    'Name': 'Dhruv Kohli',
    'kl_mail': '2200033125@kluniversity.in',  # Changed 'kl mail' to 'kl_mail' for consistency
    'email': 'dhruvkohli67@gmail.com',
    'mobile': '9116538867',
}

doc_ref = db.collection('taskCollections').document()
doc_ref.set(name)

print('Document id:', doc_ref.id)
