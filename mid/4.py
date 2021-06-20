class University:
    def __init__(self,name):
        self.name =name
        self.cps =[]
class Department:
    def __init__(self,name):
        self.name = name
class Campus:
    def __init__(self,name):
        self.name =name
        self.dep =[]
nkust =University("國立高雄科技大學")
cpsname = ["建工校區","旗津校區","第一校區","楠梓校區","燕巢校區"]
dpsname1= ['智商',"金資","會資","財稅","觀光","國企",'金資','企管','應外',"人力",'文創']
dpsname2= ['化工',"工管","土木","機械","模具","電機","電子","資訊","光電"]
dpsname3= ['營造',"環境","觀光","機自","創新","電機",'電通','電子','運管','資管',"行銷",'金融','風保','會資','財管','應英',"應日",'應德']
dpsname4= ['造船',"電訊","微電子","資管","海洋",'航管','供管','海休',"漁管",'水產','海生','水食']
dpsname5= ['輪機',"海事","航運"]
nkust_dc={"燕巢校區":dpsname1,"建工校區":dpsname2,"第一校區":dpsname3,"楠梓校區":dpsname4,"旗津校區":dpsname5}


for key,value in nkust_dc.items():
    nkust.cps.append(Campus(key))
    for i in value:
        nkust.cps[len(nkust.cps)-1].dep.append(Department(i))








