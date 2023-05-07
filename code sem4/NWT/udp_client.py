import socket
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address=('127.0.0.1',12345)
message=input("Enter the message: ")
udp_socket.sendto(message,server_address)

while True:
    print("Waiting for server...")
    data,addr=udp_socket.recvfrom(1024)
    print("Received Messages: ",data.decode()," from ",addr)
    break
udp_socket.close()
