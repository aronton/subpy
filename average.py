import sys
import os
import datetime
import scriptCreator

def submut(parameterlist, tSDRG_path):

    p = parameterlist
    
    Ncore = parameterlist["Ncore"]
    partition = parameterlist["partition"]

    L=scriptCreator.paraList("L",parameterlist["L"])
    L_num = L.num_list
    L_p_num = L.p_num_list
    L_str = L.str_list
    L_p_str = L.p_str_list
    L_s100 = L.s100_list
    L_p_s100 = L.p_s100_list
    print("L_num:",L_num)
    print("L_p_num:",L_p_num)
    print("L_str:",L_str)
    print("L_p_str:",L_p_str)
    print("L_s100:",L_s100)
    print("L_p_s100:",L_p_s100)


    S=scriptCreator.Spara("Seed",parameterlist["seed"])
    S_num = S.toS()
    S_str = S.toStr()
    s1 = parameterlist["seed"]["s1"]
    s2 = parameterlist["seed"]["s2"]

    J=scriptCreator.paraList("Jdis",parameterlist["J"])
    J_num = J.num_list
    J_p_num = J.p_num_list
    J_str = J.str_list
    J_p_str = J.p_str_list
    J_s100 = J.s100_list
    J_p_s100 = J.p_s100_list
    
    print("J_num",J_num)
    print("J_p_num",J_p_num)
    print("J_str:",J_str)
    print("J_p_str:",J_p_str)
    print("J_s100:",J_s100)
    print("J_p_s100:",J_p_s100)
    
    D=scriptCreator.paraList("Dim",parameterlist["D"])
    D_num = D.num_list
    D_p_num = D.p_num_list
    D_str = D.str_list
    D_p_str = D.p_str_list
    D_s100 = D.s100_list
    D_p_s100 = D.p_s100_list
    
    print("D_num:",D_num)
    print("D_p_num:",D_p_num)
    print("D_str:",D_str)
    print("D_p_str:",D_p_str)
    print("D_s100:",D_s100)
    print("D_p_s100:",D_p_s100)

    Spin=parameterlist["Spin"]
    Pdis=parameterlist["Pdis"]
    dx=parameterlist["dx"]
    bondDim=parameterlist["bondDim"]
    BC=parameterlist["BC"]
    check_Or_Not=parameterlist["check_Or_Not"]

    tSDRG_record = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/submit_record"
    record_dir = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/jobRecord" 
    script_dir = record_dir + "/script" + "/" + str(BC) + "/B" + str(bondDim)
    output_dir = record_dir + "/slurmOutput" + "/" + str(BC) + "/B" + str(bondDim)

    tSDRG_fileName="/tSDRG_Spin=" + str(Spin) + ";BC=" + str(BC) + ";P="+ str(Pdis) + ";B=" + str(bondDim) \
        + ";L=" + str(L_p_num[0]) + "_" + str(L_p_num[1]) + "(" + str(L_p_num[2])\
        + ");J=" + str(J_num[0]) + "_" + str(J_p_num[1]) +"(" + str(round(J_p_num[2],2)) \
        + ");D=" + str(D_num[0]) + "_" + str(D_p_num[1]) + "(" + str(round(D_p_num[2],2)) +");"\
        + "seed1=" + str(s1) + "_seed2=" + str(s2) + ";Partition=" + str(partition) + ";Number_of_core=" + str(Ncore)

    nt=datetime.datetime.now()
    now_year = str(nt.year)
    now_date = str(nt.year) + "_" + str(nt.month) + "_" + str(nt.day)
    now_time = "H" + str(nt.hour) + "_M" + str(nt.minute) + "_S" + str(nt.second)
    
    tSDRG_fileDir = tSDRG_record + "/" + now_year + "/" + now_date

    if os.path.exists(tSDRG_fileDir):
        print(tSDRG_fileDir)
    else:
        os.makedirs(tSDRG_fileDir)

    tSDRG_filePath = tSDRG_fileDir + tSDRG_fileName + "_" + now_time

    with open(tSDRG_filePath, "wt") as file:
        file.write(tSDRG_fileName)

    with open("run.sh", "r") as file:
        template = file.readlines()

    print("tSDRG_filePath : ",tSDRG_filePath)
    
    os.system( "cd " + tSDRG_path + "/tSDRG/Main_" + Spin)
    
    for l_i,l in enumerate(L_str):
        for j_i,j in enumerate(J_str):
            for d_i,d in enumerate(D_str):
                for s_i in range(len(S_num)):
                    s = S_num[s_i]
                    script_path = script_dir + "/" + l + "/" + j + "/" + d  
                    output_path = output_dir + "/" + l + "/" + j + "/" + d
                    if os.path.exists(script_path):
                        pass
                        # print("exist : ", script_path)
                    else:
                        # print("not exist : ", script_path)
                        os.makedirs(script_path)
                        
                    if os.path.exists(output_path):
                        pass
                        # print("exist : ", output_path)
                    else:
                        # print("not exist : ", output_path)
                        os.makedirs(output_path)
                        
                    jobName = "Spin" + str(Spin) + "_" + l + "_" + j + "_" + d + "_" + "P" + str(Pdis) \
                                + "_" + "BC=" + str(BC) + "_B" + str(bondDim) + "_Ncore=" + Ncore + "_seed1=" \
                                    + str(s[0]) + "_seed2=" + str(s[-1]) + ""
                    script_name = jobName + "_" + now_date + "_" + now_time
                    script_path = script_path + "/" + script_name + "_random.sh"
                    output_path = output_path + "/" + script_name + "_random.out"
                    context = template.copy()
                    with open(script_path, "w") as file:
                        context[1] = context[1].replace("replace1", "scopion" + str(partition))
                        context[3] = context[3].replace("replace2", jobName)
                        context[4] = context[4].replace("replace3", Ncore)
                        context[5] = context[5].replace("replace4", output_path)
                        file.writelines(context)
                    
                    submit_cmd_list = ["nohup sbatch ",script_path, str(Spin),str(L_num[l_i]),str(J_num[j_i]),str(D_num[d_i])\
                    ,str(BC),str(bondDim),str(Pdis),str(s[0]),str(s[-1]),check_Or_Not,str(Ncore),tSDRG_path,output_path, ">/dev/null 2>& 1&"]

                    submit_cmd = " ".join(submit_cmd_list)
                    os.system(submit_cmd)

def find(parameterlist):
    print("find")
    p = parameterlist
    # flag = input("Job_state R/P")
    if p["status"] == "R":
        Job_state = "RUNNING"
    elif p["status"] == "P":
        Job_state = "PENDING"
    elif p["status"] == "" :
        Job_state = ""

    Ncore = p["Ncore"]
    partition = p["partition"]      
      
    if partition != "":
        job_list = os.popen("squeue -u aronton " + "-p scopion" + str(partition) + " -o \"%%.12i %%.12P %%.90j %%.8T\"")
    else:
        job_list = os.popen("squeue -u aronton " + " -o \"%%.12i %%.12P %%.90j %%.8T\"")
    
    job_list = list(job_list)
    
    del job_list[0]
    for i in range(len(job_list)):
        job_list[i] = job_list[i].split()    


    if (p["L"]["L1"] != "") and (p["L"]["L2"] != "") and (p["L"]["dL"] != ""): 
        L=scriptCreator.paraList("L",p["L"])
        L_num = L.num_list
        L_p_num = L.p_num_list
        L_str = L.str_list
        L_p_str = L.p_str_list
        L_s100 = L.s100_list
        L_p_s100 = L.p_s100_list
        
        temp = []
        for l in L_str:
            for e in job_list:
                if l in e[2]:
                    temp.append(e)
        job_list = temp

            
    if (p["J"]["J1"] != "") and (p["J"]["J2"] != "") and (p["J"]["dJ"] != ""): 
        J=scriptCreator.paraList("Jdis",p["J"])
        J_num = J.num_list
        J_p_num = J.p_num_list
        J_str = J.str_list
        J_p_str = J.p_str_list
        J_s100 = J.s100_list
        J_p_s100 = J.p_s100_list

        temp = []
        for j in J_str:
            for e in job_list:
                if j in e[2]:
                    temp.append(e)
        job_list = temp




    if (p["D"]["D1"] != "") and (p["D"]["D2"] != "") and (p["D"]["dD"] != ""): 
        D=scriptCreator.paraList("Dim",p["D"])
        D_num = D.num_list
        D_p_num = D.p_num_list
        D_str = D.str_list
        D_p_str = D.p_str_list
        D_s100 = D.s100_list
        D_p_s100 = D.p_s100_list

        temp = []
        for d in D_str:
            for e in job_list:
                if d in e[2]:
                    temp.append(e)
            # if i in job_list
        job_list = temp
        
        # print(D_str)
        # # d = []
        # for i in D_str:
        #     job_list = job_list + list(filter(lambda n: i in n[2],job_list))
    # else:
    #     d = c
            
    s1 = p["seed"]["s1"]
    s2 = p["seed"]["s2"]
    Pdis=p["Pdis"]
    dx=p["dx"]
    bondDim=p["bondDim"]
    BC=p["BC"]
    check_Or_Not=p["check_Or_Not"]
    
        
    if (p["Spin"] != ""): 
        Spin=p["Spin"]
        job_list = list(filter(lambda n: Spin in n[2],job_list))
    if (p["Pdis"] != ""): 
        Pdis=p["Pdis"]
        job_list = list(filter(lambda n: Pdis in n[2],job_list))        
    if (p["bondDim"] != ""): 
        bondDim=p["bondDim"]
        job_list = list(filter(lambda n: bondDim in n[2],job_list))   
    if (p["BC"] != ""): 
        BC=p["BC"]
        job_list = list(filter(lambda n: BC in n[2],job_list))    
    if (Job_state != ""): 
        job_list = list(filter(lambda n: Job_state in n[3],job_list))     
     
    return job_list

def cancel(parameterlist):

    job_list = find(parameterlist)

    print("Cancel : \n\n")
    print("------------------------------------------------- \n\n")

    for i in range(len(job_list)):
        cmd = "scancel " + job_list[i][0]
        print(cmd + " : " + job_list[i][2])    
        os.system(cmd)
    
def show(parameterlist):
        
    job_list = find(parameterlist)

    print("show\n\n")
    print("------------------------------------------------------\n\n")

    for i in range(len(job_list)):
        print(job_list[i])
    

task = sys.argv[1]

parameterlist = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"seed":{"s1":None,"s2":None,"ds":None},\
                 "BC":None,"Pdis":None,"bondDim":None,"dx":None,"check_Or_Not":None,"status":None,"Ncore":None,"partition":None}
# Ncore = input("Ncore : \n")
# partition = input("partition : \n")
print("key in parameter in the following format : \n\
ex : Spin, L1, L2, delta_L, J1, J2, delta_J, D1, D2, delta_D, Pdis, bondDim, initialSampleNumber, finalSampleNumber, sampleDelta, check_Or_Not\n\
ex : 15(Spin) 64(L) 1.1(J) 0.1(D) 10(Pdis) 40(bondDim) 1(initialSampleNumber) 20(finalSampleNumber) 5(sampleDelta), Y(check_Or_Not)\n")

# try:
    # parameterlist["Spin"]=input("Spin : ")

    # parameterlist["L"]["L1"]=input("L1 : ")
    # parameterlist["L"]["L2"]=input("L2 : ")
    # parameterlist["L"]["dL"]=input("dL : ")    

    # parameterlist["J"]["J1"]=input("J1 : ")
    # parameterlist["J"]["J2"]=input("J2 : ")
    # parameterlist["J"]["dJ"]=input("dJ : ")

    # parameterlist["D"]["D1"]=input("D1 : ")
    # parameterlist["D"]["D2"]=input("D2 : ")
    # parameterlist["D"]["dD"]=input("dD : ")

    # parameterlist["seed"]["s1"]=input("initialSampleNumber : ")
    # parameterlist["seed"]["s2"]=input("finalSampleNumber : ")
    # parameterlist["seed"]["ds"]=input("sampleDelta : ")
    # parameterlist["BC"] = input("BC : ")
    # parameterlist["Pdis"] = input("Pdis : ")
    # parameterlist["bondDim"] = input("bondDim : ")
    # parameterlist["dx"] = input("dx : ")
    # parameterlist["check_Or_Not"]=input("check_Or_Not(Y/N) : ")
    # parameterlist["status"]=input("R/P) : ")
i = 2
for key1,value1 in parameterlist.items():
    if type(value1) != dict:
        try:
            if sys.argv[i] == "skip":
                parameterlist[key1] = ""
            else:
                parameterlist[key1]=sys.argv[i]
        except IndexError:
            parameterlist[key1]=""
        i = i + 1
    else:
        for key2,value2 in value1.items():
            try:
                if sys.argv[i] == "skip":
                    parameterlist[key1][key2] = ""
                else:
                    parameterlist[key1][key2]=sys.argv[i]
            except IndexError:
                parameterlist[key1][key2]=""
            i = i + 1
                
# parameterlist["L"]["L1"]=sys.argv[3]
# parameterlist["L"]["L2"]=sys.argv[4]
# parameterlist["L"]["dL"]=sys.argv[5]

# parameterlist["J"]["J1"]=sys.argv[6]
# parameterlist["J"]["J2"]=sys.argv[7]
# parameterlist["J"]["dJ"]=sys.argv[8]

# parameterlist["D"]["D1"]=sys.argv[9]
# parameterlist["D"]["D2"]=sys.argv[10]
# parameterlist["D"]["dD"]=sys.argv[11]

# parameterlist["seed"]["s1"]=sys.argv[12]
# parameterlist["seed"]["s2"]=sys.argv[13]
# parameterlist["seed"]["ds"]=sys.argv[14]
# parameterlist["BC"] = sys.argv[15]
# parameterlist["Pdis"] = sys.argv[16]
# parameterlist["bondDim"] = sys.argv[17]
# parameterlist["dx"] = sys.argv[18]
# parameterlist["check_Or_Not"]=sys.argv[19]
# parameterlist["status"]=sys.argv[20]
# parameterlist["Ncore"]=sys.argv[21]
# parameterlist["partition"]=sys.argv[22]
# except KeyboardInterrupt:
#     print("shut down")
#     exit()


print(parameterlist,"\n")
for s in parameterlist:
    print(s," : ",parameterlist[s])

tSDRG_path="/home/aronton/tSDRG_random"


if task == "submut" or task == "a":
    print("task")
    submut(parameterlist, tSDRG_path)
elif task == "show" or task == "b":
    show(parameterlist)
elif task == "cancel" or task == "c":
    cancel(parameterlist)