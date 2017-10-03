import time

def method1():
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    wkd = [(1+366)%7,]      #每月1日的星期数(对7取余)
                            #1901.1.1的星期数
        
    for year in range(1901, 2001):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            months[1] = 29
        else:
            months[1] = 28  #判断闰年
                
        for i in range(len(months)):
            wkd.append((wkd[-1]+months[0])%7)

    return wkd.count(0)

def method2():
    from datetime import date
    from itertools import starmap,product

    count = 0
    for day in starmap(date, product(range(1901,2001),range(1,13),(1,))):
        if day.weekday() == 6:      #weekday()返回的0-6是星期一到星期日
            count += 1
    return count

t1 = time.time()
print(method1())
t2 = time.time()
print(t2-t1)
print(method2())
t3 = time.time()
print(t3-t2)
