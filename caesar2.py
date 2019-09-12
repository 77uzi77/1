from time import perf_counter

print("执行开始".center(100,"-"))
x = input("请输入您的选择：\n1.加密文字\n2.加密文件\n3.解密文字\n4.解密文件\n")
start = perf_counter()#记录开始的时间
x = int(x)
i = 0
#加密文字
if x==1 :
    key1 = input("请输入想加密的文字:")
    n = input("请输入加密偏移量：")
    list1 = list(key1)
    re_list1 = list1
    for i in range(len(list1)):
        if ord(list1[i]) + int(n) <= 126:
            re_list1[i] = chr(ord(list1[i]) + int(n))
        else:
            re_list1[i] = chr(ord(list1[i]) +int(n) - 126)
    for ch in range(len(re_list1)):
        print("{}".format(re_list1[ch]),end="")
#加密文件
elif x==2 :
    key2 = input("请输入想要加密的文件及其目录：")
    n = input("请输入加密偏移量：")
    file1 = open(key2,"r")
    file2 = file1.readline(1)
    re_file2 = []
    while file2 != "":
        if ord(file2[i]) + int(n) <= 126:
            re_file2.append(chr(ord(file2[i]) + int(n)))
        else:
            re_file2.append(chr(ord(file2[i]) +int(n) - 126))
        file2 =file1.readline(1)
    file1.close()
    for ch in range(len(re_file2)):
        print("{}".format(re_file2[ch]),end="")
#解密文字
elif x==3:
    key3 = input("请输入想解密的文字：")
    n = input("请输入解密偏移量：")
    list3 = list(key3)
    re_list3 = list3
    for i in range(len(list3)):
        if ord(list3[i]) + int(n) <= 126:
            re_list3[i] = chr(ord(list3[i]) - int(n))
        else:
            re_list3[i] = chr(ord(list3[i]) +int(n) - 126)
    for ch in range(len(re_list3)):
        print("{}".format(re_list3[ch]),end="")
#解密文件
elif x==4:
    key4 = input("请输入想要解密的文件及其目录：")
    n = input("请输入加密偏移量：")
    file3 = open(key4,"r")
    file4 = file3.readline(1)
    re_file4 = []
    while file4 != "":
        if ord(file4[i]) - int(n) <= 126:
            re_file4.append(chr(ord(file4[i]) - int(n)))
        else:
            re_file4.append(chr(ord(file4[i]) - int(n) - 126))
        file4 =file3.readline(1)
    file3.close()
    for ch in range(len(re_file4)):
        print("{}".format(re_file4[ch]),end="")
    case = input("您想将所解的密码保存起来吗？默认不保存(Y/N):")
    if case == 'Y' or 'y':
        save1 = input("请输入想保存的文件：")
        save2 = open(save1,"a",encoding='utf-8')
        for ch in range(len(re_file4)):
            save2.write(re_file4[ch])
        save2.close()
        print("写入完毕...")    
else :
    print("输入错误！")
#计算解密所需时间
print("\n加/解密所需时间为：{:.5f}s".format(perf_counter()-start))
print("\n"+"执行结束".center(100,'-'))
