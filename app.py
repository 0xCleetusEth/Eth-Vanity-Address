from datetime import datetime
from sha3 import keccak_256
from coincurve import PublicKey
from secrets import token_bytes

from addrgen import read, write, keycall, leading_check

# read the search.txt file and pass the contents to the var
input_strs = read.readInputString()
print(f'Checking for the following strings: {input_strs}')

current_best_zeroes = 0
count = 0
timer = datetime.now().timestamp()

while True:
    private_key = keycall.newPrivate()
    public_key = keycall.newPublic(private_key)
    addr = keycall.newAddr(public_key)

    for input_str in input_strs:
        address = addr.hex()
        if address.startswith(input_str.lower()):
            write.writeHit(private_key, address)
            write.printHit(private_key, address)

        if leading_check.leading_zeroes(address) > current_best_zeroes:
            leading_check.leading_print(private_key, address)
            write.writeHit(private_key, address)
            current_best_zeroes = leading_check.leading_zeroes(address)

    if str(count).endswith('000000'):
        time_per_tick = datetime.now().timestamp() - timer
        timer = datetime.now().timestamp()
        write.time_print(time_per_tick, count)

    count += 1
    if str(count).endswith('0000'):
        write.print_progress(count)
