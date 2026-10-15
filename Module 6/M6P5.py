#Iana Vasileva CIS160 B65    M6P5 10/14/26
#User's input
last_name=str(input("Enter a last name: "))
salary=int(input("Enter a salary: "))
job_lvl=int(input("Enter a job level: "))

# determine the bonus rate. Compute bonus amount
if job_lvl>=10:
    bonus_rate=25
elif 5<=job_lvl<=9:
    bonus_rate=20
elif job_lvl<=4:
    bonus_rate=10
bonus=salary*bonus_rate/100

#Display employee last name and bonus
print ("Last Name:",last_name)
print ("Bonus: $",bonus)
