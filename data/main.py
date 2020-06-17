#---preprocessing the spacing error in the file------

#-----extracting data-------
file = open('data.csv','r')
data = file.read()
file.close()

#-------formatting data------------
data = data.split('\n')
for i in range(0,len(data)):
    data[i]=data[i].split(',')
    for j in range(len(data[i])):
        data[i][j]=data[i][j].strip()
data[0][0]='lotid'


#----writing to the final file for csv--------
file=open('processed_data.csv','w')
s=''
for i in range(0,len(data)-1):
    s+=data[i][0]
    for j in range(1,len(data[i])):
        s+=','+data[i][j]
    s+='\n'
file.write(s)
file.close()