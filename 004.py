'''
题目 输入某年某月某日，判断这一天是这一年的第几天？
用split把日期分割成年月日，然后如果是闰年的话，注意2月有29天
'''
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
        return 1
    else:
        return 0

if __name__ == "__main__":   
    riqi = input('请输入日期，格式为yyyy-mm-dd:').strip()
    days = riqi.split('-')
    year = int(days[0])
    month = int(days[1])
    day = int(days[2])
    total = 0
    DayOfMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year):
        DayOfMonth[2] += 1
    for i in DayOfMonth[:month]:
        total = total + i
    total = total + day
    print(total)
