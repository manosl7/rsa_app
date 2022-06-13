# rsa_app

rsa_app is a project written in python tha creates an RSA key and save the private one into a pem file. Later on it changes two consecutive random characters from pem file of the private key. The second script tries to revise the original private key of the RSA algorithm.

# Prerequisites

To run the scripts you have to install the crypto, gmpy, random and primefac packages on Python. To import these packages open a terminal window and ran the following commands :

$ pip install crypto

$ pip install gmpy

$ pip install primefac

# How to use 

Download the scripts and open a terminal where these two are located and then run the command "python rsa.py". After run the script you can see the private and public keys of the algorithm and the changes of two consecutive characters from private key. Also, it appears the changed private key. Now open a new window in the same folder you've download the scripts and run the command "find_rsa_private_key.py" to find the original pem file of private key.
