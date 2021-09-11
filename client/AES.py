# #### Name :: Pradeep 
# #### Roll    :: 2018180
# #### Email :: 2018180@iiitdmj.ac.in

# In[1]:


import string 
import os


# In[2]:


def text_to_matrix(temp_string):
    ans=[[],[],[],[]]
    for i in range(4):
        for j in range(4):
            ans[j].append(hex(ord(temp_string[4*i+j])))
    return ans


# In[3]:


def matrix_to_text(state):
    for i in range(4):
        for j in range(4):
            print(chr(int(state[i][j],16)),end=" ")
        print()
    print("\n\nText :: ",end=" ")
    for i in range(4):
        for j in range(4):
            print(chr(int(state[j][i],16)),end="")


# In[4]:


s_box = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
]


# In[5]:


def sub_byte(p):
    for i in range(4):
        for j in range(4):
            jj=p[i][j][-1]
            if len(p[i][j])==3:
                ii='0'
            else:
                ii=p[i][j][-2]
            p[i][j]=hex(s_box[string.hexdigits.index(ii)][string.hexdigits.index(jj)])


# In[6]:


def shift_row(s):   # shift rows 
    # row 1  > 0 element to left
    # row 2  > 1 element to left
    # row 3  > 2 element to left
    # row 4  > 3 element to left
    s[1][0], s[1][1], s[1][2], s[1][3] = s[1][1], s[1][2], s[1][3], s[1][0]
    s[2][0], s[2][1], s[2][2], s[2][3] = s[2][2], s[2][3], s[2][0], s[2][1]
    s[3][0], s[3][1], s[3][2], s[3][3] = s[3][3], s[3][0], s[3][1], s[3][2] 


# In[7]:


def multiply_ploy(t1,t2):
    t1=bin(int(t1,16))[2:]
    t2=bin(int("0x"+t2,16))[-1:1:-1]
    ttt="0"
    for ii in range(len(t2)):
        if t2[ii]=="1":
            ttt=bin(int("0b"+ttt,2)^int("0b"+t1+"0"*ii,2))[2:]
    while len(ttt) > 8:
        ttt=bin(int("0b"+ttt,2)^int("0b"+"100011011"+"0"*(len(ttt)-9),2))[2:]
    return int("0b"+ttt,2)


# In[8]:


def mix_column(m):    
    for i in range(4):
        x,y,z,w=m[0][i],m[1][i],m[2][i],m[3][i]
        m[0][i]=hex(multiply_ploy(x,"02")^multiply_ploy(y,"03")^multiply_ploy(z,"01")^multiply_ploy(w,"01"))
        m[1][i]=hex(multiply_ploy(x,"01")^multiply_ploy(y,"02")^multiply_ploy(z,"03")^multiply_ploy(w,"01"))
        m[2][i]=hex(multiply_ploy(x,"01")^multiply_ploy(y,"01")^multiply_ploy(z,"02")^multiply_ploy(w,"03"))
        m[3][i]=hex(multiply_ploy(x,"03")^multiply_ploy(y,"01")^multiply_ploy(z,"01")^multiply_ploy(w,"02"))


# In[9]:


Rcon = [ "01", "02", "04", "08", "10", "20", "40","80", "1b", "36"]


# In[10]:


def key_expansion(state,pos):
    temp=[[],[],[],[]]
    t_matrix=[]
    for i in range(4):
        t_matrix.append(state[i][3])
    temp_var=t_matrix[0]
    del t_matrix[0]
    t_matrix.append(temp_var)

    for ii in range(4):
        jj=t_matrix[ii][-1]
        if len(t_matrix[ii])==3:
            iii='0'
        else:
            iii=t_matrix[ii][-2]
        t_matrix[ii]=hex(s_box[string.hexdigits.index(iii)][string.hexdigits.index(jj)])
            
            
    for ii in range(4):
        for j in range(4):
            xx=hex(int(state[j][ii],16)^int(t_matrix[j],16))
            temp[j].append(xx)
            t_matrix[j]=xx
    for ii in range(4):
        temp[0][ii]=hex(int(temp[0][ii],16)^int("0x"+Rcon[pos],16))
    
    return temp


# In[11]:


def round_value(plain_state,key_state):
    output=[[],[],[],[]]
    for i in range(4):
        for j in range(4):
            output[i].append(hex(int(plain_state[i][j],16)^int(key_state[i][j],16)))
    return output


# In[12]:


def new_r(m,k,n):
    sub_byte(m)
    shift_row(m)
    mix_column(m)
    m=round_value(m,k[n])
#     matrix_to_text(m)
    if n==8:
        return m
    else:
        return new_r(m,k,n+1)


# In[13]:


def change_to_string(chiper_text):
    cipher=""
    for i in range(4):
        for j in range(4):
            ii=chiper_text[i][j][-1]
            if len(chiper_text[i][j])==3:
                jj="0"
            else:
                jj=chiper_text[i][j][-2]
            cipher+=jj+ii
    return cipher


# In[14]:


def aes_enc(plain_text,key_text):
    plain_state=text_to_matrix(plain_text)
    key_state=text_to_matrix(key_text)
    pre_round=round_value(plain_state,key_state)
    m_k=[]
    for i in range(10):
        otp=key_expansion(key_state,i)
#         matrix_to_text(otp)
        m_k.append(otp)
        key_state=otp.copy()
        
    till_round_9=new_r(pre_round,m_k,0)
    sub_byte(till_round_9)
    shift_row(till_round_9)
    chiper_text=round_value(till_round_9,m_k[9])
    cipher_text=change_to_string(chiper_text)
    plain_text=change_to_string(plain_state)
    return cipher_text


# In[15]:


def encryption(plaintext,keytext):
    temp_text=""
    if len(keytext) <16 :
        keytext+="#"*(16-len(keytext))
    if len(plaintext)%16 !=0 :
        plaintext+="#"*(16-len(plaintext)%16)
        temp_text+=plaintext
    else:
        temp_text+=plaintext
    keytext=keytext[:16]
    iii=0
    result=""
    while len(plaintext[iii:])>16:
        text=plaintext[iii:iii+16]
        result+=aes_enc(text,keytext)
        iii+=16
    if len(plaintext[iii:])<=16:
        text=plaintext[iii:]
        text+=" "*(16-len(text))
        result+=aes_enc(text,keytext)
    return result,change_to_string(text_to_matrix(keytext)),temp_text


# In[ ]:




