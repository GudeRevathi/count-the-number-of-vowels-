s=input("enter a string:")
count=0
for char in s:
    if char.lower() in "aeiou":
        count=count+1 
    else: 
        pass
print(count)