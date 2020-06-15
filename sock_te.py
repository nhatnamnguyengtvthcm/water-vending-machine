import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(10)
client.connect(('192.168.30.43', 8881))
client.send("1213123".encode())
from_server = client.recv(4096)
print(from_server)
client.close()
