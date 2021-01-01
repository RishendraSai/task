import time
import threading
from threading import *

dic = {}  # 'dic' dictionary in which we store data



# FOR Craetion time_out is optional

def create(key, value, timeout=0):
    if key in dic:
        print("Key already exists")
    else:
        if key.isalpha():
            length=len(dic)
            if length < (1024 * 1024 * 1024) and value <= (16 * 1024 * 1024):
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time() + timeout]
                if len(key) <= 32:  #input key capped at 32chars
                    dic[key] = l
                    print("SUCCESSFULLY CREATED")
            else:
                print("Memory limit exceeded")  #if memory is more than 1GB
        else:
            print("Invalid KEY_NAME no special characters or numbers are allowed")


# for read operation

def read(key):
    if key not in dic:
        print("key does not exist.Enter a valid key")
    else:
        b = dic[key]
        if b[1] != 0:
            if time.time() < b[1]:  #Checking for time limitwith present time
                i = str(key) + ":" + str(b[0])
                print(i)
                return
            else:
                print("time not complted", key, "has expired")
        else:
            i = str(key) + ":" + str(b[0])
            print(i)
            return


# for delete operation

def delete(key):
    if key not in dic:
        print("Key not exist.Enter a valid key to Delete")
    else:
        b = dic[key]
        if b[1] != 0:
            if time.time() < b[1]: ##Checking for time limitwith present time
                del dic[key]
                print("key is successfully deleted")
            else:
                print("time not completed", key, "has expired")
        else:
            del dic[key]
            print("key is successfully deleted")
