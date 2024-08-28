import sys
import os
import datetime
import scriptCreator


# parameterlist = ["Spin","L1","L2","dL","J1","J2","dJ","D1","D2","dD","initialSampleNumber","finalSampleNumber","sampleDelta","BC","Pdis","bondDim","dx"]

# parameterlist = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
#                  "D":{"D1":None,"D2":None,"dD":None},"seed":{"s1":None,"s2":None,"ds":None},\
#                  "BC":None,"Pdis":None,"bondDim":None,"dx":None,"check_Or_Not":None,"status":None,"Ncore":None,"partition":None}

tasks = ["submut","show","cancel","a","b","c"]
task = ""

while task not in tasks:
    task = input("What is the task? (a)submit, (b)show, (c)cancel Jobs: : \n")
    
print(task)

para = {"Spin : ":None,"L1 : ":None,"L2 : ":None,"dL : ":None,"J1 : ":None,"J2 : ":None,"dJ : ":None\
    ,"D1 : ":None,"D2 : ":None,"dD : ":None,"initialSampleNumber : ":None,"finalSampleNumber : ":None\
        ,"sampleDelta : ":None,"BC : ":None,"Pdis : ":None,"bondDim : ":None,"dx : ":None,"check_Or_Not(Y/N) : ":None\
            ,"(R/P) : ":None,"Ncore : ":None,"Partition : ":None}


try:
    for key in para.keys():
        temp = input(key)
        if(temp == ""):
            para[key] = "skip"
        else:
            para[key] = temp
except KeyboardInterrupt:
    print("shut down")
    exit()



# try:
#     Spin=input("Spin : ")

#     L1=input("L1 : ")
#     L2=input("L2 : ")
#     dL=input("dL : ")    

#     J1=input("J1 : ")
#     J2=input("J2 : ")
#     dJ=input("dJ : ")

#     D1=input("D1 : ")
#     D2=input("D2 : ")
#     dD=input("dD : ")

#     initialSampleNumber=input("initialSampleNumber : ")
#     finalSampleNumber=input("finalSampleNumber : ")
#     sampleDelta=input("sampleDelta : ")
#     BC = input("BC : ")
#     Pdis = input("Pdis : ")
#     bondDim = input("bondDim : ")
#     dx = input("dx : ")
#     check_Or_Not=input("check_Or_Not(Y/N) : ")
#     status=input("(R/P) : ")
#     Ncore=input("Ncore : ")
#     Partition=input("Partition : ")
# except KeyboardInterrupt:
#     print("shut down")
#     exit()

l = list(para.values())
s = " ".join(l)

# tonow = datetime.datetime.now()

today = datetime.datetime.today()
now = datetime.datetime.now()
print(today.date())         # 2021-10-19
print(now.time())         # 14:25:46.962975

time = 

for key,value in para.items():
    print(key)
    print(value)
    print("\n\n")

if task == "submit" or task == "a":
    command = "nohup python ./average.py " + task + " "
    s = command + s 
    s = s + ">>./parameterRecord/" + str(today.year) + "/" + str(today.month) + "/" + str(today.day) + "/" + str(now.time()) + "/" + now.now()
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
