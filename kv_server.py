import socket
import threading
HOST='localhost'
PORT=5678
a = {}
key = ''
value = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind((HOST,PORT))
s.listen(5)
print('Waiting for connection...')
def tcplink(sock, addr):
    global key,value,a
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        c = str(data)
        d = c.strip("b")
        e = d.strip("'")
        f = e.strip("")
        b = f.split(" ")

        key = b[1]
        if b[0] == 'SET':
            value = b[2]
            a[key] = value
        elif b[0] == 'GET':
            if key in a:
                sock.send(a[key].encode())
            else :
                sock.send('\n'.encode('utf-8'))
        else :
            sock.send('请输入正确的命令：SET/GET'.encode())
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
