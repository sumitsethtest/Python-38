"""
【问题描述】
 编写程序，功能是输入一个数，输出该数的绝对值。
【输入形式】
 输入一个实数。
【输出形式】
 对应输入数的绝对值。
【样例输入】
 2.0
【样例输出】
 2.0
【样例输出说明】
输出结果时小数点后保留1位。
"""
n = float(input())
if n >= 0:
    print("%.1f" % n)
else:
    print("%.1f" % -n)