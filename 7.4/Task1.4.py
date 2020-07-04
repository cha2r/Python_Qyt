#coding = utf-8


#创建一个随机产生IP地址的代码
#导入random模块，随机产生网络IPv4地址。

import random

print ("生成随机IPv4地址:")
print (str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)))
#random.randint(a,b) 生成[a,b]内的随机整数
#需要用 str() 方法将生成的随机整型数字转换为 str 型，才能使用 + 连接
# + 操作符只能用于连接两个整数或者连接两个字符串



# if __name__ == '__main__':
# 	pass