🔐 CPABE using Blowfish for Secure Cloud Storage
This project integrates Ciphertext-Policy Attribute-Based Encryption (CP-ABE) with the Blowfish symmetric encryption algorithm to secure data before uploading it to Google Cloud Platform (GCP). It uses Firebase for user and storage management. The system ensures that only authorized users—based on attribute policies—can access and decrypt cloud-stored data.

⚠️ This is a work-in-progress prototype. Contributions, refinements, and feedback are welcome!

📁 Project Structure
File/Module	Description
CA.py	Certificate Authority – Initializes CP-ABE system and key setup
generate_test_file.py	Generates and encrypts sample files for testing and uploads to cloud
CP_ABE.py	Main module implementing CP-ABE (AC17 Type-III) and Blowfish (CBC mode)
Fire.py	Firebase integration (Authentication & Cloud Storage API support)
TCPclient(User).py	Acts as the client for uploading/downloading/decrypting files

🔧 How to Use
1. 🔑 Run the Certificate Authority
Set up CP-ABE system:
python CA.py
2. 📄 Generate & Upload Encrypted Test File
Encrypt a sample file with Blowfish and upload to GCP:
python generate_test_file.py
3. 🔐 Run the CP-ABE Scheme
Perform CP-ABE encryption/decryption with Blowfish integration:
python CP_ABE.py
Uses AC17CPABE with Type-III pairing group

Data is encrypted using Blowfish (CBC Mode) before CP-ABE encryption

4. ☁️ Firebase Integration
Handles backend operations with GCP:
python Fire.py
5. 👤 Run the Client (User Interface)
Client can download and decrypt files based on CP-ABE policy:
python TCPclient(User).py
🔒 Encryption Workflow
User Uploads File:

File is encrypted with Blowfish

Blowfish key is encrypted using CP-ABE based on attribute policy

Both are uploaded to Firebase (GCP Storage)

User Requests File:

Based on user's attributes, CP-ABE checks access

If attributes satisfy the policy:

Blowfish key is decrypted

File is decrypted using the Blowfish key

🛠 Tech Stack
Python

Charm Crypto Library – for CP-ABE (AC17 Type-III)

PyCryptodome – Blowfish encryption in CBC mode

Google Firebase (GCP) – Cloud Storage & Authentication

Socket Programming – Client-server file transfer

🚧 Status
🔄 Under active development
✅ Functional prototype is ready
🧪 Needs refinement and extensive testing

📢 Contributing
Feel free to fork, raise issues, or contribute improvements to:

Code structure

Security enhancements

Access policy design

UI/UX for the client side

📄 License
This project is open-source and licensed under the MIT License.
