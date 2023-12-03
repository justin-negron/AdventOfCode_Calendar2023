import re

with open("input.txt") as file:
  lines = file.readlines()

regex = re.compile(r"\d+")

gameSum = 0

redMax = 12
greenMax = 13
blueMax = 14
for line in lines:
  gameNum = line.split(":")[0]
  subsets = line.split(":")[1].split(";")

  #print(gameNum)
  
  red = True
  green = True
  blue = True
  for i in range(len(subsets)):
    subset = subsets[i].split(",")
    for j in range(len(subset)):
      #print(subset[j])
      match = regex.findall(subset[j])
      if "red" in subset[j]:
        if int(match[0]) > redMax:
          red = False
      if "green" in subset[j]:
        if int(match[0]) > greenMax:
          green = False
      if "blue" in subset[j]:
        if int(match[0]) > blueMax:
          blue = False
    #print(red, green, blue)

  if red and green and blue:
    gameSum = gameSum + int(regex.findall(gameNum)[0])

print("Total gamesum: ", gameSum)



# redMax = 12
# greenMax = 13
# blueMax = 14
# for line in lines:
#   gameNum = line.split(":")[0]
#   subsets = line.split(":")[1].split(";")

#   print(gameNum)
  
#   red = 0
#   green = 0
#   blue = 0
#   for i in range(len(subsets)):
#     subset = subsets[i].split(",")
#     for j in range(len(subset)):
#       print(subset[j])
#       match = regex.findall(subset[j])
#       if "red" in subset[j]:
#         red = red + int(match[0])
#       if "green" in subset[j]:
#         green = green + int(match[0])
#       if "blue" in subset[j]:
#         blue = blue + int(match[0])  
#     #print(red, green, blue)

#   if red <= redMax and green <= greenMax and blue <= blueMax:
#     gameSum = gameSum + int(regex.findall(gameNum)[0])

# print("Total gamesum: ", gameSum)