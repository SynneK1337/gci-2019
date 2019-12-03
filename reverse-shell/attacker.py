import socket

hostname = '192.168.0.80'
port = 2137

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((hostname, port))
s.listen(1)

conn, addr = s.accept()
print(f"New connection from {addr[0]}.")
while 1:
    cmd = input("> ")
    if cmd == "exit":
        break
    conn.send((cmd+'\n').encode('utf-8'))
    output = conn.recv(8192)
    if not output:
        break
    print(output.decode('utf-8'))

conn.close()
print(f"{addr[0]} disconnected.")