from sha3 import keccak_256
from coincurve import PublicKey
from secrets import token_bytes

# Function to call the creation of a new private key- returns to app.py


def newPrivate():
    private_key = keccak_256(token_bytes(32)).digest()
    return private_key

# Subsequent calling of the file - uses prior private key to create a public key


def newPublic(private_key):
    public_key = PublicKey.from_valid_secret(
        private_key).format(compressed=False)[1:]
    return public_key

# Function to take a public key and return it. Note, both the private key and the address need to be casted using .hex() appending a
# print or variable readout


def newAddr(public_key):
    addr = keccak_256(public_key).digest()[-20:]
    return addr
