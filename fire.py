import firebase_admin
from firebase_admin import credentials, storage, db

# Initialize Firebase Admin SDK with credentials from the downloaded JSON file
cred = credentials.Certificate('cpabe-cs24-firebase-adminsdk-fbsvc-344c6ac7f5.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cpabe-cs24-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket': 'cpabe-cs24.firebasestorage.app'  # Replace with your Firebase Storage bucket name
})

# Get a reference to 'users' node in Realtime Database
ref = db.reference('staff')

# Get data from 'users' node 
data = ref.get()

# Print out the fetched data
print(data)

def upload_to_firebase(local_file_path, cloud_file_path):
    """
    Upload a file to Firebase Storage.
    :param local_file_path: Path to the local file to upload.
    :param cloud_file_path: Path in the Firebase Storage bucket.
    """
    bucket = storage.bucket()
    blob = bucket.blob(cloud_file_path)
    blob.upload_from_filename(local_file_path)
    print(f"Uploaded {local_file_path} to Firebase Storage as {cloud_file_path}.")

def download_from_firebase(cloud_file_path, local_file_path):
    """
    Download a file from Firebase Storage.
    :param cloud_file_path: Path in the Firebase Storage bucket.
    :param local_file_path: Path to save the downloaded file locally.
    """
    bucket = storage.bucket()
    blob = bucket.blob(cloud_file_path)
    blob.download_to_filename(local_file_path)
    print(f"Downloaded {cloud_file_path} from Firebase Storage to {local_file_path}.")