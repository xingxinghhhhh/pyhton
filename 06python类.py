# class cat:   # 定义类
#     def eat(self):   # 定义方法
#         print("汤姆爱吃鱼")
#     def drink(self):  # 定义方法
#         print("汤姆爱喝水")

# # 创建 lazy_cat 对象
# lazy_cat = cat()
# # 调用对象的 eat 方法
# lazy_cat.eat()
# # 调用对象的 drink 方法
# lazy_cat.drink()


# class cat:
#     def set_name(self,name):
#         self.name=name
#     def eat(self):
#         print("%s爱吃鱼" % self.name)
#     def drink(self):
#         print("%s爱喝水" % self.name)
# a=cat()
# a.set_name("哈哈")
# a.eat()
# a.drink()



# class dog:
#     def set_name(self,name):
#         self.name=name
#     def show_name(self):
#         print("小狗的名字是：%s" % self.name)

# a=dog()
# a.set_name("旺财")
# a.show_name()


# b=dog()
# b.set_name("小黑")
# b.show_name()


# class cat:
#     def __init__(self,name="猫"):
#         self.name=name
#     def eat(self):
#         print("%s爱吃鱼" % self.name)
#     def drink(self):
#         print("%s爱喝水" % self.name)

# a=cat()
# a.eat()
# a.drink()

# class cat:
#     def __init__(self,aaa,name="猫"):
#         self.name=name
#         self.aaa=aaa
#     def eat(self):
#         print("%s爱吃%s" % (self.name,self.aaa))
#     def drink(self):
#         print("%s爱喝水" % self.name)

# a=cat("鱼")
# a.eat()
# a.drink()

# class cat:
#     def __init__(self,name="猫"):
#         self.name=name
#         print("%s的带有参数的初始化方法" % self.name)
#     def __del__(self):
#         print("%s被销毁了" % self.name)
#     def eat(self):
#         print("%s爱吃鱼" % self.name)
#     def drink(self):
#         print("%s爱喝水" % self.name)

# a=cat()
# print(a)
# del a
# print("程序终止")



# class cat:
#     def __init__(self,name="猫"):
#         self.name=name
#         print("%s的带有参数的初始化方法" % self.name)
#     def __del__(self):
#         print("%s 被销毁了" % self.name)
#     def eat(self):
#         print("%s爱吃鱼" % self.name)
#     def drink(self):
#         print("%s爱喝水" % self.name)

# def test_cat():
#     lazy_cat=cat()
#     lazy_cat.eat()
# test_cat()


# class dog:
#     def __init__(self,name):
#         self.name=name
#     def aa(self):
#         print("这是一个%s对象" % self.name)
#     def __str__(self):
#         return self.name

# asd=dog("这是一个小狗类对象")
# print(asd)


# class lsls:
#     def __init__(self,oper):
#         self.oper=oper
#     def jia(self,a,b):
#         return a+b
#     def jian(self,a,b):
#         return a-b
#     def cheng(self,a,b):
#         return a*b
#     def chu(self,a,b):
#         return a/b
        
# sss=lsls()
# d=int(input("输入整数："))
# f=int(input("输入整数:"))
# c=input("请输入运算符")

# if c=="+":
#     print(sss.jia(d,f))
# elif c=="-":
#     print(sss.jian(d,f))
# elif c=="*":
#     print(sss.cheng(d,f))
# elif c=="/":
#     print(sss.chu(d,f))
# else :
#     print("输入正确的运算符")
# print(sss())


# class user:
#     def __init__(self,name,passwd):
#         self.name=name
#         self.__passwd=passwd
#     def show_name(self):
#         print("name:")  
#     def __show_passwd(self):
#         print("ss:")


# class animal:
#     def sleep(self):
#         print("睡")
#     def eat(self):
#         print("吃")

# class dog(animal):
#     def run(self):
#         print("跑")

# class fish(animal):
#     def swimming(self):
#         print("游泳")

# class bird(animal):
#     def fly(self):
#         print("飞")


# class dog(animal):
#     def run(self):
#         print("跑")
# class erha(dog):
#     def kawayi(self):
#         print("萌萌哒")


# class dog(animal):
#     def run(self):
#         print("跑")
#     def eat(self):
#         print("吃肉")


# class dog(animal):
#     def run(self):
#         print("跑")
#     def eat(self):
#         print("吃肉")
#     def sleep(self):
#         super().sleep()
#         print("睡得更多")


# class father:
#     def __init__(self,name,house):
#         self.__name=name
#         self.house=house
#     def eat(self):
#         print("吃")
#     def sleep(self):
#         print("睡")
#     def __edu_back(self):
#         print("学历")

# class son(father):
#     def show_eat(self):
#         super().eat()
#     def show_sleep(self):
#         super().sleep()
#     def show_house(self):
#         print("%s" % self.house)

# aaa=son("ss","ads")
# aaa.show_eat()
# aaa.show_sleep()
# aaa.show_house()

# class animal(object):
#     def sleep(self):
#         print("睡")
#     def eat(self):
#         print("吃")

# class dog(animal):
#     def run(self):
#         print("跑")

# a=dog()
# a.sleep()
# a.eat()


# class animal(object):
#     def food(self):
#         pass
#     def eat(self):
#         self.food()
# class dog(animal):
#     def food(self):
#         print("肉")
# class cattle(animal):
#     def food(self):
#         print("草")
# d = dog()
# # 调用父类的 eat 方法
# d.eat()
# c = cattle()
# # 调用父类的 eat 方法
# c.eat()


# class A(object):
# # name 为类属性
#     name = "tom"
#     def __init__(self):
# # 属性 age 只能通过对象访问
#         self.age = 20
# # show_name 为类方法
#     @classmethod
#     def show_name(cls):
#         print(cls.name)

# A.show_name()


# class A(object):
#     name="tom"
#     @classmethod
#     def show_name(cls):
#         print(cls.name)
#     def set_name(self,name):
#         A.name = name

# A.show_name()
# a = A()
# a.set_name("mary")
# A.show_name()


# class my_class(object):
#     n = 0
#     def __init__(self):
#         my_class.n +=1
#     @classmethod
#     def count(cls):
#         print(cls.n)

# a= my_class()
# b= my_class()
# c= my_class()
# my_class.count()