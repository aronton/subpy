import re
import os

class paraList:
    def __init__(self,title,inlist):
        # self._numlist = list(numlist.values())
        if ("." in list(inlist.values())[0]) or ("." in list(inlist.values())[1]) or ("." in list(inlist.values())[2]): 
            self.intOrnot = "N"
        else:
            self.intOrnot = "Y"
        self.p_s100_list = [] # ex 050,150,050
        self.set_p_s100_list(title,list(inlist.values()))
        # self.p_list = list(inlist.values())
        self.p_num_list = [] # ex 0.5,1.5,0.5
        self.set_p_num_list(title,list(inlist.values()))
        self.p_str_list = [] # ex Jdis050,Jdis150,Jdis050
        self.set_p_str_list(title,self.p_s100_list.copy())

        self.s100_list = [] # ex 050,100,150...
        self.set_s100_list(title,self.p_s100_list.copy())
        self.num_list = [] # ex 0.5,1,1.5...
        self.set_num_list(title,self.s100_list.copy())
        self.str_list = [] # ex Jdis050,Jdis100,Jdis150...
        self.set_str_list(title,self.s100_list.copy())
        
    def set_p_s100_list(self,title,inlist):
        # if self.intOrnot == "N":
        if inlist[0] == inlist[1]:
            s = str(float(inlist[0]))
            s = inlist[0]
            slen = len(s)
            l=re.sub("[^0-9]", "", s)

            if self.intOrnot == "N":
                while len(l) < 3:
                    l = l + "0"                
            self.p_s100_list = [l,l,"000"]
        else:
            p1=re.sub("[^0-9]", "", inlist[0])
            if self.intOrnot == "N":
                while len(p1) < 3:
                    p1 = p1 + "0"            
            p2=re.sub("[^0-9]", "", inlist[1])
            if self.intOrnot == "N":
                while len(p2) < 3:
                    p2 = p2 + "0"
            dp=re.sub("[^0-9]", "", inlist[2])
            if self.intOrnot == "N":
                while len(dp) < 3:
                    dp = dp + "0"      
            self.p_s100_list = [p1,p2,dp]    
        # else:
        #     if inlist[0] == inlist[1]:
        #         slen = len(inlist[0])
        #         l=re.sub("[^0-9]", "", inlist[0])
        #         while len(l) < slen:
        #             l = l + "0"
        #         self.p_s100_list = [l,l,"000"]
        #     else:
        #         p1=re.sub("[^0-9]", "", inlist[0])
        #         if self.intOrnot == "N":
        #             while len(p1) < 3:
        #                 p1 = p1 + "0"            
        #         p2=re.sub("[^0-9]", "", inlist[1])
        #         if self.intOrnot == "N":
        #             while len(p2) < 3:
        #                 p2 = p2 + "0"
        #         dp=re.sub("[^0-9]", "", inlist[2])
        #         if self.intOrnot == "N":
        #             while len(dp) < 3:
        #                 dp = dp + "0"      
        #         self.p_s100_list = [p1,p2,dp]    
    def set_p_num_list(self,title,inlist):
        if inlist[0] == inlist[1]:
            inlist[2] = "0"
        l_num = []
        for s in inlist:
            l = [c for c in s if c.isdigit()]
            if "." in s:
                l.insert(1,".")
                x = "".join(l)
                num = float("".join(x))
            else:
                x = "".join(l)
                num = int("".join(x))
            l_num.append(num)
        self.p_num_list = l_num
    def set_p_str_list(self,title,inlist):
        self.p_str_list = []
        for s in inlist:
            self.p_str_list.append(title + s)
    def set_s100_list(self,title,inlist):
        if self.intOrnot == "N":
            if inlist[0] == inlist[1]:
                l = []
                l.append(inlist[0])
            else:
                n = int((int(inlist[1]) - int(inlist[0]))/int(inlist[2]))
                l = []
                for i in range(n+1):
                    if len(str(int(inlist[0]) + i*int(inlist[2])))==2:
                        l.append("0"+str(int(inlist[0]) + i*int(inlist[2])))
                    elif len(str(int(inlist[0]) + i*int(inlist[2])))==1:
                        l.append("00"+str(int(inlist[0]) + i*int(inlist[2])))
                    else:
                        l.append(str(int(inlist[0]) + i*int(inlist[2])))
            self.s100_list = list(l)
        else:
            if inlist[0] == inlist[1]:
                l = []
                l.append(str(int(inlist[0])))
            else:
                n = int((int(inlist[1]) - int(inlist[0]))/int(inlist[2]))
                l = []
                for i in range(n+1):
                    if len(str(int(inlist[0]) + i*int(inlist[2])))==2:
                        l.append(str(int(inlist[0]) + i*int(inlist[2])))
                    elif len(str(int(inlist[0]) + i*int(inlist[2])))==1:
                        l.append(str(int(inlist[0]) + i*int(inlist[2])))
                    else:
                        l.append(str(int(inlist[0]) + i*int(inlist[2])))
            self.s100_list = list(l)        
    def set_num_list(self,title,inlist):
        l = []
        if self.intOrnot == "N":
            for s in inlist:
                l.append(float(s[0]+"."+s[1]+s[2]))
        else:
            for s in inlist:
                l.append(int(s))            
        self.num_list = list(l)
    def set_str_list(self,title,inlist):
        l = []
        for s in inlist:
            if self.intOrnot == "N":
                if int(s) == 0:
                    l.append(title + "000")
                else:
                    l.append(title + str(s))
            else:
                if int(s) == 0:
                    l.append(title + "000")
                else:
                    l.append(title + str(s))
        self.str_list = list(l)
        
class Lpara:
    def __init__(self,title,inlist):
        
        self.p_s100_list = [] # ex 050,150,050
        self.set_p_s100_list(title,list(inlist.values()))
        # self.p_list = list(inlist.values())
        self.p_num_list = [] # ex 0.5,1.5,0.5
        self.set_p_num_list(title,list(inlist.values()))
        self.p_str_list = [] # ex Jdis050,Jdis150,Jdis050
        self.set_p_str_list(title,self.p_s100_list.copy())

        self.s100_list = [] # ex 050,100,150...
        self.set_s100_list(title,self.p_s100_list.copy())
        self.num_list = [] # ex 0.5,1,1.5...
        self.set_num_list(title,self.s100_list.copy())
        self.str_list = [] # ex Jdis050,Jdis100,Jdis150...
        self.set_str_list(title,self.s100_list.copy())
        
        # self.p_list = list(inlist.values())
        # self.p_num_list = []
        # self.set_p_num_list(title,list(inlist.values()))
        # self.p_s100_list = []
        # self.set_p_s100_list(title,list(inlist.values()))
        # self.p_str_list = []
        # self.set_p_str_list(title,self.p_s100_list.copy())

        # self.s100_list = []
        # self.set_s100_list(title,self.p_s100_list.copy())
        # self.num_list = []
        # self.set_num_list(title,self.s100_list.copy())
        # self.str_list = []
        # self.set_str_list(title,self.s100_list.copy())
    def set_p_s100_list(self,title,inlist):
        for s in inlist:
            self.p_s100_list.append(str(int(s)))
    def set_p_num_list(self,title,inlist):
        for s in inlist:
            self.p_num_list.append(int(s))
    def set_p_str_list(self,title,inlist):
        for s in inlist:
            self.p_str_list.append(title + str(int(s)))
            
    def set_s100_list(self,title,inlist):
        if inlist[0] == inlist[1]:
            l = []
            l.append(str(int(inlist[0])))
        else:
            n = int((int(inlist[1]) - int(inlist[0]))/int(inlist[2]))
            l = []
            for i in range(n+1):
                # if len(str(int(inlist[0]) + i*int(inlist[2])))==2:
                #     l.append("0"+str(int(inlist[0]) + i*int(inlist[2])))
                # else:
                l.append(str(int(inlist[0]) + i*int(inlist[2])))
        self.s100_list = list(l)
    def set_num_list(self,title,inlist):
        l = []
        for s in inlist:
            l.append(int(s))
        self.num_list = list(l)
    def set_str_list(self,title,inlist):
        l = []
        for s in inlist:
            l.append(title + s)
        self.str_list = list(l)

class Spara:
    def __init__(self,title,numlist):
        numlist = list(numlist.values())
        self.x1 = int(numlist[0])
        self.x2 = int(numlist[1])
        self.dx = int(numlist[2])
        self.title = title
    def toS(self):
        numSeed = []
        for i in list(range(self.x1 ,self.x2, self.dx)):
            a = [j for j in list(range(i,i+self.dx))]
            numSeed.append(a)
        # print(numSeed)
        # numL = [self.x1 + l*self.dx for l in range(int((self.x2-self.x1)/self.dx) + 1)]
        return list(numSeed)   
    def toStr(self):
        if self.x2>0:
            strSeed = []
            for i in list(range(self.x1 ,self.x2,self.dx)):
                a = [self.title + str(j) for j in list(range(i,i+self.dx))]
                strSeed.append(a)
            # numL = [ self.title + str(self.x1 + l*self.dx) for l in range(int((self.x2-self.x1)/self.dx) + 1)]
        else:
            strSeed = []
            for i in list(range(self.x1 ,self.x2,self.dx)):
                a = [self.title + "N" + str(j) for j in list(range(i,i+self.dx))]
                strSeed.append(a)
            # numL = [ self.title + "N" + str((self.x1 + l*self.dx)*-1) for l in range(int((self.x2-self.x1)/self.dx) + 1)]    
        return list(strSeed)    
    def __repr__(self):
        return f'Point({self.x1}, {self.x2}, {self.dx})'