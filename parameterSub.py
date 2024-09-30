import sys
import os
import datetime
import scriptCreator


# parameterlist = ["Spin","L1","L2","dL","J1","J2","dJ","D1","D2","dD","initialSampleNumber","finalSampleNumber","sampleDelta","BC","Pdis","bondDim","dx"]

# parameterlist = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
#                  "D":{"D1":None,"D2":None,"dD":None},"seed":{"s1":None,"s2":None,"ds":None},\
#                  "BC":None,"Pdis":None,"bondDim":None,"dx":None,"check_Or_Not":None,"status":None,"Ncore":None,"partition":None}

tasks = ["submit","show","cancel","change","dis","a","b","c","d","e"]
task = ""

while task not in tasks:
    task = input("What is the task? (a)submit, (b)show, (c)cancel Jobs, (d)change (e)distribution: \n")
    if task == "a":
        task = "submit"
    elif task == "b":
        task = "show"
    elif task == "c":
        task = "cancel"
    elif task == "d":
        task = "change"
    elif task == "e":
        task = "dis"    

a = scriptCreator.para(task)
a.keyin()
a.release()
paraSub = a.new_dic
print(a.para)
print(paraSub)
# paraSub = {"Spin : ":None,"L1 : ":None,"L2 : ":None,"dL : ":None,"J1 : ":None,"J2 : ":None,"dJ : ":None\
#     ,"D1 : ":None,"D2 : ":None,"dD : ":None,"initialSampleNumber : ":None,"finalSampleNumber : ":None\
#         ,"sampleDelta : ":None,"BC : ":None,"Pdis : ":None,"bondDim : ":None,"dx : ":None,"check_Or_Not(Y/N) : ":None\
#             ,"(R/P) : ":None,"Ncore : ":None,"Partition1 : ":None,"Partition2 : ":None}




# try:
#     for key, value in paraSub.items():
#         temp = input(key)
#         if temp == "":
#             paraSub[key] = "skip"
#         else:
#             paraSub[key] = temp
# except KeyboardInterrupt:
#     print("shut down")
#     exit()
l = []
for value in paraSub.values():
    l.append(value)
# l = list(str(para.values()))
print(l)
s = " ".join(l)

# tonow = datetime.datetime.now()

today = datetime.datetime.today()
now = datetime.datetime.now()
print(today.date())         # 2021-10-19
print(now.time())         # 14:25:46.962975

for key,value in paraSub.items():
    print(key)
    print(value)
    print("\n")

file = "./subparameter/" + str(today.year) + "/" + str(today.month) + "/" + str(today.day) + "/" 
if os.path.exists(file):
    file = file + str(now.time()) + ".txt"
    fh = open( file , "w" )
    print(file)
    paraStr = [task]
    for key,value in paraSub.items():
        paraStr.append(str(key)+":"+str(value))
    paraStr="\n".join(paraStr)
    fh.write(paraStr)
else:
    os.makedirs(file)
    file = file + str(now.time()) + ".txt"
    fh = open( file , "w" )
    paraStr = []
    for key,value in paraSub.items():
        paraStr.append(str(key)+":"+str(value))
    paraStr="\n".join(paraStr)
    fh.write(paraStr)

if task == "submit" or task == "change":
    command = "nohup python ./average.py " + task + " "
    s = command + s 
    s = s + " >>" 
    file = "./parameterRecord/" + str(today.year) + "/" + str(today.month) + "/" + str(today.day) + "/" 
    if os.path.exists(file):
        print(file)
    else:
        os.makedirs(file)
    s = s + file + str(now.time()) + ".txt&"
    print(s)
    os.system(s)
    # l = [command,task,Spin,L1,L2,dL,J1,J2,dJ,D1,D2,dD,initialSampleNumber,finalSampleNumber,sampleDelta,BC,Pdis,bondDim,dx,check_Or_Not,status,Ncore,Partition,"&"]
else:
    command = "python ./average.py " + task + " "
    s = command + s
    print(s)
    os.system(s)
# l = [command,task,Spin,L1,L2,dL,J1,J2,dJ,D1,D2,dD,initialSampleNumber,finalSampleNumber,sampleDelta,BC,Pdis,bondDim,dx,check_Or_Not,status,Ncore,Partition,"&"]
# s = " ".join(l)
