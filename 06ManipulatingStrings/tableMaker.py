#! python3
# tableMaker.py - Creates a table from a list of strings.
import pyperclip

print("Enter the headers of the table (separated by commas):")
headers = input().split(",")
print("Enter the data for the table (separated by commas):")
data = input().split(",")
answer = []
for i in range(len(headers)):
    answer.append("|" + headers[i] )
answer.append("|")
answer.append("\n")

for i in range(len(data)):
    answer.append("|" + data[i] )
    if (i + 1) % len(headers) == 0:
        answer.append("|")  
        answer.append("\n")
answer = "".join(answer)

print("The table is: ")
print(answer)
pyperclip.copy(answer)
print("The table has been copied to the clipboard.")

