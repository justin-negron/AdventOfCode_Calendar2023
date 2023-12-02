import re

with open("input.txt") as file:
  lines = file.readlines()

regex = re.compile(r"\d")
sum = 0

for line in lines:
  line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")

  match = regex.findall(line)
  if len(match) > 1:
    sum += int(match[0]+match[len(match)-1])
  else:
    sum += int(match[0]+match[0])
  
print("Total sum: ", sum)