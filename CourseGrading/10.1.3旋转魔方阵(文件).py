"""
【问题描述】
输入一个自然数Ｎ（2到9之间），要求输出如下的魔方阵，即边长为N*N，元素取值为1至N*N，1在
左上角，呈顺时针方向依次放置各元素。
 N=3时：
    1    2    3
    8    9    4
    7    6    5
【输入形式】
从标准输入读取一个整数N。
【输出形式】
将结果输出到文件文件file.out。输出符合要求的方阵，每个数字占5个字符宽度，向右对齐，在每一行末均输出一个回车符。
【输入样例】
4
【输出样例】输出文件file.out内容为：
        1     2       3     4
     12    13    14     5
     11    16    15     6
     10      9       8     7
【评分标准】
本题不准使用数学库函数。结果正确得20分，每个测试点4分。
【提示】
print函数的格式化控制串可用来控制每个数字的占位宽度。以下输出写法使67占5个字符宽度。
     print("%5d"%(67))
"""
N = int(input())
temp = ["" for i in range(N)]
result = []
for j in range(N):
    result.append(temp)

# for a in range(N):
#     for b in range(N):

