#!/usr/bin/env python
# coding: utf-8

# In[7]:


from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
question1 = 'Have you experienced any COVID-19 symptoms in the past 14 days?'
question2 = 'Have you been in close contact with anyone who has tested positive for COVID-19 in the past 14 days?'
question3 = 'Have you tested positive for COVID-19 in the past 14 days?'
while True:
    greeting, clientAddress = serverSocket.recvfrom(2048)
    if greeting.decode() == 'Hello!':
        answer1 = ''
        while(answer1.lower() != 'yes' and answer1.lower() != 'no'):
            serverSocket.sendto(question1.encode(), clientAddress)
            answer1, clientAddress = serverSocket.recvfrom(2048)
            answer1 = answer1.decode()
        answer2 = ''
        while(answer2.lower() != 'yes' and answer2.lower() != 'no'):
            serverSocket.sendto(question2.encode(), clientAddress)
            answer2, clientAddress = serverSocket.recvfrom(2048)
            answer2 = answer2.decode()
        answer3 = ''
        while(answer3.lower() != 'yes' and answer3.lower() != 'no'):
            serverSocket.sendto(question3.encode(), clientAddress)
            answer3, clientAddress = serverSocket.recvfrom(2048)
            answer3 = answer3.decode()
        if(answer1.lower() == 'no' and answer2.lower() == 'no' and answer3.lower() == 'no'):
            serverSocket.sendto('Green Pass!'.encode(), clientAddress)
        else:
            serverSocket.sendto('Red Pass!'.encode(), clientAddress)


# In[ ]:




