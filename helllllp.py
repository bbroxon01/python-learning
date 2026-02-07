import hashlib

for i in range(10000): 
    data = 'brandon' + str(i)
    data = data.encode()
    res = hashlib.md5(data).hexdigest()
    if res[0] == '2' and res[1] == '0' and res[2] == '2' and res[3] == '6':
        print(data, i, res)
        break
       