from time import perf_counter
from code import code1,code2
import function as f

x = input("请选择爱酱的工作:(1:现场加密.2:加密文件.)\n")
x = int(x)
start = perf_counter()#记录开始的时间
#对用户的输入进行加密
if x == 1:
    size = f.getmessage()
    n = input("请输入加密偏移量：")
    for i in size:
        i = i.upper()
        for ch in i:    
            a = code2[ch]
            if  int(a)+int(n) <= 26:
                b = code1[int(a)+int(n)]
                print(b,end="")
            else:
                b=code1[int(a)+int(n) - 26]
                print(b,end="")    
                
elif x == 2:
    file_a = input("请输入您想加密的文件及其目录：")
    n = input("请输入加密偏移量：")
    file_b = open(file_a,"r") #打开用户输入的文件
    
    txt = file_b.read(2)#将文件通过循环输出
    txt = txt.upper()#将文件以大写形式输出
    while txt != "":
        save = f.remove(txt)
        #解密过程   
        for i in save:
            a = code2[i]
            if  int(a)+int(n) <= 26:
                b = code1[int(a)+int(n)]
                print(b,end="")
            else:
                b=code1[int(a)+int(n) - 26]
                print(b,end="")               
        txt = file_b.read(2)
        txt = txt.upper()
    #解密结束后关闭文件
    file_b.close()
    
else :
    print("您的输入有误")
#计算解密所需时间
print("\n解密完毕，解密所需时间为：{:.5f}s".format(perf_counter()-start))


