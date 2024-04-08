import socket
import os 

def run_cmd(socker_client, cmd):  
    pwd = os.getcwd()  
    if cmd.startswith('cd'):  
        try:  
            os.chdir(cmd.split()[1])  
        except FileNotFoundError:  
            os.chdir(pwd)  
            result = '目录不存在'  
            socker_client.send(result.encode('UTF-8'))  
            return  
        result = '切换目录成功'  
        socker_client.send(result.encode('UTF-8'))


socker_client = socket.socket()
socker_client.connect(('localhost', 8888))
print('连接到服务端')
while True:
    send_msg = input('请输入要发送的消息：')
    if send_msg == 'exit':
        break
    socker_client.send(send_msg.encode('UTF-8'))
    recv_data = socker_client.recv(1024)
    print('服务端回复的消息：', recv_data.decode('UTF-8'))
    if recv_data.decode('UTF-8').startswith('cd'):
        run_cmd(socker_client, recv_data.decode('UTF-8'))

socker_client.close()
