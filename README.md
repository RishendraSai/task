# task(key-value-data-store file system With basic operations)

The data store Functionalities :

1.It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
2.A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.
3.If Create is invoked for an existing key, an appropriate error must be returned.
4.A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
5.A Delete operation can be performed by providing the key.
6.Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
7.Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits

#Constrains

1.The file size never exceeds 1GB
2.The code returns following errors  
      *INVALIDKEY ->if KEYLENGTH is greater than 32 or key contains any numeric,special characters etc.,
      *KEY NOT EXIST-> if key does not exist or deleted earlier
      *MEMORY LIMIT EXCEED ->if file memory exceeds 1GB
The file is accessed by multi-threading

