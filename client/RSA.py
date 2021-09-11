# # Name :: Pradeep
# # Roll    :: 2018180
# ##  Email :: 2018180@iiitdmj.ac.in

def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    # Return the array of bytes
    return cipher


# In[2]:


def decrypt(pk, ciphertext):
    key, n = pk
    plain=[chr(pow(a,key,n)) for a in ciphertext]
    return ''.join(plain)


# In[ ]:




