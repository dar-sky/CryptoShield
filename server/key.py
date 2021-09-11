

# # Name :: Pradeep
# # Roll    :: 2018180
# ##  Email :: 2018180@iiitdmj.ac.in

# In[1]:


import random
import os
import copy


# In[2]:


def is_prime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1


# In[3]:


def next_prime(num):
    if (not num & 1) and (num != 2):
        num += 1
    if is_prime(num):
        num += 2
    while True:
        if is_prime(num):
            break
        num += 2
    return num


# In[4]:


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# In[5]:



'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''


# In[6]:


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


# In[7]:


def generate_keypair(p, q):
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime 
    g = gcd(e, phi)
  
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


# In[8]:


def client_key():
    a=random.randrange(2, 10)
    b=random.randrange(2,50)
    p=a**b
    prime1=next_prime(p)
    a=random.randrange(2, 10)
    b=random.randrange(2,50)
    p=a**b
    prime2=next_prime(p)
    if prime1==prime2:
        client_key()
    public, private = generate_keypair(prime1,prime2)
    return public, private

