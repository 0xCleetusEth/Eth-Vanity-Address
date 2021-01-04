

def writeHit(private_key, address):
    with open('found.txt', 'a') as f:
        f.write("\n\n eth addr: 0x" + address +
                "\n with pvtkey: " + private_key.hex())


def printHit(private_key, address):
    print(f'\x1b[5;30;44m' + 'eth addr: 0x' + address + f'\x1b[0m')
    print(f'\x1b[5;30;44m' + 'private_key:', private_key.hex() + f'\x1b[0m')


def print_progress(_count):
    print("     ", '\x1b[6;30;42m' +
          f"{_count:,} addresses generated" + '\x1b[0m', end="\r")


def time_print(time_per_tick, count):
    print(f"Count: {count:,} - Time per 1,000,000: {time_per_tick} seconds, or { 1000000 / time_per_tick:,} addr/sec")
