import re

with open("input.txt") as file:
  lines = file.readlines()

regex = re.compile(r"\d+")

powerSum = 0

for line in lines:
  gameNum = line.split(":")[0]
  subsets = line.split(":")[1].split(";")

  #print(gameNum)
  
  redMax = 0
  greenMax = 0
  blueMax = 0
  for i in range(len(subsets)):
    subset = subsets[i].split(",")
    for j in range(len(subset)):
      #print(subset[j])
      match = regex.findall(subset[j])
      if "red" in subset[j]:
        redMax = max(redMax, int(match[0]))
      if "green" in subset[j]:
        greenMax = max(greenMax, int(match[0]))
      if "blue" in subset[j]:
        blueMax =  max(blueMax, int(match[0]))
    #print(red, green, blue)
  powerSum = powerSum + (redMax * greenMax * blueMax)
  

print("Total powersum: ", powerSum)