# Serverless Queue on Azure
I wanted to build an application that had a serverless functionality totally on Microsoft Azure. So, the goal here is to use the Azure function for the serverless part and Azure queue to receive messages from our application. The deployment can be done from the Visual Studio Code as well as the Portal itself.

# Architecture:
![architecture](https://user-images.githubusercontent.com/13358738/123502383-a6032200-d66b-11eb-9fcd-ac1a216beb13.png)

# Tools:
1. Azure Account
2. Azure Virtual Machine
3. Azure Queue Service
4. Azure Function
5. Python SDK

# Replication Steps:
1. Infrastructure: I have written all the steps to create the infrastructure on my medium blob.
 
2. Code
```bash
git clone git@github.com:codexponent/serverless-messaging-azure.git
pip install -r requirements.txt
python main.py
```
3. Check the output on port 80 of the hosted instance or localhost.
