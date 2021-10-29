#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
question1 = 'Have you experienced any COVID-19 symptoms in the past 14 days?'
question2 = 'Have you been in close contact with anyone who has tested positive for COVID-19 in the past 14 days?'
question3 = 'Have you tested positive for COVID-19 in the past 14 days?'
while True:
    connectionSocket, addr = serverSocket.accept()
    answer1 = ''
    while(answer1.lower() != 'yes' and answer1.lower() != 'no'):
        connectionSocket.send(question1.encode())
        answer1 = connectionSocket.recv(1024).decode()
    answer2 = ''
    while(answer2.lower() != 'yes' and answer2.lower() != 'no'):
        connectionSocket.send(question2.encode())
        answer2 = connectionSocket.recv(1024).decode()
    answer3 = ''
    while(answer3.lower() != 'yes' and answer3.lower() != 'no'):
        connectionSocket.send(question3.encode())
        answer3 = connectionSocket.recv(1024).decode()
    if(answer1.lower() == 'no' and answer2.lower() == 'no' and answer3.lower() == 'no'):
        connectionSocket.send('Green Pass!'.encode())
    else:
        connectionSocket.send('Red Pass!'.encode())
    connectionSocket.close()


# In[ ]:




