import pandas as pd

def markAttendance(name):
    if 'Unknown' in name:
        name.remove('Unknown')
    p={'kumar':['99210041514'],'Karthik':['99210041518']}
    l2=[]
    l3=[]
    for i in name:
       if i in p:
           l2.append(p[i][0])
        #    l3.append(p[i][1])
       else:
           l2.append('UnKnown')
        #    l3.append('Unknown')
    p={'name':name,'Reg no':l2}
    n = pd.DataFrame(p)
    n.to_csv("attx.csv")
                