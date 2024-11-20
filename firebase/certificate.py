import os
from dotenv import load_dotenv

load_dotenv()

certificate = {
    "type": os.environ["FIRESTORE_TYPE"],
    "project_id": os.environ["FIRESTORE_PROJECT_ID"],
    "private_key_id": os.environ["FIRESTORE_PRIVATE_KEY_ID"],
    "private_key": os.environ["FIRESTORE_PRIVATE_KEY"],
    "client_email": os.environ["FIRESTORE_CLIENT_EMAIL"],
    "client_id": os.environ["FIRESTORE_CLIENT_ID"],
    "auth_uri": os.environ["FIRESTORE_AUTH_URI"],
    "token_uri": os.environ["FIRESTORE_TOKEN_URI"],
    "auth_provider_x509_cert_url": os.environ["FIRESTORE_AUTH_PROVIDER_URL"],
    "client_x509_cert_url": os.environ["FIRESTORE_CLIENT_URL"],
    "universe_domain": os.environ["FIRESTORE_UNIVERSE_DOMAIN"],
}