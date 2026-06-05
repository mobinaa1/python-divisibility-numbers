five_list =[]
ten_list =[]
twenty_list =[]
thirty_list =[]

start =int(input("enter start number:"))
stop =int(input("enter stop number:"))
step =int(input("enter step number:"))

for i in range(start,stop,step):
    if i %5 ==0:
        five_list.append(i)
    if i % 10 ==0:
        ten_list.append(i)
    if i %20 ==0:
        twenty_list.append(i)
    if i %30 ==0:
        thirty_list.append(i)

print("five_list:",five_list)
print("ten_list:",ten_list)
print("twenty_list:",twenty_list)
print("thirty_list:",thirty_list)
