"""
【问题描述】求解两个整数的最大值
【输入形式】输入两个整数
【输出形式】输出两者之间的较大者
【样例输入】3 5
【样例输出】5
【样例说明】输入的两个数是3和5，程序需要自动判断5比3大，然后将5输出
【评分标准】输出正确的数，并且格式正确
【提示】
如何读入一行中的多个数字？
代码示例如下：
line = input()  #读入一行
ss = line.split()  #以空格为分隔符，得到该行字符的各个子串（本例为数字串）组成的列表ss
zs1 = int(ss[0])  #得到第一个整数
zs2 = int(ss[1])   #得到第二个整数
"""
a ,b = input().split()
a = int(a)
b = int(b)
if a > b:
    print(a)
elif a < b:
    print(b)