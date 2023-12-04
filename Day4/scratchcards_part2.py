with open("input.txt") as file:
  lines = file.readlines()

totalPoints = 0
totalInstances = 0
index = 0
copyDict = {}
for line in lines:
  cardNum = line.split(":")[0]
  winningNum = line.split(":")[1].split("|")[0].split(" ")
  availableNum = line.split(":")[1].strip().split("|")[1].split(" ")
  availableNum.remove("")
  match = 0
  count = 0
  #print(availableNum)
  for num in winningNum:
    #print(num)
    if num: 
      if num in availableNum:
        count += 1
        if match == 0:
          match = 1
        else:
          match = match * 2
        #print(num, match, count)

  if copyDict.get(index) != None:
    count = count * copyDict.get(index)

  for i in range(count):
    if copyDict.get(index+i+1) != None:
      copyDict[index+i+1] = copyDict.get(index+i+1) + 1
    else:
      copyDict[index+i+1] = 1
    
  #print(copyDict)
  
  #count += copyDict[index]
  #print(cardNum, match)
  # if copyDict.get(index) != None:
  #   print(cardNum ,"copies: ", count, copyDict[index])
  # else:
  #   print(cardNum ,"copies: ", count)
  # print()
  
  totalPoints += match
  if copyDict.get(index) != None:
    totalInstances += match * copyDict.get(index)
  index += 1

  

print("Total points: ", totalInstances)