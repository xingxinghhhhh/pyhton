# def my_func1():
#     print("*"*20)

# my_func1()


# def mu_sum():

#     a=int(input("输入整数a的值:"))
#     b=int(input("输入整数b的值:"))
#     c=input("输入+或-或*或/")
#     if c=="+":
#         print(a+b)
#     if c=="-":
#         print(a-b)
#     if c=="*":
#         print(a*b)
#     if c=="/":
#         print(a/b)

# mu_sum()


# def my_func2(num1):
#     print("*"*num1)

# my_func2(3)

# def my_sum1(start,stop):  # 定义函数
#     sum = 0    #   定义sum=0
#     a = start    #  定义a为开始的值
#     while a<=stop:   #  当开始的值小于终止的值时走循环
#         sum += a   #  sum为上一个a的值相加  相当于 sum=sum+a
#         a += 1   #  a=a+1   a每次增加1
#     return sum   #  返回sum的值

# print(my_sum1(3,9))


# def my_squar(height,width):
#     squar=height*width
#     return squar
# print(my_squar(3,4))


# def my_func(num1,num2):
#     num1=int(input("请输入数字："))
#     num2=int(input("请输入数字："))
#     if num1%num2 == 0:
#         return True
#     else:
#         return False

# print(my_func(8,4))


# def test1():
#     a=str(input("输入姓名:"))
#     b=int(input("输入年龄:"))
#     c=input("输入身高:")
#     d="*"*20
#     print("%s\n姓名:%s\n年龄:%s\n身高:%s\n%s\n" % (d,a,b,c,d))


# def mu_sum():
#     a=int(input("输入整数a的值:"))
#     c=input("输入+或-或*或/")
#     b=int(input("输入整数b的值:"))
#     if c=="+":
#         q =a+b
#         print(q)
#     elif c=="-":
#         q =a-b
#         print(q)
#     elif c=="*":
#         q = a*b
#         print(q)
#     elif c=="/":
#         q =a/b
#         print(q)
#     else :
#         print("ss")
#     return q
# kk=mu_sum()
# print(kk)
# def my_num2():
#     print(kk+2)
# my_num2()


# name="张三"
# def my_test1():
#     global name
#     name="李四"
# my_test1()
# print(name)


# def myfunc(list1):
#     list1.clear()
# list1=[2,5,3]
# myfunc(list1)
# print(list1)


# my_sum = lambda a,b : a+b
# num = my_sum(3,6)
# print(num)


# num = (lambda a, b : a if a>b else b)(3,6)
# print(num)

# for n in range(2000,3201):
#     if n%7 ==0 and n%5!=0:
#         print(n , end=",")


# n=int(input("请输入数字："))
# b=1
# a=1
# while a<=n:
#     b=b*a
#     a+=1
#     print(b)