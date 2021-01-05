from datetime import datetime
from sha3 import keccak_256
from coincurve import PublicKey
from secrets import token_bytes

from addrgen import read, write, keycall, leading_check

# read the search.txt file and pass the contents to the var
input_strs = read.readInputString()
print(f'Checking for the following strings: {input_strs}')

# State/module variable definitions - we are also starting the timer before entering the main loop.
current_best_zeroes = 0
count = 0
timer = datetime.now().timestamp()

while True:
    # generate new address/key combo
    private_key = keycall.newPrivate()
    public_key = keycall.newPublic(private_key)
    addr = keycall.newAddr(public_key)
    address = addr.hex()

    # Conditional loop to check for a preferred string, followed by 0 prefix
    for input_str in input_strs:
        if address.startswith(input_str.lower()):
            write.writeHit(private_key, address)
            write.printHit(private_key, address)

    # aforementioned 0 prefix checker.
    if leading_check.leading_zeroes(address) > current_best_zeroes:
        leading_check.leading_print(private_key, address)
        write.writeHit(private_key, address)
        current_best_zeroes = leading_check.leading_zeroes(address)

    # Check for millions - if true, take time measurement and print results. Reset timer.
    if str(count).endswith('000000'):
        time_per_tick = datetime.now().timestamp() - timer
        timer = datetime.now().timestamp()
        write.time_print(time_per_tick, count)

    # Add to the key-gen counter, display every 10,000.
    count += 1
    if str(count).endswith('0000'):
        write.print_progress(count)
