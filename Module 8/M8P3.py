#Iana Vasileva  CIS160 B65   M8P3    10/21/26
#Open file
file=open("M8P3.txt","r")
total_bonus = 0
last_name=file.readline().strip()

print(f"{"Last Name":<15}{"Salary":<15}{"Bonus":<15}")

while last_name !="":
    salary=float(file.readline().strip())

#Determine bonus rate
    if salary>=100000:
        bonus_rate=.2
    elif salary>=50000:
        bonus_rate=.15
    else:
        bonus_rate=.1

#Compute bonus
    bonus=salary*bonus_rate
    total_bonus+=bonus

    # Display: employee’s last name, salary and bonus. After the loop display the sum of all bonuses paid out.
    print(f"{last_name:<15}${salary:<15.2f}${bonus:<15.2f}")

    last_name=file.readline().strip()
# close file
file.close()

print(f"Total bonus paid: ${total_bonus:.2f}")


