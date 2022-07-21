# 列表       
# list1=["asfafs","asd","ss"]
# print(dir(list1))
# list1.insert(0,"aaa")   # 在指定位置插入数据
# list1.append("sdasdasdasd")     # 在末尾追加数据
# list1[0]= "asda11231"    # 修改指定索引的数据
# del(list1[0])    # 删除指定索引的数据
# list1.remove("asd")   # 删除第一次出现的指定数据
# list1.pop()   # 删除末尾数据
# list1.pop("ss")    # 删除指定索引数据 
# list1.clear()    # 清空列表
# print(list1.count("ss"))   # 返回指定数据在列表中出现的次数
# print(list1.index("ss"))   # 返回数据在列表中的索引值，如果找不到抛出异常
# list1.sort()    #  升序排序
# list1.sort(reverse=True)  # 降序排序
# list1.reverse()   # 逆置 反转
# print(list1) 
# a=[]
# a.insert(0,int(5))
# a.insert(1,int(9))
# a.insert(2,int(13))

# b=[5,9,13]
# a.extend(b)  # 把b列表放在a后面
# print(a)

# num=[0,3,3,9,10,3,5]   #  计算列表中有几个数
# b=0
# for a in num:
#     b+=1
#     print(a)
# print(b)

# num=[0,3,3,9,10,3,5]   # 计算列表中的总和
# b=0
# for a in num:
#     b+=a
#     print(a)
# print(b)


# list=["asd",30,4.5]
# a,b,c=list
# print(a,b,c)

# a = [i for i in range(0,101,10)]   # 输出步长为10的所有数据
# print(a)


# 如果刘备在列表里，则删除
# name=["张飞","刘备","关羽","刘邦","刘老二","曹操"]
# # a="刘备" in name
# # print(a)
# # name.remove("刘备")
# # print(name)

# if "刘备" in name:
#     name.remove("刘备")  #  如果刘备在列表里面，则删除
# print(name)

# num=[3,5,67,2,34,12,5,11]
# print(max(num))   # 返回列表中的最大值

# list1=["刘备","关羽","张飞"]
# tuple1=("曹操","周瑜")
# list2=list(tuple1)   # 把元祖转换为列表类型
# list1.append(list2)   # 将列表2加在列表1后面
# print(list1)




# 集合
# a=set()     # 定义一个空集合
# i=0
# while i<5:   # 通过input函数，向集合里输入任意五个整数
#     i+=1
#     b=int(input())
#     a.add(b)
# print(a)
# c=list(a)
# print(min(c))   #  显示集合中的最小值


# a=set()
# i=0
# while i <3:  # 输入三个字符串
#     i+=1
#     b=str(input())
#     a.add(b)
# print(a)
# for s in a:  # 依次从a集合中取值
#     print(s)




#  字典
# dict={"name":"周瑜","age":32,"id":"001"}
# dict["sex"]="男"    # 增加一个键值对
# print(dict)
# dict.pop("id")   # 删除id
# print(dict)
# dict["age"]=26    # 修改age的值为26
# print(dict)

# dict1={"a":23,"b":4,"c":9,"d":3,"e":12}
# for i in dict1: 
#     print("键：{0} , 值：{1}".format(i,dict1[i]))   # 返回字典里的每一个键和值