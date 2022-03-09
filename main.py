import cracker


cracked_password1 = cracker.crack_sha1_hash(
    "fbbe7e952d1050bfb09dfdb71d4c2ff2b3d845d2")
print(cracked_password1)

cracked_password2 = cracker.crack_sha1_hash(
    "dcc466796201f7232b22a03781110a8871fd038c", use_salts=True)
print(cracked_password2)
