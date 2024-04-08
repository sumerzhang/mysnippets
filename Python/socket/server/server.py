import socket

socket_server = socket.socket()
socket_server.bind(('localhost', 8888))
socket_server.listen(1)
conn, address = socket_server.accept()
print(f'接收到客户端连接，来自{address}')
while True:
    data = conn.recv(1024).decode("UTF-8")
    if data == 'exit':
        break
    print('接收到发来的消息：', data)
    reply = input('请输入回复的消息：').encode('UTF-8')
    conn.send(reply)

conn.close()
socket_server.close()
