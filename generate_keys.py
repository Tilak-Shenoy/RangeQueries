import time
key_length=int(input(" Enter key length\n"))
start_char=input(" start word\n")
end_char=input("end word\n")
alphabets="abcdefghijklmnopqrstuvwxyz"

# def build_key(ikey):
#     if len(ikey) ==key_length:
#         return ikey
#     build_key(ikey+alphabets[0])
temp=[]
range_query=[]
final_keys=[]
start_time=time.time()
for i in range(0,26):
    if    ord(alphabets[i]) < ord(start_char[0]) :
        continue
    if  ord(alphabets[i]) > ord(end_char[0]):
        break
    temp.append(alphabets[i])

for p in range(1,key_length+1):
    range_query=temp
    temp=[]   
    # print(range_query)
    for j in range(len(range_query)):
        for i in range(0,26):
            temp_word=range_query[j]+alphabets[i]
            if temp_word >= start_char[:len(temp_word)] and temp_word <= end_char[:len(temp_word)]:
                temp.append(temp_word)
    
end_time=time.time()
# print("keys ", range_query)
print("No. of keys ", len(range_query))
print("time taken for key generation", end_time -start_time)
    

