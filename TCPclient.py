import socket
import json
import base64
from Include import SerializeKey as SerializeKey
from Include import CPABE as cp_abe
from charm.toolbox.pairinggroup import PairingGroup
from charm.core.engine.util import bytesToObject

def main():
    HOST = '127.0.0.1'  # Server's address
    PORT = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # Receive the public key (Base64 encoded)
        pk_b64 = s.recv(4096)
        if not pk_b64:
            print("No public key received from server.")
            return
        pk_str = pk_b64.decode()
        try:
            # Decode the Base64 string to bytes, then deserialize using bytesToObject.
            group = PairingGroup('MNT224')
            pk_obj = bytesToObject(base64.b64decode(pk_str), group)
        except Exception as e:
            print("Failed to load public key:", e)
            return
        print("Public key received:", pk_obj)

if __name__ == '__main__':
    main()