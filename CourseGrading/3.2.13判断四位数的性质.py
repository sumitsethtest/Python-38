"""
【问题描述】
3025这个数具有一种独特的性质：将它平分为二段，即30和25，使之相加后求平方，即(30+25)*(30+25)，恰好等于3025本身。
编写程序判断输入的四位数n是否是满足abcd=(ab+cd)*(ab+cd)这样性质的四位数，是则输出1，否则输出0。
【输入】
一个四位数n
【输出】
1或者0
【样例输入】
3025
【样例输出】
1
【样例输入】
3354
【样例输出】
0
"""
num0 = input()
abcd = int(num0)
ab = int(num0[0])*10+int(num0[1])
cd = int(num0[2])*10+int(num0[3])
if abcd == (ab+cd)*(ab+cd):
    print("1")
else:
    print(0)