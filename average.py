import sys
import os
import datetime
import scriptCreator
tSDRG_path="/home/aronton/tSDRG_random"

def submitPara(parameterlist, tSDRG_path):

    p = parameterlist
    Spin = parameterlist["Spin"]
    Ncore = parameterlist["Ncore"]
    partition = parameterlist["partition1"]
    para=scriptCreator.paraList1(parameterlist["L"],parameterlist["J"],parameterlist["D"],parameterlist["seed"])
    L_num = para.L_num
    L_p_num = para.L_p_num
    L_str = para.L_str
    L_p_str = para.L_p_str
    

    
    print("L_num:",L_num)
    print("L_p_num:",L_p_num)
    print("L_str:",L_str)
    print("L_p_str:",L_p_str)

    S_num = para.S_num
    S_str = para.S_str
    s1 = parameterlist["seed"]["S1"]
    s2 = parameterlist["seed"]["S2"]
    print("S_num:",S_num)
    print("S_str:",S_str)

    J_num = para.J_num
    J_p_num = para.J_p_num
    J_str = para.J_str
    J_p_str = para.J_p_str
    J_s100 = para.J_s100
    J_p_s100 = para.J_p_s100


    print("J_num",J_num)
    print("J_p_num",J_p_num)
    print("J_str:",J_str)
    print("J_p_str:",J_p_str)
    print("J_s100:",J_s100)
    print("J_p_s100:",J_p_s100)
    
    D_num = para.D_num
    D_p_num = para.D_p_num
    D_str = para.D_str
    D_p_str = para.D_p_str
    D_s100 = para.D_s100
    D_p_s100 = para.D_p_s100

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

    # tSDRG_fileName="/tSDRG_Spin=" + str(Spin) + ";BC=" + str(BC) + ";P="+ str(Pdis) + ";B=" + str(bondDim) \
    #     + ";L=" + str(L_p_num[0]) + "_" + str(L_p_num[1]) + "(" + str(L_p_num[2])\
    #     + ");J=" + str(J_p_num[0]) + "_" + str(J_p_num[1]) +"(" + str(J_p_num[2]) \
    #     + ");D=" + str(D_p_num[0]) + "_" + str(D_p_num[1]) + "(" + str(D_p_num[2]) +");"\
    #     + "seed1=" + str(s1) + "_seed2=" + str(s2) + ";Partition=" + str(partition) + ";Number_of_core=" + str(Ncore)

    nt=datetime.datetime.now()
    now_year = str(nt.year)
    now_date = str(nt.year) + "_" + str(nt.month) + "_" + str(nt.day)
    now_time = "H" + str(nt.hour) + "_M" + str(nt.minute) + "_S" + str(nt.second)
    
    # tSDRG_fileDir = tSDRG_record + "/" + now_year + "/" + now_date

    # if os.path.exists(tSDRG_fileDir):
    #     print(tSDRG_fileDir)
    # else:
    #     os.makedirs(tSDRG_fileDir)

    # tSDRG_filePath = tSDRG_fileDir + tSDRG_fileName + "_" + now_time

    # with open(tSDRG_filePath, "wt") as file:
    #     file.write(tSDRG_fileName)

    with open("run.sh", "r") as file:
        template = file.readlines()

    # print("tSDRG_filePath : ",tSDRG_filePath)
    
    os.system( "cd " + tSDRG_path + "/tSDRG/Main_" + str(Spin))
    script_path_tot = "" 
    submitlsit = []
    for l,L in enumerate(L_str):
        for j,J in enumerate(J_str):
            for d,D in enumerate(D_str):
                for s_i in range(len(S_num)):
                    s = S_num[s_i]
                    name = ["Spin"+Spin,L,J,D,"P"+str(Pdis),"BC="+BC,"B"+str(bondDim),"Ncore="+Ncore,"seed1="+str(s[0]),"seed2="+str(s[-1])]
                    name = "_".join(name)
                    submitlsit.append(name)
    return submitlsit               

def submit(parameterlist, tSDRG_path):
    
    tSDRG_record = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/submit_record"
    record_dir = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/jobRecord" 
    script_dir = record_dir + "/script" + "/" + str(BC) + "/B" + str(bondDim)
    output_dir = record_dir + "/slurmOutput" + "/" + str(BC) + "/B" + str(bondDim)
    
def EditandSub(parameterlist,script_path,output_path,jobName,context):

    partition = parameterlist["partition1"]
    Ncore = parameterlist["Ncore"]
    check_Or_Not = parameterlist["check_Or_Not"]

    elementlist = jobName.split("_")
    Spin = elementlist[0].replace("Spin","")
    L = elementlist[1].replace("L","")
    J = elementlist[2][4] + "." + elementlist[2][5] + elementlist[2][6]
    D = elementlist[3][3] + "." + elementlist[3][4] + elementlist[3][5]
    Pdis = elementlist[4].replace("P","")
    BC = elementlist[5].replace("BC=","")
    bondDim = elementlist[6].replace("B","")
    s1 = elementlist[7].replace("seed1=","")
    s2 = elementlist[8].replace("seed2=","")
    
    with open(script_path, "w") as file:
        context[1] = context[1].replace("replace1", "scopion" + str(partition))
        context[3] = context[3].replace("replace2", jobName)
        context[4] = context[4].replace("replace3", str(Ncore))
        context[5] = context[5].replace("replace4", output_path)
        file.writelines(context)
    
    submit_cmd_list = ["nohup sbatch ",script_path, str(Spin),str(L),str(J),str(D)\
    ,str(BC),str(bondDim),str(Pdis),str(s1),str(s2),check_Or_Not,str(Ncore),tSDRG_path,output_path, ">/dev/null 2>& 1&"]

    submit_cmd = " ".join(submit_cmd_list)
    os.system(submit_cmd)    

def submit(parameterlist, tSDRG_path, tasklist):

    p = parameterlist
    
    Ncore = parameterlist["Ncore"]
    partition = parameterlist["partition1"]
    Spin=parameterlist["Spin"]
    Pdis=parameterlist["Pdis"]
    bondDim=parameterlist["bondDim"]
    BC=parameterlist["BC"]
    check_Or_Not=parameterlist["check_Or_Not"]

    # tSDRG_record = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/submit_record"
    record_dir = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/jobRecord" 
    script_dir = record_dir + "/script" + "/" + str(BC) + "/B" + str(bondDim)
    output_dir = record_dir + "/slurmOutput" + "/" + str(BC) + "/B" + str(bondDim)

    # tSDRG_fileName="/tSDRG_Spin=" + str(Spin) + ";BC=" + str(BC) + ";P="+ str(Pdis) + ";B=" + str(bondDim) \
    #     + ";L=" + str(L_p_num[0]) + "_" + str(L_p_num[1]) + "(" + str(L_p_num[2])\
    #     + ");J=" + str(J_p_num[0]) + "_" + str(J_p_num[1]) +"(" + str(J_p_num[2]) \
    #     + ");D=" + str(D_p_num[0]) + "_" + str(D_p_num[1]) + "(" + str(D_p_num[2]) +");"\
    #     + "seed1=" + str(s1) + "_seed2=" + str(s2) + ";Partition=" + str(partition) + ";Number_of_core=" + str(Ncore)

    nt=datetime.datetime.now()
    now_year = str(nt.year)
    now_date = str(nt.year) + "_" + str(nt.month) + "_" + str(nt.day)
    now_time = "H" + str(nt.hour) + "_M" + str(nt.minute) + "_S" + str(nt.second)
    
    # tSDRG_fileDir = tSDRG_record + "/" + now_year + "/" + now_date

    # if os.path.exists(tSDRG_fileDir):
    #     print(tSDRG_fileDir)
    # else:
    #     os.makedirs(tSDRG_fileDir)

    # tSDRG_filePath = tSDRG_fileDir + tSDRG_fileName + "_" + now_time

    # with open(tSDRG_filePath, "wt") as file:
    #     file.write(tSDRG_fileName)

    with open("run.sh", "r") as file:
        template = file.readlines()

    # print("tSDRG_filePath : ",tSDRG_filePath)
    
    os.system( "cd " + tSDRG_path + "/tSDRG/Main_" + str(Spin))
    script_path_tot = "" 
    # for l_i,l in enumerate(L_str):
    #     for j_i,j in enumerate(J_str):
    #         for d_i,d in enumerate(D_str):
    #             for s_i in range(len(S_num)):
    #                 s = S_num[s_i]
    for jobName in tasklist:
        
        elementlist = jobName.split("_")
        
        L = elementlist[1]
        J = elementlist[2]
        D = elementlist[3]
        
        script_path = script_dir + "/" + L + "/" + J + "/" + D  
        output_path = output_dir + "/" + L + "/" + J + "/" + D
        
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
            
        # jobName = "Spin" + str(Spin) + "_" + str(l) + "_" + j + "_" + d + "_" + "P" + str(Pdis) \
        #             + "_" + "BC=" + str(BC) + "_B" + str(bondDim) + "_Ncore=" + str(Ncore) + "_seed1=" \
        #                 + str(s[0]) + "_seed2=" + str(s[-1])
        script_name = jobName + "_" + now_date + "_" + now_time
        script_path = script_path + "/" + script_name + "_random.sh"
        output_path = output_path + "/" + script_name + "_random.out"
        context = template.copy()
        script_path_tot = script_path_tot + script_path + "\n"
        EditandSub(parameterlist,script_path,output_path,jobName,context)
        # with open(script_path, "w") as file:
        #     context[1] = context[1].replace("replace1", "scopion" + str(partition))
        #     context[3] = context[3].replace("replace2", jobName)
        #     context[4] = context[4].replace("replace3", str(Ncore))
        #     context[5] = context[5].replace("replace4", output_path)
        #     file.writelines(context)
        
        # submit_cmd_list = ["nohup sbatch ",script_path, str(Spin),str(L_num[l_i]),str(J_num[j_i]),str(D_num[d_i])\
        # ,str(BC),str(bondDim),str(Pdis),str(s[0]),str(s[-1]),check_Or_Not,str(Ncore),tSDRG_path,output_path, ">/dev/null 2>& 1&"]

        # submit_cmd = " ".join(submit_cmd_list)
        # os.system(submit_cmd)
    print(script_path_tot)


def submit1(parameterlist, tSDRG_path, tasklist):

    p = parameterlist
    
    Ncore = parameterlist["Ncore"]
    partition = parameterlist["partition1"]
    para=scriptCreator.paraList1(parameterlist["L"],parameterlist["J"],parameterlist["D"],parameterlist["seed"])
    L_num = para.L_num
    L_p_num = para.L_p_num
    L_str = para.L_str
    L_p_str = para.L_p_str

    
    print("L_num:",L_num)
    print("L_p_num:",L_p_num)
    print("L_str:",L_str)
    print("L_p_str:",L_p_str)

    S_num = para.S_num
    S_str = para.S_str
    s1 = parameterlist["seed"]["S1"]
    s2 = parameterlist["seed"]["S2"]
    print("S_num:",S_num)
    print("S_str:",S_str)

    J_num = para.J_num
    J_p_num = para.J_p_num
    J_str = para.J_str
    J_p_str = para.J_p_str
    J_s100 = para.J_s100
    J_p_s100 = para.J_p_s100


    print("J_num",J_num)
    print("J_p_num",J_p_num)
    print("J_str:",J_str)
    print("J_p_str:",J_p_str)
    print("J_s100:",J_s100)
    print("J_p_s100:",J_p_s100)
    
    D_num = para.D_num
    D_p_num = para.D_p_num
    D_str = para.D_str
    D_p_str = para.D_p_str
    D_s100 = para.D_s100
    D_p_s100 = para.D_p_s100

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
        
    Pdis=p["Pdis"]
    bondDim=p["bondDim"]
    BC=p["BC"]
    
        
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
def get(parameterlist):
    
    job_list = find(parameterlist)
    task_list = []
    for job in job_list:
        task_list.append(job[2])
        
    return task_list


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

def check(parameterlist):
        
    p = parameterlist
    
    Ncore = parameterlist["Ncore"]
    partition = parameterlist["partition1"]
    para=scriptCreator.paraList1(parameterlist["L"],parameterlist["J"],parameterlist["D"],parameterlist["seed"])
    # L=scriptCreator.paraList1("L",parameterlist["L"])
    L_num = para.L_num
    L_p_num = para.L_p_num
    L_str = para.L_str
    L_p_str = para.L_p_str

    
    print("L_num:",L_num)
    print("L_p_num:",L_p_num)
    print("L_str:",L_str)
    print("L_p_str:",L_p_str)

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
    tSDRG_path = tSDRG_path + "/data_random/" + str(BC) + "/"
    for l_i,l in enumerate(L_str):
        for j_i,j in enumerate(J_str):
            for d_i,d in enumerate(D_str):
                for s_i in range(len(S_num)):
                    s = S_num[s_i]
                    ZL = tSDRG_path + "L" + str(L) + "_P" + str(Pdis) + "_m" + str(bondDim) + "_" + str(s[-1]) + "/ZL.csv"
                    energy = tSDRG_path + "L" + str(L) + "_P" + str(Pdis) + "_m" + str(bondDim) + "_" + str(s[-1]) + "/energy.csv"
                    path = script_dir + "/" + l + "/" + j + "/" + d  
                    path = output_dir + "/" + l + "/" + j + "/" + d
    #                 if os.path.exists(script_path):
    #                     pass
    #                     # print("exist : ", script_path)
    #                 else:
    #                     # print("not exist : ", script_path)
    #                     os.makedirs(script_path)
                        
    #                 if os.path.exists(output_path):
    #                     pass
    #                     # print("exist : ", output_path)
    #                 else:
    #                     # print("not exist : ", output_path)
    #                     os.makedirs(output_path)
                        
    #                 jobName = "Spin" + str(Spin) + "_" + str(l) + "_" + j + "_" + d + "_" + "P" + str(Pdis) \
    #                             + "_" + "BC=" + str(BC) + "_B" + str(bondDim) + "_Ncore=" + str(Ncore) + "_seed1=" \
    #                                 + str(s[0]) + "_seed2=" + str(s[-1])
    #                 script_name = jobName + "_" + now_date + "_" + now_time
    #                 script_path = script_path + "/" + script_name + "_random.sh"
    #                 output_path = output_path + "/" + script_name + "_random.out"
    #                 context = template.copy()
    #                 script_path_tot = script_path_tot + script_path + "\n"
    #                 with open(script_path, "w") as file:
    #                     context[1] = context[1].replace("replace1", "scopion" + str(partition))
    #                     context[3] = context[3].replace("replace2", jobName)
    #                     context[4] = context[4].replace("replace3", str(Ncore))
    #                     context[5] = context[5].replace("replace4", output_path)
    #                     file.writelines(context)
                    
    #                 submit_cmd_list = ["nohup sbatch ",script_path, str(Spin),str(L_num[l_i]),str(J_num[j_i]),str(D_num[d_i])\
    #                 ,str(BC),str(bondDim),str(Pdis),str(s[0]),str(s[-1]),check_Or_Not,str(Ncore),tSDRG_path,output_path, ">/dev/null 2>& 1&"]

    #                 submit_cmd = " ".join(submit_cmd_list)
    #                 os.system(submit_cmd)
    # print(script_path_tot)

# task = input("task\n")

def main():
    nt=datetime.datetime.now()

    print("---------------------------"+str(nt.now())+"---------------------------")

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
        psubmit = a.resubmit
        pcancel = a.cancel

    print(parameterlist,"\n")
    for s in parameterlist:
        print(s," : ",parameterlist[s])

    if task == "submit" or task == "a":
        tasklist = submitPara(parameterlist, tSDRG_path)
        submit(parameterlist, tSDRG_path, tasklist)
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
        tasklist=get(pcancel)
        cancel(pcancel)
        submit(psubmit, tSDRG_path, tasklist)
    elif task == "dis" or task == "e":
        Distribution(parameterlist)
    elif task == "check" or task == "f":
        Distribution(parameterlist)
    return

if __name__ == '__main__' :
    main()
