#Iana Vasileva  CIS160 B65   M9P5    10/24/26
#define function for charge per credit and to compute tuition
def charge_per_credit(dist_code):
    if dist_code=="I":
        return 250
    elif dist_code=="O":
        return 550
    else:
        return 0

def compute_tuition_owed(dist_code,credit_hrs):
    tuition_owed=charge_per_credit(dist_code)*credit_hrs
    return tuition_owed

#Define sum of tuitions
sum_tuition=0

#User's input and loop
last_name = str(input("Enter your last name (Enter to stop): "))
while last_name!="":
    credit_hrs=int(input("Enter your credit hours: "))
    dist_code=str(input("Enter your district code (I or O):").upper())
    while dist_code!="I" and dist_code!="O":
        print("Please enter a valid district code")
        dist_code = str(input("Enter your district code (I or O):").upper())

    tuition_owed = compute_tuition_owed(dist_code, credit_hrs)

#define total tuition
    sum_tuition+=tuition_owed

#Display last name and tuition owed
    print("Last Name:",last_name)
    print(f"Tuition owed:${tuition_owed:.2f}")
    print()

#next entry:
    last_name = str(input("Enter your last name (Enter to stop): "))

#display summary of tuition owed
print(f"Total Tuition owed:${sum_tuition:.2f}")
