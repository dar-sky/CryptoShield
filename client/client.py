# ### Pradeep
# ### 2018180@iiitdmj.ac.in

from AES import *
from hash import *
from key import *
from RSA import *


# In[33]:


plain=input("Enter your Plain_test :: ")
key=input("Enter your Key :: ")
Cipher_Text,Key,plain_text =encryption(plain,key)
print(f"\nCipher_Text :: \n{Cipher_Text}\n")
print(f"Key :: {Key} \n")
print(f"Plain Text :: \n{plain_text}\n\n")


# In[36]:


client_public,client_private=client_key()


# In[37]:


print("Client_public  >> " +client_public)


# In[38]:



print("client_private  >> " + client_private )

# In[39]:


msg_digset=SHA(plain_text)


# In[40]:


client_signature=encrypt(client_private,msg_digset)
c_s=""
for i in client_signature:
    c_s+=str(i)


# In[41]:


def enc_key(server_public_key):
    ppp=encrypt(server_public_key,Key)
    return ppp


# In[42]:


import socket  
import time
def clientSideConnection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_hostname = socket.gethostname()
    local_fqdn = socket.getfqdn()
 
    ip_address = socket.gethostbyname(local_hostname)
    port = 55468
    server_address = (ip_address, port)
    sock.connect(server_address)
 
    print (f"Connecting to {local_hostname} ({local_fqdn}) with {ip_address}")
    print ("\nConnected to server-side. \n")
    data=str("\n\nSend me Public Key ").encode("utf-8")
    sock.sendall(data)
#     time.sleep(2)
    
    q=sock.recv(4096).decode()
    n=sock.recv(4096).decode()
    
    server_public_key=(int(q),int(n))
    
    encrypted_secret_key=enc_key(server_public_key)
    esk=str(encrypted_secret_key).encode()
    print(esk)
    print(type(esk[0]))
    
    sock.send(esk)
    print("encrypted_secret_key send successfully \n\n ")
    
    esk=str(Cipher_Text).encode()
    sock.send(esk)
    print(Cipher_Text)
    print("\n\nCipher_text send successfully \n\n ")
    
    
    esk=str(client_public).encode()
    sock.send(esk)
    print(client_public)
    print("\n\nclient_public send successfully \n\n ")

#     sock.send(str("as").encode())
    i=0
    while i < len(client_signature):
        sock.send(str(client_signature[i]).encode())
        time.sleep(1)
        i+=1
    print(c_s)
    print("\n\n  client_signature send successfully \n\n ")

    

    
    
    sock.close()
 
clientSideConnection()


# In[ ]:




