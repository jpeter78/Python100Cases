'''
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
因为他加入100，是一个完全平方数，然后再加168又是一个完全平方数，从这里分析，可以判断出，这个数应该是小于168的
小于168的话，直接用循环来做，求平方根的话，用××0.5，判断是否完全平方数的，那么小数点后面的值应该是0，把求的平
方根转为整数后，两者相等。求得156
'''
for  i in range(1,169):
    if (i + 100) ** 0.5 == int((i + 100) ** 0.5) and (i + 168) ** 0.5 == int((i + 168) ** 0.5):
        print(i)
        break
