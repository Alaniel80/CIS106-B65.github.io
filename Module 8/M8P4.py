#Iana Vasileva  CIS160 B65   M8P4    10/21/26
#Open file
file=open("M8P4.txt","r")

#Read item
item=file.readline().strip()

#Define
total_ext_price = 0
count = 0

#Display 1:
print(f"{"Item":<15}{"Quantity":<15}{"Price":<15}{"Extended Price":<15}")

#read next
while item!="":
    quantity=int(file.readline().strip())
    price=float(file.readline().strip())

#Compute extended price and totals
    ext_price=quantity*price
    total_ext_price+=ext_price
    count+=1

#Display 2:
    print(f"{item:<15}{quantity:<15}${price:<15.2f}${ext_price:.2f}")

#read next
    item = file.readline().strip()

#Compute average
average_order=total_ext_price/count

#Close file
file.close()

#Display totals
print(f"Total extended prices: ${total_ext_price:.2f}")
print(f"Number of orders: {count}")
print(f"Average order: ${average_order:.2f}")







