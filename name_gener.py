import re

for i in range(1000):
    print("buJoghBergward" + str(i))
    if i > 99:
        continue
    print("buJoghBergward" + str(i).zfill(3))

f = open("gefunden3.txt", "r")
f2 = open("nums.txt")
nums = f2.readlines()
f2.close()
lines = f.readlines()
f.close()
pattern = r".*login: [0-9]{1,5}.*"
for line in lines:
    if re.match(pattern, line):
        number = re.search(pattern, line)
        if nums.__contains__(number):
            nums.remove(number)

print(nums)
