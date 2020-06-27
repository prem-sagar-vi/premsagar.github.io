import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('youtube.com',80))
cmd='GET https://www.youtube.com/watch'.encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()
    
