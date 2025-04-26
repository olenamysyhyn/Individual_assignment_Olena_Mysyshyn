import os
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def sign_image(image_path, private_key_path, output_path):
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' does not exist.")
        return

    if not os.path.exists(private_key_path):
        print(f"Error: Private key file '{private_key_path}' does not exist.")
        return

    with open(image_path, 'rb') as f:
        image_data = f.read()

    hash_obj = SHA256.new(image_data)

    with open(private_key_path, 'rb') as f:
        private_key = RSA.import_key(f.read())

    signature = pkcs1_15.new(private_key).sign(hash_obj)

    with open(output_path, 'wb') as f:
        f.write(image_data)
        f.write(b'\n---SIGNATURE_START---\n')
        f.write(signature)

if __name__ == "__main__":
    image_path = '/Users/user/Desktop/individual_assignment_Olena_Mysyshyn/images/image1.jpeg'
    private_key_path = '/Users/user/Desktop/individual_assignment_Olena_Mysyshyn/keys/private_key.pem'
    output_path = '/Users/user/Desktop/individual_assignment_Olena_Mysyshyn/images/signed_image_without_innovations.jpeg'
    sign_image(image_path, private_key_path, output_path)

