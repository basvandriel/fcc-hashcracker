import hashlib
from typing import Final

NOT_FOUND_MSG: Final = "PASSWORD NOT IN DATABASE"

def crack_sha1_hash(hash: str, use_salts: bool = False) -> str:
    """
    Brute forces a SHA-1 hash and returns it
    """
    passwords_file = open('passwords.txt', 'r')
    salts_file = open('salts.txt', 'r')

    # passwords = []
    salts = salts_file.readlines()


    # Read and compare every password with the hash
    for pw in passwords_file.readlines():
        # Trim off the new line from the string
        pw = pw.rstrip("\n")

        #  ... each salt string from the file `salts.txt` should be appended AND prepended to each 
        # password from `passwords.txt` before hashing and before comparing it to the hash passed into the function.
        if use_salts:
            for known_salt in salts:
                known_salt = known_salt.rstrip("\n")

                # Append and prepend the password
                prependedhash: hashlib._Hash = hashlib.sha1(f"{known_salt}{pw}".encode())
                appendedhash: hashlib._Hash = hashlib.sha1(f"{pw}{known_salt}".encode())

                if prependedhash.hexdigest() == hash:
                    return pw

                if appendedhash.hexdigest() == hash:
                    return pw

        hash_object: hashlib._Hash = hashlib.sha1(pw.encode())

        if hash_object.hexdigest() != hash:
            continue

        return pw.decode()

    return NOT_FOUND_MSG