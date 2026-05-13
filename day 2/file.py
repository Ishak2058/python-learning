# Student CSV Reader
#First create csv file and Enter data what you want like Name,Product,Price

file = open("students.csv","r")
for line in file:
    parts= line.strip().split(",")

    print("Customer:",parts[0])
    print("Product:",parts[1])
    print("Price:",parts[2])
    print("------")
file.close()