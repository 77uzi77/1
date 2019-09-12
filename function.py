#定义函数排除特殊字符
def remove(txt):
    for ch in '1234567890!@#$%^&*()_+ {}|:"[]<>?,./\n￥`…':  
        txt = txt.replace(ch,"")#
    return txt
#定义函数收集用户不定长度的输入    
def getmessage():
    message = []
    imessage = input("请输入信息(回车结束)：")
    remessage = remove(imessage)
    while remessage != "":
        message.append(remessage)
        remessage = input("请输入信息(回车结束)：")
        remessage = remove(remessage)
    return message
#检查模块
def check():
	x = getmessage()
	print(x)
if __name__ == "__main__":
	check()
