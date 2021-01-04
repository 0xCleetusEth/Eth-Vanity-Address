from sha3 import keccak_256
from coincurve import PublicKey
from secrets import token_bytes

private_key = keycall.newPrivate()
public_key = keycall.newPublic(private_key)
addr = keycall.newAddr(public_key)

print('address: 0x' + addr)
print('private: ' + private_key.hex())

private_key = keccak_256(token_bytes(32)).digest()
print('private: ', private_key.hex() + '\n')

pub = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
print('public key: ', pub.hex() + '\n')

ad = keccak_256(pub).digest()[-20:]
print('address: 0x' + ad.hex() + '\n')
