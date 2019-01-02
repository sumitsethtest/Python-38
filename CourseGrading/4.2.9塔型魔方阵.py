"""
【问题描述】输入一个自然数Ｎ（1<=N<=9），要求输出如下的魔方阵，即边长为2*N-1，Ｎ在中心出现一次，其余位置上的数字从外向中心逐渐增大。
N=3时：
11111
12221
12321
12221
11111
N=4时：
1111111
1222221
1233321
1234321
1233321
1222221
1111111
【输入形式】从标准输入读取一个整数N。
【输出形式】向标准输出打印结果。输出符合要求的方阵，每个数字占一个字符宽度，在每一行末均输出一个回车符。
【输入样例】3
【输出样例】
11111
12221
12321
12221
11111
【样例说明】输入自然数3，则输出边长为5的方阵，3在方阵的中间出现一次，其余位置上的数字从外向中心逐渐增大。
"""
N = int(input())
i = 1
temp = []
for a in range(2 * N - 1):
    add = []
    for f in range(2 * N - 1):
        add.append(i)
    temp.append(add)
for b in range(N):
    for c in range(b, 2 * N - b - 1):
        temp[b][c] = temp[c][b] = temp[c][2 * N - b - 2] = temp[2 * N - b - 2][c] = i
    i += 1
for d in range(2 * N - 1):
    for e in range(2 * N - 1):
        print(temp[d][e], end = "")
    print()
