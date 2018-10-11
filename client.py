from socket import *
import sys
import time
import datetime
import json
import random
import threading
class client(threading.Thread):

    def run(self):
        def count_id():
            today = datetime.datetime.today()  # час
            idi = random.randint(0, 100)  # ід від 0 до 100
            inf = 'ID', idi, today.strftime("%Y-%m-%d-%H:%M:%S")  # вивід
            return (json.dumps(inf))  # вивід в форматі

        host = 'localhost'
        port = 777
        addr = (host, port)

        tcp_socket = socket(AF_INET, SOCK_STREAM)
        tcp_socket.connect(addr)

        data = count_id()
        if not data:
            tcp_socket.close()
            sys.exit()
        time.sleep(1)
        data = str.encode(data)
        tcp_socket.send(data)
        data = tcp_socket.recv(1024)
        print(data)
        tcp_socket.close()
one = client()
for i in range(5):
    one.run()
