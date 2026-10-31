#Iana Vasileva  CIS160 B65   M10P3  10/30/26
#Define variables
out_price=0
sum_msrp=0
sum_all_sales=0

#Define function to compute the out the door price
def compute_out_price(make,model,electric_code,msrp):
    if make.upper()=="HONDA" and model.upper()=="ACCORD":
        msrp_percent=0.10
    elif make.upper()=="TOYOTA" and model.upper()=="RAV4":
        msrp_percent=0.15
    elif electric_code.upper()=="Y":
        msrp_percent=0.30
    else:
        msrp_percent=0.05

    out_price=msrp*msrp_percent
    new_msrp=msrp-out_price
    sales_tax=new_msrp*.07
    total_price=new_msrp+sales_tax
    return total_price

#Ask user if they want to run the program
repeat=input("Do you want to run this program (Yes or No): ")

#While loop and input from user
while repeat.upper()=="YES":
    make=input("Enter your make: ")
    model=input("Enter your model: ")
    electric_code=input("Enter your electric code (Y or N): ")
    msrp=float(input("Enter your sticker price(MSRP): $"))

#call function
    total_price=compute_out_price(make,model,electric_code,msrp)
    sum_msrp=msrp+sum_msrp
    sum_all_sales=sum_all_sales+total_price

#Display results
    print(f"Out the door price: ${total_price:,.2f}")

# Ask user if they want to run the program
    repeat=input("Do you want to run this program again (Yes or No): ")

#Display sums of MSRP's and all sales
print(f"Sum of all MSRP's: ${sum_msrp:,.2f}")
print(f"Sum of all sales: ${sum_all_sales:,.2f}")