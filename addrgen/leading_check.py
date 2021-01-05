# File to check and write if leading zeros returns true as > priorLeading

# Function to take the address (without 0x prefix) and count out / return consecutive 0s prefixing
def leading_zeroes(inp_str):
    cnt = 0

    for c in inp_str:
        if c == '0':
            cnt += 1
        else:
            break
    return cnt

# reads any new records to the terminal.


def leading_print(private_key, address):
    print(
        f"eth addr: 0x{address} with pvtkey {private_key.hex()} has more zeros than previous ones known")
