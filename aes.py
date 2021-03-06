import numpy as np


class AES:
    def __init__(self, code_bytes, key):
        self.code_bytes = code_bytes.reshape((4, 4)).T
        self.key = key.reshape((4, 4)).T
        self.key_exp = 0
        self.SboxE = np.array(
            [[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
             [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
             [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
             [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
             [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
             [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
             [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
             [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
             [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
             [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
             [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
             [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
             [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
             [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
             [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
             [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]])
        self.SboxD = np.array([
             [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
             [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
             [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
             [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
             [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
             [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
             [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
             [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
             [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
             [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
             [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
             [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
             [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
             [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
             [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
             [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]])
        self.ME = np.array([
            [2, 3, 1, 1],
            [1, 2, 3, 1],
            [1, 1, 2, 3],
            [3, 1, 1, 2]
        ])
        self.MD = np.array([
            [0x0e, 0x0b, 0x0d, 0x09],
            [0x09, 0x0e, 0x0b, 0x0d],
            [0x0d, 0x09, 0x0e, 0x0b],
            [0x0b, 0x0d, 0x09, 0x0e],
        ])
        self.Rcon = np.array([
            [0x01, 0x00, 0x00, 0x00],
            [0x02, 0x00, 0x00, 0x00],
            [0x04, 0x00, 0x00, 0x00],
            [0x08, 0x00, 0x00, 0x00],
            [0x10, 0x00, 0x00, 0x00],
            [0x20, 0x00, 0x00, 0x00],
            [0x40, 0x00, 0x00, 0x00],
            [0x80, 0x00, 0x00, 0x00],
            [0x1b, 0x00, 0x00, 0x00],
            [0x36, 0x00, 0x00, 0x00],
        ]).T
        np.set_printoptions(formatter={'int': '{:02x}'.format})

    def __str__(self):
        return np.array_str(self.code_bytes.T.flatten())

    def show(self):
        print(self.code_bytes, '\n')

    def split_hex(self, value):
        return divmod(value, 0x10)

    def get_bytes(self, value):
        high, low = self.split_hex(value)
        return self.SboxE[high, low]

    def get_bytes_rev(self, value):
        high, low = self.split_hex(value)
        return self.SboxD[high, low]

    def sub_bytes(self):
        self.code_bytes = np.array([self.get_bytes(by) for by in self.code_bytes])

    def sub_bytes_rev(self):
        self.code_bytes = np.array([self.get_bytes_rev(by) for by in self.code_bytes])

    def shift_rows(self):
        self.code_bytes[1] = np.roll(self.code_bytes[1], -1)
        self.code_bytes[2] = np.roll(self.code_bytes[2], -2)
        self.code_bytes[3] = np.roll(self.code_bytes[3], -3)

    def shift_rows_rev(self):
        self.code_bytes[1] = np.roll(self.code_bytes[1], 1)
        self.code_bytes[2] = np.roll(self.code_bytes[2], 2)
        self.code_bytes[3] = np.roll(self.code_bytes[3], 3)

    def mix_columns(self):
        res_list = []
        for row_c_b in self.code_bytes.T:
            for row_me in self.ME:
                res = 0
                for c_c_b, c_me in zip(row_c_b, row_me):
                    res ^= g_m(c_c_b, c_me)
                res_list.append(res)
        self.code_bytes = np.array(res_list).reshape((4, 4)).T

    def mix_columns_rev(self):
        res_list = []
        for row_c_b in self.code_bytes.T:
            for row_me in self.MD:
                res = 0
                for c_c_b, c_me in zip(row_c_b, row_me):
                    res ^= g_m(c_c_b, c_me)
                res_list.append(res)
        self.code_bytes = np.array(res_list).reshape((4, 4)).T

    def key_expansion(self, round):
        row, col = self.key.shape
        key_exp = np.zeros((row, col * (round + 1)), dtype=int)
        key_exp[:, :4] = self.key
        for i in range(1, round + 1):
            new_row = np.array([self.get_bytes(by) for by in np.roll(key_exp[:, (i * 4) - 1], -1)])
            new_row = key_exp[:, (i - 1) * 4] ^ new_row ^ self.Rcon[:, i - 1]
            l = [new_row]
            for j in range(1, 4):
                new_row = key_exp[:, ((i - 1) * 4) + j] ^ new_row
                l.append(new_row)
            key_exp[:, (i * 4): (i * 4) + 4] = np.array(l).T
        self.key_exp = key_exp

    def full_cycle(self, round):
        print('Input array\n')
        self.show()
        self.key_expansion(round)
        print('Round {}\n'.format(0))
        self.add_round_key(0)
        self.show()
        for i in range(1, round + 1):
            print('Round {}\n'.format(i))
            self.sub_bytes()
            self.show()
            self.shift_rows()
            self.show()
            if i != round:
                self.mix_columns()
                self.show()
            self.add_round_key(i)
            self.show()

    def add_round_key(self, key_i):
        print('Key:', self.key_exp[:, key_i * 4:(key_i * 4) + 4].flatten(), '\n')
        self.code_bytes = self.code_bytes ^ self.key_exp[:, key_i * 4:(key_i * 4) + 4]

    def reverse_cycle(self, round):
        self.key_expansion(round)
        print(self.key_exp.T.flatten().reshape((round + 1, 16)))
        print()
        self.show()
        for i in range(round, 0, -1):
            print('Rev round {}\n'.format(i))
            self.add_round_key(i)
            self.show()
            if i != round:
                self.mix_columns_rev()
                self.show()
            self.shift_rows_rev()
            self.show()
            self.sub_bytes_rev()
            self.show()
        self.add_round_key(0)
        self.show()


def m_p(polynomial1, polynomial2):  # multiply_polynomials
    result = 0
    for i in range(len(bin(polynomial2)) - 2):
        if polynomial2 & (1 << i):
            result ^= polynomial1 << i
    return result


def d_p(polynomial1, polynomial2):  # divide_polynomials
    quotient = 0
    reminder = polynomial1
    while len(bin(reminder)) >= len(bin(polynomial2)):
        shift = len(bin(reminder)) - len(bin(polynomial2))
        reminder ^= polynomial2 << shift
        quotient ^= 1 << shift
    return quotient, reminder


def g_m(polynomial1, polynomial2):  # galois_multiply
    mul_res = m_p(polynomial1, polynomial2)
    return d_p(mul_res, 0x11b)[1]


def main():
    # with open('text.txt', 'rb') as f:
    #     data = f.read(16)
    #     input_text = np.array([l for l in data])

    # print(input_text)

    # with open('t_out.txt', 'wb') as f:
    #     f.write(bytearray([0xD0, 0x9D, 0xD0, 0xB5, 0x20, 0xD1, 0x81, 0xD0, 0xBB, 0xD0, 0xB5, 0xD0, 0xB4, 0xD1, 0x83, 0x65]))

    input_text = np.array([0xD0, 0x9D, 0xD0, 0xB5, 0x20, 0xD1, 0x81, 0xD0, 0xBB, 0xD0, 0xB5, 0xD0, 0xB4, 0xD1, 0x83, 0x65]).reshape((4,4)).T.flatten()
    key        = np.array([0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F])
    # rever_text = np.array([0xf9, 0x0d, 0xb4, 0xc0, 0xba, 0xc0, 0xee, 0x99, 0x9c, 0xd3, 0x58, 0x87, 0xed, 0xa0, 0x83, 0x98])
    # input_text = np.array([0x19, 0x3d, 0xe3, 0xbe, 0xa0, 0xf4, 0xe2, 0x2b, 0x9a, 0xc6, 0x8d, 0x2a, 0xe9, 0xf8, 0x48, 0x08])
    # key        = np.array([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])
    # input_text = np.array([0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34])

    cycles = 10

    aes = AES(input_text, key)
    aes.full_cycle(cycles)
    print('---------------------------------------------\n')
    print(aes, '\n')
    # print(aes.key_exp.T.flatten().reshape((cycles + 1, 16)))
    aes.reverse_cycle(cycles)

# D0 9D D0 B5 20 D1 81 D0 BB D0 B5 D0 B4 D1 83 65
# 00 04 08 0c 01 05 09 0d 02 06 0a 0e 03 07 0b 0f key

# D0 99 D8 B9 21 D4 88 DD B9 D6 BF DE B7 D6 88 6A
# 70 EE 61 56 FD 48 C4 C1 56 F6 08 1D A9 F6 C4 02
# 70 EE 61 56 48 C4 C1 FD 08 1D 56 F6 02 A9 F6 C4
# 32 24 3A 82 FA F3 F4 72 2E F0 0D 0B D4 B9 C3 62
# E4 F6 E0 54 50 5C 52 D9 5A 82 75 7D 29 43 32 9C
# d6 d2 da d6 aa af a6 ab 74 72 78 76 fd fa f1 fe key

# rev
# df 26 5f 48 d8 3d ae 63 52 42 7b a0 d5 54 1a dd
# b6 64 be 68 92 3d 9b 30 cf bd c5 b3 0b f1 00 fe key
# 69 42 E1 20 4A 00 35 53 9D FF BE 13 DE A5 1A 23
# 69 42 E1 20 53 4A 00 35 BE 13 9D FF A5 1A 23 DE
# E4 F6 E0 54 50 5C 52 D9 5A 82 75 7D 29 43 32 9C

if __name__ == '__main__':
    main()