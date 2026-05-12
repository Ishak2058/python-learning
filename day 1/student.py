# Simple Python script to display text
import numbers
file = open("../../ishak.txt","r")
total = 0
count = 0

highest = 0
lowest = 99

for line in file:
    number = int(line)

    total = total + number
    count = count + 1
    if number > highest:
        highest = number
    if number < lowest:
        lowest = number
average = total /count


print("Total number of numbers: ", total)
print("Average number of numbers: ", average)
print("Highest number: ", highest)
print("Lowest number: ", lowest)
file.close()
