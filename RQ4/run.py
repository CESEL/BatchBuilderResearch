import pandas as pd
from math import ceil



def runbatch(batch):

    for test in batch:
        if(test==False):
            return False
    return True




batch_feedback_time=0
clock=1
def batchstop4(batch):
    global batch_feedback_time
    global clock

    if (len(batch)<=4):
        l=(len(batch)*(len(batch)+1))/2
        batch_feedback_time=clock*len(batch)+l+batch_feedback_time
        clock+=len(batch)

    else:
        sub_batch_right=batch[0:ceil(len(batch)/2)]
        sub_batch_left=batch[ceil(len(batch)/2):len(batch)]
        clock+=1
        if(runbatch(sub_batch_right)==False):
            batchstop4(sub_batch_right)
        else:
            batch_feedback_time+=len(sub_batch_right)*clock
        clock+=1
        if(runbatch(sub_batch_left)==False):
            batchstop4(sub_batch_left)
        else:
            batch_feedback_time+=len(sub_batch_left)*clock
    return batch_feedback_time





def batchbisect(batch):
    global batch_feedback_time
    global clock

    if (len(batch)<=2):
        l=(len(batch)*(len(batch)+1))/2
        batch_feedback_time=clock*len(batch)+l+batch_feedback_time
        clock+=len(batch)

    else:
        sub_batch_right=batch[0:ceil(len(batch)/2)]
        sub_batch_left=batch[ceil(len(batch)/2):len(batch)]
        clock+=1
        if(runbatch(sub_batch_right)==False):
            batchstop4(sub_batch_right)
        else:
            batch_feedback_time+=len(sub_batch_right)*clock
        clock+=1
        if(runbatch(sub_batch_left)==False):
            batchstop4(sub_batch_left)
        else:
            batch_feedback_time+=len(sub_batch_left)*clock
    return batch_feedback_time







data_file=["ruby--ruby.csv",'rapid7--metasploit-framework.csv',"Graylog2--graylog2-server.csv","owncloud--android.csv","mitchellh--vagrant.csv","gradle--gradle.csv","puppetlabs--puppet.csv","opal--opal.csv","rspec--rspec-core.csv"]

batch_size=4
#this should be tuned based on the methodology
bisect=[4,8, 8, 7, 8, 8, 8, 8,4]
stop4=[4, 7, 8, 8, 8, 6, 8, 8, 4]
batch4=[4, 4, 4, 4, 4, 4, 4, 4, 4]
batch2=[2, 2, 2, 2, 2, 2, 2, 2, 2]


r=0
i=0
val = input("Enter your value 1:BatchStop4 2:BatchBisect 3: batch4 4: Batch2 ")
if(val=='1'):
    method_type=batchstop4
    batch_size_list=stop4

elif(val=='2'):
    method_type=batchbisect
    batch_size_list=bisect


elif (val == '3'):
    method_type = batchstop4
    batch_size_list = batch4

elif (val == '4'):
    method_type = batchstop4
    batch_size_list = batch2

for path in data_file:
    print(path)

    batch_size=batch_size_list[i]
    i+=1


    feedbacktime=0
    data_path= './data/'+path
    data = pd.read_csv(data_path)


    data = data.build_successful
    data = pd.Series.tolist(data)

    data = data[100:]

    counter=0
    flag=True
    while(flag):
        slicebatch=data[counter:(counter+batch_size)]
        counter=counter+batch_size
        clock=1
        batch_feedback_time=0
        if(runbatch(slicebatch)==True):
            feedbacktime+=len(slicebatch)
        else:
            feedbacktime+=method_type(slicebatch)
        if(counter>=len(data)):
            flag=False
    print(1-(feedbacktime/(len(data)*((batch_size+1)/2))))
    r+=1


