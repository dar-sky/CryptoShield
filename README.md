# AES-Encryption-Decryption 
Client inputs:	 Message, Secret Key, Public and Private key parameters for Client .
Server Inputs: 	 Public and Private key parameters for Server. 
# Message Flow:
  Client requests for public key of server. Server sends the public key. Client sends Ciphertext, Encrypted secret key, Client Signature, Client public key. 
#  Client side computation:
Create Client signature through RSA algorithm, taking Digest from Hash algorithm and client private key as input.Create Ciphertext through the AES variant, taking Message and Secret key as input.Encrypt Secret key with RSA algorithm, taking Secret key and Server Public key as input.
#  Server side Computation:
   Decrypt Secret key using RSA algorithm . Decrypt ciphertext using AES variant .Create message digest .Verify Client Signature
#
The client then sends ciphertext and key to the server. Server on receiving the encrypted message decrypts the message .
Integrity and key sharing among both the client and server. Implement the RSA algorithm from scratch that will be used for secret key encryption and digital signature. For Message digest creation you may use any existing implementation of hash algorithm compatible with your program. Working of the secure system will be as follows:
![Cryptograpgy](https://user-images.githubusercontent.com/84175560/132932017-a94248b4-eeb0-48cf-8dfa-ac7098e8b608.jpg)
