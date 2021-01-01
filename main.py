import function as s 

#creation
s.create("Rishi",26) #creation of key with no time
s.create("qwerty",1)
s.create("Sai",30,3600) #creation of key with time in secs

#reading
s.read("Rishi") #returns key in JSON format
s.read("sai") #returns key in JSON format if the time not completed else it returns an message
s.create("Rishi",50) #returns an error message since the key_name already exists

#deleting 
s.delete("Rishi") #it deletes the key with memory

#By using multiple threads
t1=Thread(target=(create or read or delete),args=(key,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t2.start()
t2.sleep()
# ............. to tn 
