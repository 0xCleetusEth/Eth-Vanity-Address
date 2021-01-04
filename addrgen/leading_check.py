
def leading_zeroes(inp_str):
    cnt = 0

    for c in inp_str:
        if c == '0':
            cnt += 1
        else:
            break
    return cnt


def leading_print(private_key, address):
    print(
        f"eth addr: 0x{address} with pvtkey {private_key.hex()} has more zeros than previous ones known")
    current_best_zeroes = leading_zeroes(address)
