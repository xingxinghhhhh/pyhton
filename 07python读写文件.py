# abc=open(r"C:\Users\Administrator\Desktop\python1\aaa.txt","r")
# abc.close()


# a=r"C:\Users\Administrator\Desktop\python1\aaa1.txt"  # 创建文件
# aa=open(a,"a+",encoding="utf-8")  
# str1="hello world\n"   
# aa.write(str1)    # 写入内容str
# str2="hello python\n"
# aa.write(str2)   # 写入内容str2
# aa.seek(0)   #  查看内容
# print(aa.read())   
# aa.close()


# a=open(r"C:\Users\Administrator\Desktop\python1\aaa.txt","a+")
# str1="你好啊\n"
# a.write(str1)
# str2="嘻嘻嘻\n"
# a.write(str2)
# str3="helloxixiix\n"
# a.write(str3)
# a.seek(0)
# print(a.read())


# a=open(r"C:\Users\Administrator\Desktop\python1\aaa.txt","a+")
# str1="\n你好啊\n嘻嘻嘻\nhelloxixiix\n"
# a.write(str1)
# print(a.tell())
# a.seek(63)
# print(a.read())
# a.close()


# a=open(r"C:\Users\Administrator\Desktop\python1\aaa.txt","r")
# print(a.readline())
# a.close()


# a=r"C:\Users\Administrator\Desktop\python1\a.txt"
# hh=open(a,"a+",encoding="utf-8")
# # str="12345\nabcde\n"
# # hh.write(str)
# print(hh.tell())
# hh.seek(0)
# print(hh.read())
# hh.close()


# import json
# f = open(r'C:\Users\Administrator\Desktop\python1\nnnn.json', "r", encoding='gbk')
# data = json.load(f)
# # 返回的 data 数据类型为字典或列表
# print(data)
# f.close()


# import json
# data = {'name': 'tom', 'age': 20, 'country': '中国'}
# f = open(r'C:\Users\Administrator\Desktop\python1\nnnn.json', 'w', encoding='gbk')
# json.dump(data, f, ensure_ascii=False)
# # ensure_ascii=False 代表中文不转义
# f.close()


# import json
# # aa = open(r'C:\Users\Administrator\Desktop\python1\test1.json','w',encoding='gbk')
# # date= {"name":"诸葛亮","sex":"男","age":"24"}
# # json.dump(date,aa,ensure_ascii=False)
# # aa.close()


# s= open(r'C:\Users\Administrator\Desktop\python1\test1.json','r',encoding='gbk')
# c=json.load(s)
# c["age"]=30
# print(c)
# s.close()