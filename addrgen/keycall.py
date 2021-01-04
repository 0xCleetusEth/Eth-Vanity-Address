from sha3 import keccak_256
from coincurve import PublicKey
from secrets import token_bytes


def newPrivate():
    private_key = keccak_256(token_bytes(32)).digest()
    return private_key


def newPublic(private_key):
    public_key = PublicKey.from_valid_secret(
        private_key).format(compressed=False)[1:]
    return public_key


def newAddr(public_key):
    addr = keccak_256(public_key).digest()[-20:]
    return addr
