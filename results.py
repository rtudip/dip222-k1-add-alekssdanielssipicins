data=[]
with open("data.txt") as file:
    for line in file:
        row=line.rstrip().split(",")
        data.append(row)

list_oman=[]
for line in data:
    if line[4]=="Oman":
        list_oman.append(line) 
founded=2023
for line in list_oman:
    if int(line[6])<founded:
        founded=int(line[6])

list_latvia=[]
for line in data:
    if line[4]=="Latvia":
        list_latvia.append(line)

employees=0
for line in list_latvia:
     employees+=int(line[8])

employees_tel=0
for line in list_latvia:
    if line[7]=="Telecommunications":
        employees_tel+=int(line[8])

ssl_count=0
for line in list_latvia:
    if line[3][:8]=="https://":
        ssl_count+=1

org_count=0
for line in list_latvia:
    if ".org" in line[3]:
        org_count+=1

print("1: "+str(founded)+"\n"+"2: "+str(employees)+"\n"+"3: "+str(employees_tel)+"\n"+"4: "+str(ssl_count)+"\n"+"5: "+str(org_count))

