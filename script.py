from datetime import datetime
from secrets import token_bytes

from coincurve import PublicKey
from sha3 import keccak_256

import txt_interfacing

input_strs = []
with open('.\\txt_interfacing\\search.txt', 'r') as f:
    for line in f.readlines():
        input_strs.append(line.rstrip())

print(f'Checking for the following strings: {input_strs}')


def leading_zeroes(inp_str):
    cnt = 0
    for c in inp_str:
        if c == '0':
            cnt += 1
        else:
            break
    return cnt


def print_progress(_count):
    print("     ", '\x1b[6;30;42m' +
          f"{_count:,} addresses generated" + '\x1b[0m', end="\r")


count = 0
timer = datetime.now().timestamp()
current_best_zeroes = 0
while True:
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(
        private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    for input_str in input_strs:
        address = addr.hex()
        if address.startswith(input_str.lower()) or leading_zeroes(address) > current_best_zeroes:
            print(f'\x1b[5;30;44m' + 'private_key:',
                  private_key.hex() + f'\x1b[0m')
            print(f'\x1b[5;30;44m' + 'eth addr: 0x' + address + f'\x1b[0m')
            with open('.\\txt_interfacing\\found.txt', 'a') as f:
                f.write("\n\n eth addr: 0x" + address +
                        "\n with pvtkey: " + private_key.hex())

            if leading_zeroes(address) > current_best_zeroes:
                print(
                    f"eth addr: 0x{address} with pvtkey {private_key.hex()} has more zeros than previous ones known")
                current_best_zeroes = leading_zeroes(address)

    if str(count).endswith('000000'):
        time_per_tick = datetime.now().timestamp() - timer
        timer = datetime.now().timestamp()
        print(
            f"Count: {count:,} - Time per 1,000,000: {time_per_tick} seconds, or { 1000000 / time_per_tick:,} addr/sec")

    count += 1
    if str(count).endswith('0000'):
        print_progress(count)
