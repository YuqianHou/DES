# S盒置换函数 48位->32位
# 函数说明：x为48位数据
# 返回值为32位
def SBoxes(x):
    # S盒置换表
    s = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ]
    ]
    x = str(bin(int(x, 2))[2:]).zfill(48)
    y = ""
    for i in range(8):
        t = int(x[i * 6] + x[i * 6 + 5], 2)
        u = int(x[i * 6 + 1:i * 6 + 5], 2)
        y += str(bin(s[i][t][u])[2:].zfill(4))
    return y


# 密钥初始置换表
PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63,
       55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

# 密钥压缩置换表
PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

# 数据初始置换表IP
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32,
      24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47,
      39, 31, 23, 15, 7]

# 数据扩展表
EP = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
      22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# P盒置换表
PT = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4,
      25]

# 最终置换表
FP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53,
      21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1,
      41, 9, 49, 17, 57, 25]


# P盒置换函数 32位->32位
def PBox(a, x):
    s = len(a)
    y = ""
    for i in range(s):
        y += x[a[i] - 1]
    return y


# 密钥初始置换函数 64位->58位
# 函数说明：x为64位的初始密钥
# 返回值为58位
def PerCho1(x):
    return PBox(PC1, x)


# 密钥压缩置换函数 56位->48位
# 函数说明：x为56为的密钥
# 输出为48位的子密钥
def PerCho2(x):
    return PBox(PC2, x)


# 明文初始置换函数 64位->64位
# 函数说明：x为初始明文 64位
# 返回值为6位
def InitPer(x):
    return PBox(IP, x)


# 最终置换函数 64位->64位
# 函数说明：x为完成最后一轮循环得到的64为数据
# 返回值为密文或明文
def FinalPer(x):
    return PBox(FP, x)


# 数据扩展函数 32->48
# 函数说明：x为数据的右半部分 32位
# 扩展成48位的输出
def ExpPer(x):
    return PBox(EP, x)


def PerTabl(x):
    return PBox(PT, x)


# 异或运算函数
# 要求位数相同
def XOR(x, y):
    x = int(x, 2)
    y = int(y, 2)
    z = x ^ y
    return str(bin(z)[2:].zfill(32))


# 16进制转2进制函数
# 函数说明：x为16进制字符串
# 返回为2进制字符串
def HexToBin(x):
    n = len(x) * 4
    x = str(bin(int(x, 16))[2:].zfill(n))
    return x


# 2进制转16进制函数
# y为2进制字符串
# 返回值为16进制字符串
def BinToHex(y):
    return str(hex(int(y, 2)))[2:].upper()


# 密钥循环左移函数 56位->56位
# 函数说明：x为密钥
# 返回值位数不变
def LeftCircularShift(x):
    l = int(len(x) / 2)
    y = ""
    for i in range(l - 1):
        y += x[i + 1]
    y += x[0]
    for i in range(l, 2 * l - 1):
        y += x[i + 1]
    y += x[l]
    return y


def Round(x, k):
    l0 = x[:32]
    r0 = x[32:]
    l1 = r0
    ep = ExpPer(r0)
    xo = XOR(ep, k)
    sb = SBoxes(xo)
    p = PerTabl(sb)
    r1 = XOR(p, l0)
    y = l1 + r1
    return y


def swap32bit(x):
    L0 = x[:32]
    R0 = x[32:]
    y = R0 + L0
    return y


Rots = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


# DES加密函数 64位->64位
# 函数说明：text为64位的给定明文，key为密钥
# 返回值为64位的密文
def Encrypt(key, text, num):
    key = PerCho1(key)
    text = InitPer(text)
    # print('请输入需要加密的轮数（1 <= i <= 16）：')
    # num = int(input())
    for i in range(num):
        for j in range(Rots[i]):
            key = LeftCircularShift(key)
        k = PerCho2(key)
        text = Round(text, k)
    text = swap32bit(text)
    text = FinalPer(text)
    return text


# 转换明文的第num个比特位
def BitTrans(text, num):
    tmp = ''
    for i in range(0, num):
        tmp += text[i]
    if text[num] == '0':
        tmp += '1'
    else:
        tmp += '0'
    for i in range(num+1, len(text) - 1):
        tmp += text[i]
    return tmp


# print('请输入16进制明文x：')
# text = input()
text = 'EB3B4B887DF349EF'
print('16进制明文x = ' + text)
# print('请输入密钥k：')
# key = input()
key = '4F6556C45580DAD9'
print('密钥k = ' + key)
# print('请输入加密次数：')
# itr = int(input())
itr = 1

text = HexToBin(text)
textBin = text
print('2进制明文为：')
print(text)

key = HexToBin(key)
# print('2进制密钥为：')
# print(key)

for i in range(itr):
    text = Encrypt(key, text, 16)
textHex = BinToHex(text).zfill(16)
print('加密后的密文z为：')
print(textHex)
print('2进制密文z为：')
# text0 = int(text)
text0 = int(text, 2)
print(text)


# # print('请输入修改后的16进制明文x\'：')
# # text = input()
# text = 'EB3B4B987DF349EF'
# print('修改后的16进制明文x\' = ' + text)
# # print('请输入加密次数：')
# # itr = int(input())
#
# text = HexToBin(text)
# print('2进制明文为：')
# print(text)

# key = HexToBin(key)
# # print('2进制密钥为：')
# # print(key)

sum = 0
for i in range(1, 16):
    for j in range(64):
        textModified = BitTrans(text, j)
        textModified = HexToBin(textModified)
        textModified = Encrypt(key, textModified, i)
        text1 = int(textModified, 2)
        xorz = text0 ^ text1
        xorzBin = str(bin(xorz))
        tmp = xorzBin.count('1')
        sum += tmp
        print('改变明文第 ' + str(j+1) + ' 比特位后，经过 ' + str(i) + ' 轮迭代加密后，密文有 ' + str(tmp) + ' 位不同')
    sum = sum / 64.0
    print('经过 ' + str(i) + ' 轮迭代加密后 ' + 'e(' + str(i) + ') = ' + str(sum))
    if(sum >= 30 and sum <= 34):
        minNum = i
        break

print('满足题意的最小的i值为 ' + str(minNum))

# for k in range(itr):
#     text = Encrypt(key, text, i)
# textHex = BinToHex(text).zfill(16)
# print('加密后的密文z\'为：')
# print(textHex)
# print('2进制密文z\'为：')
# # text1 = int(text)
# text1 = int(text, 2)
# print(text)

# # 异或运算
# xorz = text0 ^ text1
# # 十进制转换为二进制
# xorzBin = str(bin(xorz))
# print('z^z\'为：')
# print(xorzBin)
# tmp = xorzBin.count('1')
# print('其中，z^z\'中1的个数为：' + str(tmp))
