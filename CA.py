import socket
import json
import base64
from charm.toolbox.pairinggroup import PairingGroup
from charm.schemes.abenc.ac17 import AC17CPABE
from charm.core.engine.util import objectToBytes, bytesToObject

def main():
    HOST = ''  # Listen on all available interfaces
    PORT = 12345

    # Initialize CP-ABE scheme and generate public key and master secret key
    group = PairingGroup('MNT224')
    cpabe = AC17CPABE(group, 2)
    pk, msk = cpabe.setup()

    # Serialize the public key using objectToBytes, then encode as Base64 string
    pk_bytes = objectToBytes(pk, group)
    pk_b64 = base64.b64encode(pk_bytes).decode('utf-8')

    # Save the public key to a file
    with open("public_key.json", "w") as f:
        json.dump(pk_b64, f)
    print("Public key saved to 'public_key.json'.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print("Server is listening...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                # Send the Base64-encoded public key to the client
                conn.sendall(pk_b64.encode())
                print("Public key sent to the client.")

if __name__ == "__main__":
    main()