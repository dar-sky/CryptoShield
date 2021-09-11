# # Name :: Pradeep
# # Roll    :: 2018180
# ##  Email :: 2018180@iiitdmj.ac.in


from Inverse_AES import *
from hash import *
from key import *
from RSA import *


# In[2]:


server_public,server_private=client_key()


# In[3]:


server_public


# In[4]:


server_private


# In[5]:


def resolve(cipher_text,encrypted_secret_key,client_public_key,client_signature):
    secret_key=decrypt(server_private,encrypted_secret_key)
    plain_text=decryption(cipher_text,secret_key)
    server_digset=SHA(plain_text)
    ccs=[]
    for i in client_signature:
        ccs.append(int(i))
    msg_digset=decrypt(client_public_key,ccs)
    
    verify=False
    if msg_digset==server_digset:
        verify=True
    print(f"msg_digset :: {msg_digset}")
    return plain_text,verify


# In[6]:


import socket
import time
import sys
import pickle
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
local_fqdn = socket.getfqdn()
 
ip_address = socket.gethostbyname(local_hostname)
port = 55468
 
server_address = (ip_address, port)
 
print (f"Working on {local_hostname} ({local_fqdn}) with {ip_address}")
time.sleep(1)
print ("Starting server-side connection: ")
print (f"\tIP Address {ip_address} ")
print (f"\tPort: {port} ")
time.sleep(1)
 
sock.bind(server_address)
sock.listen(1)
timeout = 0


# In[ ]:


def acceptConnection():
    while True:
        print("Waiting for a connection from client-side.")
        
        connection, client_address = sock.accept()
 
        try:
            print("Received connection from client. from :: " ,end=" ")
            print ('Connection from', client_address)
 
            while True:
                data = connection.recv(4096).decode()
                if data:
                    time.sleep(3)
                    print (f"Received data: {data} ")
                    print(f" Responce to the Client {client_address }" )
                    responce=str(f"{server_public[0]}").encode("utf-8")
                    connection.send(responce)
                    responce=str(f"{server_public[1]}").encode("utf-8")
                    connection.send(responce)
                    print(f"Server_Public_key \n{server_public[0]} \n\n{server_public[1]} \n\n")
                    print("Data Send Successfully !\n\n")
                    
                    
                    data = connection.recv(4096).decode("utf-8")
                    encrypted_secret_key=eval(data)
                    print("encrypted_secret_key :: \n")
                    print(encrypted_secret_key)
                    
                    print(f"\ntype of encrypted_secret_key:: {type(encrypted_secret_key[0])}")
                    
                    
                    Cipher_Text = connection.recv(4096).decode("utf-8")
                    print("\n\n")
                    print(Cipher_Text)
                    print(f"\ntype of Cipher_Text:: {type(Cipher_Text)}")
                    print("\nCipher_Text Received seccessfully \n\n")
                    
                    
                    client_public_key=connection.recv(4096).decode("utf-8")
                    print("\n\n")
                    client_public_key=eval(client_public_key)
                    print(client_public_key)
                    print(f"\ntype of client_public_key:: {type(client_public_key[0])}")
                    print("\nclient_public_key Received seccessfully \n\n")
                    
                    
                    client_signature=[]
                    while True:
                        d=connection.recv(4096).decode("utf-8")
                        print(d)
#                         d=int(d)
#                         print(type(d))

                        if d:
                            client_signature.append(d)
                        else:
                            break
       
                    print(f"\ntype of client_signature:: {type(client_signature)}")
                    print(client_signature)
                    print("\nclient_signature Received seccessfully \n\n")
                
                
                
                
                
                
                    plain_text,verify=resolve(Cipher_Text,encrypted_secret_key,client_public_key,client_signature)
                    
                    
                    
                    print(f"\nPlainText :: {plain_text}\nVerify_status :: {verify}")
                
                
                
                
                


                

                    
                else:
                    print ("\nThere is no more data to receive.")
                    break
 
        finally:
            connection.close()
            print("nConnection closed.")
            exit()
 
acceptConnection()


# In[ ]:




