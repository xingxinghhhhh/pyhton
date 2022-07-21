# a = 1
# while a==1: # 当a=1时，一直打印a
#     print("a")

# a = input("请输入：")  # 接收用户输入
# while a=="6":   # 当a为6时
#     print("小红今年{0}岁了".format(a))  # 打印


# a = 0
# while a < 5 :  
#     print("hello world")
#     a += 1

# a = 5 
# while a >=0 :   # 必须满足第一步才能进入循环
#     print(a)
#     a -= 1 

# a= 0
# num=0
# while a<=50:
#     num += a
#     print(num)
#     a += 1

# 在循环内部，通过input输入，当输入exit时，退出循环
# while True :   
#     a=input("输入:")
#     if a=="exit":
#         break


# while True:
#     a = int(input())
#     if a==5:
#         print("*\n"*a)
#         continue
#     if a==10:
#         print("*\n"*a)
#         continue
#     if a>=20:
#         print("*\n"*20)
#         continue


# a = 0 
# while a< 5:  # 外面循环五次
#     b=0
#     while b <5:   # 里面循环五次
#         print("*" , end="")
#         b +=1
#     print("")
#     a +=1


# a=1
# while a<6:
#     b=1
#     while b<=a:
#         print("{0}".format(b) , end="")
#         b +=1
#     print("")
#     a +=1



# a="hello itcast"
# b=0
# for i in a :
#     print(i)
#     b+=1
# print(b)


# for i in range(0,5):
#     print("*"*5)


# 99乘法表用两种方式输出
# a=0
# while a <9:    
#     a+=1
#     b=0
#     while b <a:
#         b+=1
#         print(b,"*",a,"=",(a*b),end=" ")   
#     print()
    

# for a in range(1,10):
#     for b in range(1,a+1):
#         print(b,"*",a,"=",(a*b),end=" ")
#     print()




# a=int(input("输入整数a的值:"))
# b=int(input("输入整数b的值:"))
# print("a+b的计算结果是:",a+b)
# print("a-b的计算结果是:",a-b)
# print("a*b的计算结果是:",a*b)
# print("a/b的计算结果是:",a/b)


# a=int(input("输入整数a的值:"))
# b=int(input("输入整数b的值:"))
# c=input()
# if c=="+":
#     print(a+b)
# if c=="+":
#     print(a-b)
# if c=="*":
#     print(a*b)
# if c=="/":
#     print(a/b)


# a=input()
# if a.isdigit():
#     print(a)
# else:
#     print("请输入数字")


# 去掉空格 
# a="明日复明日   明日何其多   我生待明日   万事成蹉跎"
# b=a.replace(" ","")
# print(b)


# id= 1
# name = "刘备"
# weight = 80.2
# tel = "13912345678"
# c="*"*10
# print("%s\n编号%06d\n姓名:%s\n体重:%.3f\n电话:%s\n%s\n" %(c,id,name,weight,tel,c))