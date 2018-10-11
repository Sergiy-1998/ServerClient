from socket import *
import time
import datetime
import json
import random

host = 'localhost'
port = 777
addr = (host, port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(1)

def count_id():
    today = datetime.datetime.today()#час
    idi = random.randint(0,100)#ід від 0 до 100
    inf = 'ID', idi, today.strftime("%Y-%m-%d-%H:%M:%S")#вивід
    return (json.dumps(inf))#вивід в форматі

while True:

    print('CONNECTION...')
    conn, addr = tcp_socket.accept()
    print('client addr: ', addr)

    data = conn.recv(1024)
    if not data:
        conn.close()
        break
    else:
        time.sleep(1)
        print(data)
        buf = count_id()
        conn.send(data)
        conn.close()

tcp_socket.close()
