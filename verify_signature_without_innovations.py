import os
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def verify_image(image_path, public_key_path):
    if not os.path.exists(image_path):
        return False

    if not os.path.exists(public_key_path):
        return False

    with open(image_path, 'rb') as f:
        content = f.read()

    if b'---SIGNATURE_START---' not in content:
        print('No signature found in the image.')
        return False

    image_data, signature = content.split(b'\n---SIGNATURE_START---\n')
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
    signed_image_path = '/Users/user/Desktop/individual_assignment_Olena_Mysyshyn/images/signed_image_without_innovations.jpeg'
    public_key_path = '/Users/user/Desktop/individual_assignment_Olena_Mysyshyn/keys/public_key.pem'
    verify_image(signed_image_path, public_key_path)
