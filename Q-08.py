
# Count digit in a number.
# Example:  jab bhi number ko 10 se divide karenge to last digit remove ho jayega. 
#            or last digit ko count kar sakte hai.
# 567 // 10 = 56
# 56  // 10 = 5
# 5   // 10 = 0

num = int(input("Enter a number: "))
count = 0
while num != 0:
    num = num // 10
    count += 1
print("Number of digits:", count)