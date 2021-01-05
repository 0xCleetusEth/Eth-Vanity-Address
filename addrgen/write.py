# File that provides append/general communication
# Appends an address + pvtkey to the found.txt file - called by app.py when new leading 0s or hit on the address targets
def writeHit(private_key, address):
    with open('found.txt', 'a') as f:
        f.write("\n\n eth addr: 0x" + address +
                "\n with pvtkey: " + private_key.hex())

# Writes to the console log, highlighted, if a target address is returned. Called by app.py


def printHit(private_key, address):
    print(f'\x1b[5;30;44m' + 'eth addr: 0x' + address + f'\x1b[0m')
    print(f'\x1b[5;30;44m' + 'private_key:', private_key.hex() + f'\x1b[0m')

# Continuous printing of the addresses scanned - called every 10,000 addresses. Config in app.py


def print_progress(_count):
    print("     ", '\x1b[6;30;42m' +
          f"{_count:,} addresses generated" + '\x1b[0m', end="\r")

# addr/second calc and terminal readout - default config is every 1,000,000 addresses.


def time_print(time_per_tick, count):
    print(f"Count: {count:,} - Time per 1,000,000: {time_per_tick} seconds, or { 1000000 / time_per_tick:,} addr/sec")
