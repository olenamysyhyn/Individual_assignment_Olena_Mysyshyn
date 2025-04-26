import os
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def verify_image(image_path, public_key_path):
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' does not exist.")
        return False

    if not os.path.exists(public_key_path):
        print(f"Error: Public key file '{public_key_path}' does not exist.")
        return False

    with open(image_path, 'rb') as f:
        content = f.read()

    insert_position = 1024
    signature_size = 512  
    signature = content[insert_position:insert_position + signature_size]
    image_data = content[:insert_position] + content[insert_position + signature_size:]

    hash_obj = SHA256.new(image_data)

    with open(public_key_path, 'rb') as f:
        public_key = RSA.import_key(f.read())

    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        print('Signature is valid.')
        return True
    except (ValueError, TypeError):
        print('Signature is invalid.')
        return False

if __name__ == "__main__":
    signed_image_path = '/Users/user/Desktop/individual_assignment_Olena_Mysyshyn/images/signed_image.jpeg'
    public_key_path = '/Users/user/Desktop/individual_assignment_Olena_Mysyshyn/keys/public_key.pem'
    verify_image(signed_image_path, public_key_path)
