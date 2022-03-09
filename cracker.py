import hashlib
from typing import Final

NOT_FOUND_MSG: Final = "PASSWORD NOT IN DATABASE"

def crack_sha1_hash(hash: str) -> str:
    """
    Brute forces a SHA-1 hash and returns it
    """

    file = open('passwords.txt', 'r')

    # Read and compare every password with the hash
    for pw in file.readlines():
        # Trim off the new line from the string
        pw = pw.rstrip("\n").encode()
    	
        # Instantiate the hash and start comparing
        hash_object: hashlib._Hash = hashlib.sha1(pw)

        if hash_object.hexdigest() != hash:
            continue;

        return pw.decode()

    return NOT_FOUND_MSG