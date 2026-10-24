#Iana Vasileva  CIS160 B65   M9P4    10/24/26
#Define pay rate depending on the job code
def get_pay_rate(job_code):
    if job_code=="A":
        return 30
    elif job_code=="J":
        return 50
    elif job_code=="L":
        return 25
    else:
        return 0

#Define total gross
sum_gross = 0

#Input from a user and loop
last_name=str(input("Enter your last name (Enter to stop):"))
while last_name!="":
    job_code=input("Enter your job code(L,A,or J):").upper()
    pay_rate=get_pay_rate(job_code)
    while pay_rate==0:
        print("Please enter a valid job code")
        job_code = input("Enter your job code(L,A,or J):").upper()
        pay_rate = get_pay_rate(job_code)

    hours_worked = int(input("Enter your hours worked:"))

#Compute gross pay
    if hours_worked>40:
        over_time=hours_worked-40
        gross_pay=(pay_rate*hours_worked)+(over_time*pay_rate*1.5)
    else:
        gross_pay=hours_worked*pay_rate

#Count sun gross pay and # Define sum of gross pay
    sum_gross+=gross_pay

#Display last name and gross pay
    print("Last Name:",last_name)
    print(f"Gross pay:${gross_pay:.2f}")

#next entry
    last_name=str(input("Enter your last name (Enter to stop):"))

#Display number of entries
print(f"Sum of all gross pays:${sum_gross:.2f}")
