import re

with open("input.txt") as file:
  lines = file.readlines()

regex = re.compile(r"\d")
sum = 0

count = 1
for line in lines:
  match = regex.findall(line)
  if len(match) > 1:
    sum += int(match[0]+match[len(match)-1])
  else:
    sum += int(match[0]+match[0])
  
print("Total sum: ", sum)
