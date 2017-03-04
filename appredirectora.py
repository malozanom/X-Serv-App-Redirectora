#!/usr/bin/python3

"""
Miguel Ángel Lozano Montero.
Programa que construye una aplicación web redirectora.
"""

# Después de lanzar la aplicación web, se comprueba que el navegador
# realiza infinitas redirecciones a los recursos aleatorios.

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print((recvSocket.recv(1024)).decode('utf-8'))
        aleatorio = random.randrange(1000000000)
        recvSocket.send(bytes("HTTP/1.1 302 Found\r\n\r\n" +
                              "<html><body><h1>" +
                              "<meta http-equiv='refresh'" +
                              "content='5;url=http://localhost:1234/" +
                              str(aleatorio) + "'/>Redirigiendo en 5s a /" +
                              str(aleatorio) + "</h1></body></html>"
                              "\r\n", "utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
