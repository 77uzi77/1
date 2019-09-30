import socket
HOST='localhost'
PORT=5678
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect((HOST,PORT))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
while(True):
    data = input()
    if not data or data == 'exit':
        break
    key = input()
    if data == 'SET':
        value = input()
        s.send(value.encode('utf-8'))
    s.send(data.encode('utf-8'))
    s.send(key.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
    

s.send(b'exit')
s.close()
