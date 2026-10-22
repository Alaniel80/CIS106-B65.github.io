#Iana Vasileva  CIS160 B65   M8P5    10/21/26
#open file
file=open("M8P5.txt","r")

#read name
last_name=file.readline().strip()

#Define
count=0
tuition_sum=0

#Display 1:
print(f"{"Last name":<15}{"Credits taken":<15}{"Tuition owed":<15}")

#Loop
while last_name!="":
    district_code=file.readline().strip()
    credits_taken=int(file.readline().strip())
    if district_code=="I":
        cost_per_credit=250.00
    else:
        cost_per_credit=500.00

#compute tuition owed
    tuition_owed=cost_per_credit*credits_taken
    count=count+1
    tuition_sum += tuition_owed
    print(f"{last_name:<15}{credits_taken:<15}{tuition_owed:<15.2f}")
#read next
    last_name = file.readline().strip()

#Close file
file.close()

#Display
print(f"Tuition owed summary: ${tuition_sum:.2f}")
print ("Number of students:",count)



