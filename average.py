import sys
import os
import datetime
import scriptCreator

task = input("What is the task? (a)submit, (b)resubmit, (c)cancel Jobs: : \n")
print(task)

parameterlist = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"seed":{"s1":None,"s2":None,"ds":None},\
                 "BC":None,"Pdis":None,"bondDim":None,"dx":None,"check_Or_Not":None}
Ncore = input("Ncore : \n")
partition = input("partition : \n")
print("key in parameter in the following format : \n\
ex : Spin, L1, L2, delta_L, J1, J2, delta_J, D1, D2, delta_D, Pdis, bondDim, initialSampleNumber, finalSampleNumber, sampleDelta, check_Or_Not\n\
ex : 15(Spin) 64(L) 1.1(J) 0.1(D) 10(Pdis) 40(bondDim) 1(initialSampleNumber) 20(finalSampleNumber) 5(sampleDelta), Y(check_Or_Not)\n")

try:
    parameterlist["Spin"]=input("Spin : ")

    parameterlist["L"]["L1"]=input("L1 : ")
    parameterlist["L"]["L2"]=input("L2 : ")
    parameterlist["L"]["dL"]=input("dL : ")    

    parameterlist["J"]["J1"]=input("J1 : ")
    parameterlist["J"]["J2"]=input("J2 : ")
    parameterlist["J"]["dJ"]=input("dJ : ")

    parameterlist["D"]["D1"]=input("D1 : ")
    parameterlist["D"]["D2"]=input("D2 : ")
    parameterlist["D"]["dD"]=input("dD : ")

    parameterlist["seed"]["s1"]=int(input("initialSampleNumber : "))
    parameterlist["seed"]["s2"]=int(input("finalSampleNumber : "))
    parameterlist["seed"]["ds"]=int(input("sampleDelta : "))
    parameterlist["BC"] = input("BC : ")
    parameterlist["Pdis"] = int(input("Pdis : "))
    parameterlist["bondDim"] = int(input("bondDim : "))
    parameterlist["dx"] = int(input("dx : "))
    parameterlist["check_Or_Not"]=input("check_Or_Not(Y/N) : ")
except KeyboardInterrupt:
    print("shut down")
    exit()



# parameterlist["Spin"]=sys.argv[0]

# parameterlist["L"]["L1"]=sys.argv[1]
# parameterlist["L"]["L2"]=sys.argv[2]
# parameterlist["L"]["dL"]=sys.argv[3]

# parameterlist["J"]["J1"]=sys.argv[4]
# parameterlist["J"]["J2"]=sys.argv[5]
# parameterlist["J"]["dJ"]=sys.argv[6]

# parameterlist["D"]["D1"]=sys.argv[7]
# parameterlist["D"]["D2"]=sys.argv[8]
# parameterlist["D"]["dD"]=sys.argv[9]

# parameterlist["seed"]["s1"]=int(sys.argv[10])
# parameterlist["seed"]["s2"]=int(sys.argv[11])
# parameterlist["seed"]["ds"]=int(sys.argv[12])
# parameterlist["BC"] = sys.argv[13]
# parameterlist["Pdis"] = int(sys.argv[14])
# parameterlist["bondDim"] = int(sys.argv[15])
# parameterlist["dx"] = int(sys.argv[16])
# parameterlist["check_Or_Not"]=sys.argv[17]



print(parameterlist,"\n")
for s in parameterlist:
    print(s," : ",parameterlist[s])

tSDRG_path="/home/aronton/tSDRG_random"

def submut(parameterlist, Ncore, partition, tSDRG_path):

    p = parameterlist

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
                    
                    # print("jobName:",jobName)
                    # print("script_name:",script_name)
                    # print("script_path:",script_path)
                    # print("output_path:",output_path)
                    
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

def show(parameterlist, Ncore, partition):
    
    print("show")
    
    p = parameterlist
    
    job_list = os.popen("squeue -u aronton " + "-p scopion" + str(partition) + " -o \"%%.12i %%.12P %%.90j %%.8T\"")

    a = list(job_list)

    del a[0]
    # print(a)
    for i in range(len(a)):
        a[i] = a[i].split()    
    for i in range(len(a)):
        print(a[i])
    # print(a)

    if (p["L"]["L1"] != "") and (p["L"]["L2"] != "") and (p["L"]["dL"] != ""): 
        L=scriptCreator.paraList("L",p["L"])
        L_num = L.num_list
        L_p_num = L.p_num_list
        L_str = L.str_list
        L_p_str = L.p_str_list
        L_s100 = L.s100_list
        L_p_s100 = L.p_s100_list
        print(L_str)
        b = []
        for i in L_str:
            b = b + list(filter(lambda n: i in n[2],a))
            
    if (p["J"]["J1"] != "") and (p["J"]["J2"] != "") and (p["J"]["dJ"] != ""): 
        J=scriptCreator.paraList("Jdis",p["J"])
        J_num = J.num_list
        J_p_num = J.p_num_list
        J_str = J.str_list
        J_p_str = J.p_str_list
        J_s100 = J.s100_list
        J_p_s100 = J.p_s100_list

        print(J_str)
        c = []
        for i in J_str:
            c = c + list(filter(lambda n: i in n[2],b))


    if (p["D"]["D1"] != "") and (p["D"]["D2"] != "") and (p["D"]["dD"] != ""): 
        D=scriptCreator.paraList("Dim",p["D"])
        D_num = D.num_list
        D_p_num = D.p_num_list
        D_str = D.str_list
        D_p_str = D.p_str_list
        D_s100 = D.s100_list
        D_p_s100 = D.p_s100_list
        
        print(D_str)
        d = []
        for i in D_str:
            d = d + list(filter(lambda n: i in n[2],c))
            
    s1 = p["seed"]["s1"]
    s2 = p["seed"]["s2"]
    Pdis=p["Pdis"]
    dx=p["dx"]
    bondDim=p["bondDim"]
    BC=p["BC"]
    check_Or_Not=p["check_Or_Not"]
    
    # print("ddd")
    # for i in range(len(d)):
    #     print(d[i])    
        
    if (p["Spin"] != ""): 
        Spin=p["Spin"]
        e = list(filter(lambda n: Spin in n[2],d))
    if (p["Pdis"] != ""): 
        Pdis=p["Pdis"]
        f = list(filter(lambda n: Pdis in n[2],e))        
    if (p["bondDim"] != ""): 
        bondDim=p["bondDim"]
        g = list(filter(lambda n: bondDim in n[2],f))   
    if (p["BC"] != ""): 
        BC=p["BC"]
        h = list(filter(lambda n: BC in n[2],g))     
    # print("hhh")
    # for i in range(len(h)):
    #     print(h[i])
        

# def cancel(parameterlist, Ncore, partition):
    
#     p = parameterlist

#     L=scriptCreator.paraList("L",parameterlist["L"])
#     L_num = L.num_list
#     L_s100 = L.s100_list
#     L_str = L.str_list
#     L_p_num = L.p_num_list

#     print("L_num:",L_num)
#     print("L_p_num:",L_p_num)
#     print("L_str:",L_str)
#     print("L_p_str:",L_p_str)
#     print("L_s100:",L_s100)
#     print("L_p_s100:",L_p_s100)

#     S=scriptCreator.Spara("Seed",parameterlist["seed"])
#     S_num = S.toS()
#     S_str = S.toStr()
#     s1 = parameterlist["seed"]["s1"]
#     s2 = parameterlist["seed"]["s2"]

#     J=scriptCreator.paraList("Jdis",parameterlist["J"])
#     J_num = J.num_list
#     J_p_num = J.p_num_list
#     J_str = J.str_list
#     J_p_str = J.p_str_list
#     J_s100 = J.s100_list
#     J_p_s100 = J.p_s100_list

#     D=scriptCreator.paraList("Dim",parameterlist["D"])
#     D_num = D.num_list
#     D_p_num = D.p_num_list
#     D_str = D.str_list
#     D_p_str = D.p_str_list
#     D_s100 = D.s100_list
#     D_p_s100 = D.p_s100_list

#     Spin=parameterlist["Spin"]
#     Pdis=parameterlist["Pdis"]
#     dx=parameterlist["dx"]
#     bondDim=parameterlist["bondDim"]
#     BC=parameterlist["BC"]
    
#     job_list = os.popen("squeue -u aronton " + "-p scopion" + str(partition) + " -o \"%%.12i %%.12P %%.90j %%.8T\"")
#     a = list(job_list)
#     del a[0]
#     for i in range(len(a)):
#         a[i] = a[i].split()
#     print(a)
#     print(J_str)
#     b = []
#     for i in J_str:
#         b = b + list(filter(lambda n: i in n[2],a))
#     # print(list(b))
#     print(D_str)
#     c = []
#     for i in D_str:
#         c = c + list(filter(lambda n: i in n[2],b))
#     # print(list(c))
#     print(Pdis)
#     d = []
#     d = d + list(filter(lambda n: str(Pdis) in n[2],c))
#     # print(list(d))

#     e = []
#     for i in L_str:
#         e = e + list(filter(lambda n: i in n[2],d))    
#     e=list(e)
       
#     return 0

# def p_del(b, title, L_s100):
#     for l_i,l in enumerate(L_s100):
#         b=filter(lambda s : title + str(l) in s[2],b)
#     return b
# def s_del(b, S_num):
#     for s_i in range(len(S_num)):
#         seed = S_num[s_i]
#         b=filter(lambda s : "seed1=" + str(seed[0]) in s[2],b)
#         b=filter(lambda s : "seed2=" + str(seed[-1]) in s[2],b)
#     return b
if task == "a":
    print(task)
    submut(parameterlist, Ncore, partition, tSDRG_path)
elif task == "b":
    print(task)
    show(parameterlist, Ncore, partition)
else:
    pass