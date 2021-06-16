def to_pow(num):
    superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    return str(num).translate(superscript)


def cryp():
    # secret_message = b'message'
    # m = int.from_bytes(h.sha1(secret_message).digest(), "big")
    # print('M = {}\n'.format(m))
    # p = get_random_bigger(m)
    # g = rd.randint(0, p)
    # x = rd.randint(0, p)

    m = 5
    print('Input M = {}\n'.format(m))
    p, g, x = 11, 2, 8
    y = pow(g, x, p)
    print('y = {}{} mod {} = {}'.format(g, to_pow(x), p, y))
    print('p = {}, g = {}, y = {}'.format(p, g, y))
    # k = rd.randint(0, p - 1)
    k = 9
    print('k = {}'.format(k))
    a = g ** k % p
    b = (y ** k) * m % p
    print('a = {}{} mod {} = {}'.format(g, to_pow(k), p, a))
    print('b = {}{} * {} mod {} = {}'.format(y, to_pow(k), m, p, b))
    # print('a = {}, b = {}\n'.format(a, b))

    # Same as b*a^x^-1 mod p
    # s = pow(a, x, p)
    # new_m = (b * pow(s, p - 2, p)) % p
    #
    # print(new_m)

    new_m = (b * (pow(pow(a, x, p), -1, p))) % p
    # print(new_m)

    print('\nOutput M = {}*({}{})⁻{} mod {} = {}'.format(b, a, to_pow(x), to_pow(1), p, new_m))


def key():
    m = 16

    print('\nInput M = {}'.format(m))
    p, g, x = 43, 17, 11
    y = pow(g, x, p)
    print('y = {}{} mod {} = {}'.format(g, to_pow(x), p, y))
    print('p = {}, g = {}, y = {}'.format(p, g, y))
    k = 31
    print('k = {}'.format(k))
    # print('k = {}'.format(str(k).translate(superscript)))
    r = g ** k % p
    s = (pow(m - x * r, 1, p - 1) * pow(k, -1, p - 1)) % (p - 1)
    print('r = {}{} mod {} = {}'.format(g, to_pow(k), p, r))
    print('s = ({} - {} * {}) * {}⁻{} mod {} - 1 = {}'.format(m, x, r, k, to_pow(1), p, s))
    left = pow(y, r, p) * pow(r, s, p) % p
    right = pow(g, m, p)
    print('left  = {}{} * {}{} mod {} = {}'.format(y, to_pow(r), r, to_pow(s), p, left))
    print('right = {}{} mod {} = {}'.format(g, to_pow(m), p, right))
    # print(left, right)
    if left == right:
        print('\nSign is ok')
    else:
        print('\nSign is not ok')


def main():
    cryp()
    # key()


if __name__ == '__main__':
    main()