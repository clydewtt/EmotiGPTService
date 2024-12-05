import firebase_admin
from firebase_admin import credentials, firestore
from firebase.certificate import certificate

cred = credentials.Certificate(certificate)
firebase_admin.initialize_app(cred)
db = firestore.client()