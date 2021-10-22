
# name = input("请输入姓名：")
# age  =  input("请输入年龄")
# print("你叫{},今年{}岁了".format(name,age))


# for i in range(1,11):
#     print("叔衡走的第{}天，想他！".format(i))

# i = 0
# while i <= 9:
#     i = i + 1
#     print(i)

# for i  in range(101):
#     if i%7 ==0:
#         print(i)




# N = 10
# sum = 0
# i = 0
#
# while i < N:
#     number = int(input())
#     sum += number
#     i = i +1
#     average = sum/N
# print(average)


# F = float(input())
# C = (F - 32)/1.8
# print("{:5.2f}".format(C))


#打印斐波那契数列
# a = 0
# b = 1
#
# while b < 20:
#     print(b)
#     a,b = b,a + b


# physics = float(input('physics:'))
# math = float(input('math:'))
# history = float(input('history:'))
# if (physics + math + history)< 120:
#     print('failed')
# else:
#     print('passed')

# lst = [1,2,3,4]
# def plus(num):
#     return num + 1
# print(list(map(plus,lst)))



# minute = int(input())
# print("{}H,{}M".format(int(minute/60),minute%60))

#写程序求出100以内的所有素数
# for i in range(0,1001):
#     if i%2 != 0 and i%3 !=0 and i%5 !=0 and i%7 !=0:
#         print(i)


#楼层打印99乘法表

# for i in range(1,17):
#      print(i)




# while True:
#     A,B = map(int,input().split())
#     print(A+B)

# n = int(input())
# i = 1
# while i <= n:
#          A,B = map(int,input().split())
#          print(A+B,type(A+B))
         # i = i + 1




#打印列表中所有元素
# L = [11,22,33,44,55]
# s = ""
#
# for i  in range():
#     s = s + str(len[l])
# print(s)





# L = [1,2,3,4,5]
#
# L2 = []
# L2.append(L.pop())
# print(L2)

# import collections
# d = collections.deque()
# d.append(0)
# print(d)


# import collections
# d = collections.deque()
# d.append(' ')
# print(d)

# l = []
# l.append(' ')
# print(l)

# aaa=['黑色','红色','白色','黑色']
# ccc={'黑色':'黄色','红色':'白色'}
# bbb=[ccc[i] if i in ccc else i for i in aaa]
# print(bbb)

# a = -1
# a = abs(a)
# print(a)




# L = []
# a,b,c = map(int,input('请输入三角形的三条边，用空格隔开：').split(' '))
# L.append(a)
# L.append(b)
# L.append(c)
# L.sort()
# m = max(a,b,c)
# n = min(a,b,c)
# l = L[1]
# if l > m+n or l < m-n:
#     print('该三角形不成立！')
# elif a == b == c:
#     print('该三角形是等边三角形！')
# elif a == b or a == c or b == c:
#     print('该三角形是等腰三角形！')
# elif l**2 + n**2 == m**2:
#     print('该三角形是直角三角形！')
# else:
#     print('该三角形是一般三角形！')

# m,n = map(int,input('请输入鸡和兔的总头数和总脚数，用空格隔开:').split(' '))
# s = (n - m*2)/2
# t = m - s
# print('兔子个数:{}，鸡的个数:{}'.format(int(s),int(t)))

#列表中多个元素同时替换(需要用到字典）
# l = [1,2,3,4,1]
# d = {1:0,2:1}
# L = [d[i] if i in d else i for i in l]
# print(L)

# 函数求和
# def plus(*S):
#     d = 0
#     for i in S:
#         d = d + i
#     return d
# t = plus(1,2,3)
# print(t)

# 函数求俩个数的最大公约数
# a = int(input())
# b = int(input())
# def gac(a,b):
#     m = max(a, b)
#     n = min(a, b)
#     r = m % n
#     if r == 0:
#         d = n
#     else:
#         while r != 0:
#             m = n
#             n = r
#             r = m % n
#         d = n
#     return (d)
# print(gac(a,b))


# 输入两个数，输出两个数的最小公倍数（运用两个函数，其中一个为求最大公因数）
a,b = map(int,input().split(' '))
def _gcd(a, b):
    m = max(a, b)
    n = min(a, b)
    r = m % n
    if r == 0:
        d = n
    else:
        while r != 0:
            m = n
            n = r
            r = m % n
        d = n
    return (d)
def lcm(a, b):
    s = _gcd(a, b)
    if s == 1:
        t = a * b
    elif s != 1:
        f = a / s
        h = b / s
        t = f * h * s
    return (int(t))
print(lcm(a, b))