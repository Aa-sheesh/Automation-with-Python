items = []
print(
    "Enter the things that you want to buy separated by commas and write 'done' when you are done"
)
while True:
    user_input = input()
    if user_input.lower() == "done":
        print("Thank you for shopping with us")
        break
    items.extend(user_input.split(","))
print("Bill".center(30, "="))
for item in items:
    print(item.strip().center(30, "-"))
print("Total Items: ", len(items))
print("Thank you for shopping with us.")
print("x".center(30, "-"))
