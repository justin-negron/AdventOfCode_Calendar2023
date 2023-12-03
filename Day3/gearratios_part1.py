import re

with open("input.txt") as file:
  lines = [line.split() for line in file]

regex = re.compile(r"\d+")

partNumSum = 0

for i in range(len(lines)):
  # check only row below
  if i == 0:
    currNum = ""
    nextToSymbol = False
    for j in range(len(lines[i][0])):
      #print(lines[i][0][j])
      
      if lines[i][0][j].isdigit():
        currNum += lines[i][0][j]

        if len(currNum) == 1:
          # check left side of number
          if lines[i+1][0][j] != "." or lines[i][0][j-1] != "." or lines[i+1][0][j-1] != ".":
            nextToSymbol = True
        
        if j+1 > len(lines[i][0])-1:
          # check just above an below current index
          if lines[i+1][0][j] != ".":
            nextToSymbol = True

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
          else:
            print("Not near symbol: ", currNum)

          currNum = ""
          nextToSymbol = False
        
        elif not lines[i][0][j+1].isdigit():
          # check right side of number
          if lines[i+1][0][j] != "." or lines[i][0][j+1] != "." or lines[i+1][0][j+1] != ".":
            nextToSymbol = True

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
          else:
            print("Not near symbol: ", currNum)
  
          currNum = ""
          nextToSymbol = False
        else:
          # check just above an below current index
          if lines[i+1][0][j] != ".":
            nextToSymbol = True
      else:
        currNum = ""
        nextToSymbol = False

  # check only row above
  elif i == len(lines)-1:
    currNum = ""
    nextToSymbol = False
    for j in range(len(lines[i][0])):
      #print(lines[i][0][j])
      
      if lines[i][0][j].isdigit():
        currNum += lines[i][0][j]

        if len(currNum) == 1:
          # check left side of number
          if lines[i-1][0][j] != "." or lines[i-1][0][j-1] != "." or lines[i][0][j-1] != ".":
            nextToSymbol = True

        if j+1 > len(lines[i][0])-1:
          # check just above an below current index
          if lines[i-1][0][j] != ".":
            nextToSymbol = True

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
          else:
            print("Not near symbol: ", currNum)

          currNum = ""
          nextToSymbol = False
        
        elif not lines[i][0][j+1].isdigit():
          # check right side of number
          if lines[i-1][0][j] != "." or lines[i-1][0][j+1] != "." or lines[i][0][j+1] != ".":
            nextToSymbol = True

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
          else:
            print("Not near symbol: ", currNum)
  
          currNum = ""
          nextToSymbol = False

        else:
          # check just above an below current index
          if lines[i-1][0][j] != ".":
            nextToSymbol = True
      else:
        currNum = ""
        nextToSymbol = False 
    
  # check rows above and below
  else:
    # matchAbove = regex.findall(lines[i-1][0])
    # matchCurr = regex.findall(lines[i][0])
    # matchBelow = regex.findall(lines[i+1][0])
    # print()
    # print(lines[i-1][0])
    # print(lines[i][0])
    # print(lines[i+1][0])
    # print()

    currNum = ""
    nextToSymbol = False
    for j in range(len(lines[i][0])):
      #print(lines[i][0][j])
      
      if lines[i][0][j].isdigit():
        currNum += lines[i][0][j]
        print(currNum)

        if len(currNum) == 1:
          # check left side of number
          if lines[i-1][0][j] != "." or lines[i+1][0][j] != "." or lines[i-1][0][j-1] != "." or lines[i][0][j-1] != "." or lines[i+1][0][j-1] != ".":
            nextToSymbol = True
        
        if j+1 > len(lines[i][0])-1:
          # check just above an below current index
          if lines[i-1][0][j] != "." or lines[i+1][0][j] != ".":
            nextToSymbol = True

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
          else:
            print("Not near symbol: ", currNum)

          currNum = ""
          nextToSymbol = False
        
        elif not lines[i][0][j+1].isdigit():
          # check right side of number
          if lines[i-1][0][j] != "." or lines[i+1][0][j] != "." or lines[i-1][0][j+1] != "." or lines[i][0][j+1] != "." or lines[i+1][0][j+1] != ".":
            nextToSymbol = True

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
          else:
            print("Not near symbol: ", currNum)
  
          currNum = ""
          nextToSymbol = False
    
        else:
          # check just above an below current index
          if lines[i-1][0][j] != "." or lines[i+1][0][j] != ".":
            nextToSymbol = True
      else:
        currNum = ""
        nextToSymbol = False

print("Sum of part numbers: ", partNumSum)
