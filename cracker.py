import hashlib
from typing import Final

NOT_FOUND_MSG: Final = "PASSWORD NOT IN DATABASE"

def sha1hash(txt: str) -> str:
    txt = txt.encode()

    hash = hashlib._Hash = hashlib.sha1(txt)
    return hash.hexdigest()


def crack_sha1_hash(hash: str, use_salts: bool = False) -> str:
    """
    Brute forces a SHA-1 hash and returns it
    """
    passwords = open('passwords.txt', 'r').readlines()

    # Read and compare every password with the hash
    for pw in passwords:
        # Trim off the new line from the string
        pw = pw.rstrip("\n")

        #  ... each salt string from the file `salts.txt` should be appended AND prepended to each 
        # password from `passwords.txt` before hashing and before comparing it to the hash passed into the function.
        if use_salts:
            salts = open('salts.txt', 'r').readlines()
            for salt in salts:
                salt = salt.rstrip("\n")

                # Map over the possibilities of salting
                # and up if the hash is in the array of hashes
                if hash in [sha1hash(x) for x in [salt + pw, pw + salt]]:
                    return pw

        if sha1hash(pw) == hash:
            return pw

    return NOT_FOUND_MSG