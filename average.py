import sys
import os
import datetime
import scriptCreator



def submit(parameterlist, tSDRG_path):

    p = parameterlist
    
    Ncore = parameterlist["Ncore"]
    partition = parameterlist["partition1"]
    para=scriptCreator.paraList1(parameterlist["L"],parameterlist["J"],parameterlist["D"],parameterlist["seed"])
    # L=scriptCreator.paraList1("L",parameterlist["L"])
    L_num = para.L_num
    L_p_num = para.L_p_num
    L_str = para.L_str
    L_p_str = para.L_p_str
    # L_s100 = para.L_s100
    # L_p_s100 = para.L_p_s100
    # L=scriptCreator.paraList("L",parameterlist["L"])
    # L_num = L.num_list
    # L_p_num = L.p_num_list
    # L_str = L.str_list
    # L_p_str = L.p_str_list
    # L_s100 = L.s100_list
    # L_p_s100 = L.p_s100_list   
    
    print("L_num:",L_num)
    print("L_p_num:",L_p_num)
    print("L_str:",L_str)
    print("L_p_str:",L_p_str)
    # print("L_s100:",L_s100)
    # print("L_p_s100:",L_p_s100)


    # S=scriptCreator.Spara("Seed",parameterlist["seed"])
    # S_num = S.toS
    # S_str = S.toStr
    # s1 = parameterlist["seed"]["s1"]
    # s2 = parameterlist["seed"]["s2"]

    S_num = para.S_num
    S_str = para.S_str
    s1 = parameterlist["seed"]["S1"]
    s2 = parameterlist["seed"]["S2"]
    print("S_num:",S_num)
    print("S_str:",S_str)

    # J=scriptCreator.paraList1("Jdis",parameterlist["J"])
    J_num = para.J_num
    J_p_num = para.J_p_num
    J_str = para.J_str
    J_p_str = para.J_p_str
    J_s100 = para.J_s100
    J_p_s100 = para.J_p_s100

    # J=scriptCreator.paraList("Jdis",p["J"])
    # J_num = J.num_list
    # J_p_num = J.p_num_list
    # J_str = J.str_list
    # J_p_str = J.p_str_list
    # J_s100 = J.s100_list
    # J_p_s100 = J.p_s100_list


    print("J_num",J_num)
    print("J_p_num",J_p_num)
    print("J_str:",J_str)
    print("J_p_str:",J_p_str)
    print("J_s100:",J_s100)
    print("J_p_s100:",J_p_s100)
    
    # D=scriptCreator.paraList1("Dim",parameterlist["D"])
    D_num = para.D_num
    D_p_num = para.D_p_num
    D_str = para.D_str
    D_p_str = para.D_p_str
    D_s100 = para.D_s100
    D_p_s100 = para.D_p_s100

    # D=scriptCreator.paraList("Dim",p["D"])
    # D_num = D.num_list
    # D_p_num = D.p_num_list
    # D_str = D.str_list
    # D_p_str = D.p_str_list
    # D_s100 = D.s100_list
    # D_p_s100 = D.p_s100_list

    print("D_num:",D_num)
    print("D_p_num:",D_p_num)
    print("D_str:",D_str)
    print("D_p_str:",D_p_str)
    print("D_s100:",D_s100)
    print("D_p_s100:",D_p_s100)

    Spin=parameterlist["Spin"]
    Pdis=parameterlist["Pdis"]
    bondDim=parameterlist["bondDim"]
    BC=parameterlist["BC"]
    check_Or_Not=parameterlist["check_Or_Not"]

    tSDRG_record = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/submit_record"
    record_dir = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/jobRecord" 
    script_dir = record_dir + "/script" + "/" + str(BC) + "/B" + str(bondDim)
    output_dir = record_dir + "/slurmOutput" + "/" + str(BC) + "/B" + str(bondDim)

    tSDRG_fileName="/tSDRG_Spin=" + str(Spin) + ";BC=" + str(BC) + ";P="+ str(Pdis) + ";B=" + str(bondDim) \
        + ";L=" + str(L_p_num[0]) + "_" + str(L_p_num[1]) + "(" + str(L_p_num[2])\
        + ");J=" + str(J_p_num[0]) + "_" + str(J_p_num[1]) +"(" + str(J_p_num[2]) \
        + ");D=" + str(D_p_num[0]) + "_" + str(D_p_num[1]) + "(" + str(D_p_num[2]) +");"\
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
    
    os.system( "cd " + tSDRG_path + "/tSDRG/Main_" + str(Spin))
    script_path_tot = "" 
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
                        
                    jobName = "Spin" + str(Spin) + "_" + str(l) + "_" + j + "_" + d + "_" + "P" + str(Pdis) \
                                + "_" + "BC=" + str(BC) + "_B" + str(bondDim) + "_Ncore=" + str(Ncore) + "_seed1=" \
                                    + str(s[0]) + "_seed2=" + str(s[-1])
                    script_name = jobName + "_" + now_date + "_" + now_time
                    script_path = script_path + "/" + script_name + "_random.sh"
                    output_path = output_path + "/" + script_name + "_random.out"
                    context = template.copy()
                    script_path_tot = script_path_tot + script_path + "\n"
                    with open(script_path, "w") as file:
                        context[1] = context[1].replace("replace1", "scopion" + str(partition))
                        context[3] = context[3].replace("replace2", jobName)
                        context[4] = context[4].replace("replace3", str(Ncore))
                        context[5] = context[5].replace("replace4", output_path)
                        file.writelines(context)
                    
                    submit_cmd_list = ["nohup sbatch ",script_path, str(Spin),str(L_num[l_i]),str(J_num[j_i]),str(D_num[d_i])\
                    ,str(BC),str(bondDim),str(Pdis),str(s[0]),str(s[-1]),check_Or_Not,str(Ncore),tSDRG_path,output_path, ">/dev/null 2>& 1&"]

                    submit_cmd = " ".join(submit_cmd_list)
                    os.system(submit_cmd)
    print(script_path_tot)

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
    partition = p["partition1"]      
      
    if partition != "":
        job_list = os.popen("squeue " + "-p scopion" + str(partition) + " -o \"%%.12i %%.12P %%.90j %%.8T\"")
    else:
        job_list = os.popen("squeue " + " -o \"%%.12i %%.12P %%.90j %%.8T\"")
    
    job_list = list(job_list)
    
    del job_list[0]
    for i in range(len(job_list)):
        job_list[i] = job_list[i].split()    

    para = scriptCreator.paraList1(p["L"],p["J"],p["D"],p["seed"])
    
    if (p["L"]["L1"] != "") and (p["L"]["L2"] != "") and (p["L"]["dL"] != ""): 
        # L=scriptCreator.paraList("L",p["L"])
        # L_num = L.num_list
        # L_p_num = L.p_num_list
        # L_str = L.str_list
        # L_p_str = L.p_str_list
        L_num = para.L_num
        L_p_num = para.L_p_num
        L_str = para.L_str
        L_p_str = para.L_p_str       
        temp = []
        for l in L_str:
            for e in job_list:
                if l in e[2]:
                    temp.append(e)
        job_list = temp

            
    if (p["J"]["J1"] != "") and (p["J"]["J2"] != "") and (p["J"]["dJ"] != ""): 
        # J=scriptCreator.paraList("Jdis",p["J"])
        # J_num = J.num_list
        # J_p_num = J.p_num_list
        # J_str = J.str_list
        # J_p_str = J.p_str_list
        # J_s100 = J.s100_list
        # J_p_s100 = J.p_s100_list
        J_num = para.J_num
        J_p_num = para.J_p_num
        J_str = para.J_str
        J_p_str = para.J_p_str
        J_s100 = para.J_s100
        J_p_s100 = para.J_p_s100
        temp = []
        for j in J_str:
            for e in job_list:
                if j in e[2]:
                    temp.append(e)
        job_list = temp




    if (p["D"]["D1"] != "") and (p["D"]["D2"] != "") and (p["D"]["dD"] != ""): 
        # D=scriptCreator.paraList("Dim",p["D"])
        # D_num = D.num_list
        # D_p_num = D.p_num_list
        # D_str = D.str_list
        # D_p_str = D.p_str_list
        # D_s100 = D.s100_list
        # D_p_s100 = D.p_s100_list
        D_num = para.D_num
        D_p_num = para.D_p_num
        D_str = para.D_str
        D_p_str = para.D_p_str
        D_s100 = para.D_s100
        D_p_s100 = para.D_p_s100
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
    # S_num = para.S_num
    # S_str = para.S_str
    # s1 = parameterlist["seed"]["S1"]
    # s2 = parameterlist["seed"]["S2"]            
    # s1 = p["seed"]["s1"]
    # s2 = p["seed"]["s2"]
    Pdis=p["Pdis"]
    # dx=p["dx"]
    bondDim=p["bondDim"]
    BC=p["BC"]
    # check_Or_Not=p["check_Or_Not"]
    
        
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

def Distribution(parameterlist):
        
    job_list = find(parameterlist)

    print("Distribution\n\n")
    print("------------------------------------------------------\n\n")
    print("tot:")
    tot=len(job_list)
    print(tot)
    print("Running:")
    job_list = list(filter(lambda n: "RUNNING" in n[3],job_list)) 
    run=len(job_list)
    print(run)
    print("Pending:")  
    print(tot-run)      


# task = input("task\n")
nt=datetime.datetime.now()

print("---------------------------"+str(nt.now())+"---------------------------")


# parameterlist = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
#                  "D":{"D1":None,"D2":None,"dD":None},"seed":{"s1":None,"s2":None,"ds":None},\
#                  "BC":None,"Pdis":None,"bondDim":None,"dx":None,"check_Or_Not":None,"status":None,"Ncore":None,"partition1":None,"partition2":None}
print("key in parameter in the following format : \n\
ex : Spin, L1, L2, delta_L, J1, J2, delta_J, D1, D2, delta_D, Pdis, bondDim, initialSampleNumber, finalSampleNumber, sampleDelta, check_Or_Not\n\
ex : 15(Spin) 64(L) 1.1(J) 0.1(D) 10(Pdis) 40(bondDim) 1(initialSampleNumber) 20(finalSampleNumber) 5(sampleDelta), Y(check_Or_Not)\n")

task = sys.argv[1]

a = scriptCreator.para(task)
parameterlist = a.para

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
if task == "change":
    psubmit = a.submit
    pcancel = a.cancel


# a = scriptCreator.para(task)
# parameterlist = a.para
# print(parameterlist)

print(parameterlist,"\n")
for s in parameterlist:
    print(s," : ",parameterlist[s])

tSDRG_path="/home/aronton/tSDRG_random"


if task == "submit" or task == "a":
    submit(parameterlist, tSDRG_path)
elif task == "show" or task == "b":
    show(parameterlist)
    Distribution(parameterlist)
elif task == "cancel" or task == "c":
    cancel(parameterlist)
elif task == "change" or task == "d":
    for key,value in parameterlist.items():
        if key in psubmit and key != "partition1":
            psubmit[key] = value
        if key in pcancel and key != "partition1":
            pcancel[key] = value
    print(parameterlist)
    pcancel["partition1"] = parameterlist["partition1"] 
    psubmit["partition1"] = parameterlist["partition2"]
    cancel(pcancel)
    submit(psubmit, tSDRG_path)
elif task == "dis" or task == "e":
    Distribution(parameterlist)
