#!/usr/bin/env python
# coding: utf-8

# In[7]:


from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto('Hello!'.encode(),(serverName, serverPort))
answer1 = ''
while(answer1.lower() != "yes" and answer1.lower() != "no"):
    question1, serverAddress = clientSocket.recvfrom(2048)
    print(question1.decode())
    answer1 = input('Response: ')
    clientSocket.sendto(answer1.encode(),(serverName, serverPort))
answer2 = ''
while(answer2.lower() != "yes" and answer2.lower() != "no"):
    question2, serverAddress = clientSocket.recvfrom(2048)
    print(question2.decode())
    answer2 = input('Response: ')
    clientSocket.sendto(answer2.encode(),(serverName, serverPort))
answer3 = ''
while(answer3.lower() != "yes" and answer3.lower() != "no"):
    question3, serverAddress = clientSocket.recvfrom(2048)
    print(question3.decode())
    answer3 = input('Response: ')
    clientSocket.sendto(answer3.encode(),(serverName, serverPort))
result, serverAddress = clientSocket.recvfrom(2048)
print(result.decode())
clientSocket.close()


# In[ ]:




