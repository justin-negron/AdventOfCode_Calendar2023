with open("input.txt", "r") as file:
  lines = file.readlines()

totalPoints = 0

for line in lines:
  cardNum = line.split(":")[0]
  winningNum = line.split(":")[1].split("|")[0].split(" ")
  availableNum = line.split(":")[1].strip().split("|")[1].split(" ")
  availableNum.remove("")
  match = 0
  #print(availableNum)
  for num in winningNum:
    #print(num)
    if num: 
      if num in availableNum:
        #print(num, match)
        if match == 0:
          match = 1
        else:
          match = match * 2

  #print(cardNum, match)
  totalPoints += match

  

print("Total points: ", totalPoints)