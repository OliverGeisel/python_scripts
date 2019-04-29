import re

f = open("YOUR_RESULTS.TXT", "r")
lines = f.readlines()
f.close()

f2 = open("LIST_OF_NUMS.TXT","r")
nums = f2.readlines()
f2.close()
for i in range(len(nums)):
	nums[i]=nums[i].rstrip()

pattern = r".*login: ([0-9]{1,5}).*"
i=0
for line in lines:
    if i%100==0:
	print("At number "+str(i))
    if re.match(pattern, line):
        number = re.search(pattern, line).group(1).rstrip()
        if nums.__contains__(number):
            nums.remove(number)
	    #print("Die Loesung ist "+ str(number))
	    #break
    i+=1
print(nums)
