from AES import AES
import numpy as np


a = AES(0x2b7e151628aed2a6abf7158809cf4f3c)
#a.print_key()

encriped = a.encript(0x3243f6a8885a308d313198a2e0370734)
a.print_data()
#print(list(range(9,0,-1)))
#print(0x28^0xa0)
#### round const

# round_const = [0x00,0x01]
# a = 0x01
# for i in range(30):
#     a = a*0x02
#     if a > 0xff:
#         a = a^0b100011011
#     round_const.append(a)
# np.set_printoptions(formatter={'int': hex})
# print(np.array(round_const))


# array = [[0 for x in range(4)] for y in range(4)]
# print(array)
# block = range(128)
# print(block)
#
# for i in range(4):
#     for j in range(4):
#         print(block[32 * i + 8 * j : 32 * i + 8 * (j+1)])
#         array[j][i] = block[32 * i + 8 * j : 32*i + 8*(j+1)]
#     print(" ")
#
# print(" ")
# for i in range(4):
#     for j in range(4):
#         print(array[i][j])