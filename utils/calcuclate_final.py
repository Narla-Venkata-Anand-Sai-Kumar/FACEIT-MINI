from datetime import datetime

def calculate(l1,l2,timestamp_dict):
    for i in l1:
        if i not in l2:
            l2[i]=1
        else:
            l2[i]+=1
    final_list={}
    for i in l2:
        if l2[i]>3:
            dt_final = datetime.fromtimestamp(max(timestamp_dict[i]))
            final_list[i] = [dt_final.strftime("%H:%M:%S")]
    return final_list