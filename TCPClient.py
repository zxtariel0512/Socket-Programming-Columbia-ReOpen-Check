#!/usr/bin/env python
# coding: utf-8

# In[14]:


from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
answer1 = ''
while(answer1.lower() != "yes" and answer1.lower() != "no"):
    question1 = clientSocket.recv(1024)
    print(question1.decode())
    answer1 = input('Response: ')
    clientSocket.send(answer1.encode())
answer2 = ''
while(answer2.lower() != "yes" and answer2.lower() != "no"):
    question2 = clientSocket.recv(1024)
    print(question2.decode())
    answer2 = input('Response: ')
    clientSocket.send(answer2.encode())
answer3 = ''
while(answer3.lower() != "yes" and answer3.lower() != "no"):
    question3 = clientSocket.recv(1024)
    print(question3.decode())
    answer3 = input('Response: ')
    clientSocket.send(answer3.encode())
result = clientSocket.recv(1024)
print(result.decode())
clientSocket.close()


# In[ ]:





# In[ ]:




