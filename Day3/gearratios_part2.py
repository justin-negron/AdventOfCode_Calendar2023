import re

with open("input.txt") as file:
  lines = [line.split() for line in file]

regex = re.compile(r"\d+")

gearRatios = 0
partNumSum = 0

symbolDict = {}

for i in range(len(lines)):
  # check only row below
  if i == 0:
    currNum = ""
    nextToSymbol = False
    symbolAtIndex = tuple()
    for j in range(len(lines[i][0])):
      #print(lines[i][0][j])
      
      if lines[i][0][j].isdigit():
        currNum += lines[i][0][j]

        if len(currNum) == 1:
          # check left side of number
          if lines[i+1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j]) 
          elif lines[i][0][j-1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i,j-1])
          elif lines[i+1][0][j-1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j-1]) 
        
        if j+1 > len(lines[i][0])-1:
          # check just above an below current index
          if lines[i+1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j]) 

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
            if symbolAtIndex:
              if symbolAtIndex in symbolDict:
                gearRatios += symbolDict.get(symbolAtIndex) * int(currNum)
              else:
                symbolDict[symbolAtIndex] = int(currNum)
          else:
            print("Not near symbol: ", currNum)

          currNum = ""
          nextToSymbol = False
          symbolAtIndex = tuple()
        
        elif not lines[i][0][j+1].isdigit():
          # check right side of number
          if lines[i+1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j]) 
          elif lines[i][0][j+1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i,j+1]) 
             
          elif lines[i+1][0][j+1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j+1]) 

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
            if symbolAtIndex:
              if symbolAtIndex in symbolDict:
                gearRatios += symbolDict.get(symbolAtIndex) * int(currNum)
              else:
                symbolDict[symbolAtIndex] = int(currNum)
          else:
            print("Not near symbol: ", currNum)
  
          currNum = ""
          nextToSymbol = False
          symbolAtIndex = tuple()
        else:
          # check just above an below current index
          if lines[i+1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j]) 
      else:
        currNum = ""
        nextToSymbol = False
        symbolAtIndex = tuple()

  # check only row above
  elif i == len(lines)-1:
    currNum = ""
    nextToSymbol = False
    symbolAtIndex = tuple()
    for j in range(len(lines[i][0])):
      #print(lines[i][0][j])
      
      if lines[i][0][j].isdigit():
        currNum += lines[i][0][j]

        if len(currNum) == 1:
          # check left side of number
          if lines[i-1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j])
          elif lines[i-1][0][j-1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j-1]) 
          elif lines[i][0][j-1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i,j-1]) 

        if j+1 > len(lines[i][0])-1:
          # check just above an below current index
          if lines[i-1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j])

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
            if symbolAtIndex:
              if symbolAtIndex in symbolDict:
                gearRatios += symbolDict.get(symbolAtIndex) * int(currNum)
              else:
                symbolDict[symbolAtIndex] = int(currNum)
          else:
            print("Not near symbol: ", currNum)

          currNum = ""
          nextToSymbol = False
          symbolAtIndex = tuple()
        
        elif not lines[i][0][j+1].isdigit():
          # check right side of number
          if lines[i-1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j]) 
          elif lines[i-1][0][j+1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j+1]) 
          elif lines[i][0][j+1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i,j+1]) 

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
            if symbolAtIndex:
              if symbolAtIndex in symbolDict:
                gearRatios += symbolDict.get(symbolAtIndex) * int(currNum)
              else:
                symbolDict[symbolAtIndex] = int(currNum)
          else:
            print("Not near symbol: ", currNum)
  
          currNum = ""
          nextToSymbol = False
          symbolAtIndex = tuple()

        else:
          # check just above an below current index
          if lines[i-1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j]) 
      else:
        currNum = ""
        nextToSymbol = False 
        symbolAtIndex = tuple()
    
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
    symbolAtIndex = tuple()
    for j in range(len(lines[i][0])):
      #print(lines[i][0][j])
      
      if lines[i][0][j].isdigit():
        currNum += lines[i][0][j]
        #print(currNum)

        if len(currNum) == 1:
          # check left side of number
          if lines[i-1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j])
          elif lines[i+1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j])
          elif lines[i-1][0][j-1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j-1])
          elif lines[i][0][j-1] != ".": 
            nextToSymbol = True
            symbolAtIndex = tuple([i,j-1])
          elif lines[i+1][0][j-1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j-1])
            
        
        if j+1 > len(lines[i][0])-1:
          # check just above an below current index
          if lines[i-1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j])
          elif lines[i+1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j])
          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
            if symbolAtIndex:
              if symbolAtIndex in symbolDict:
                gearRatios += symbolDict.get(symbolAtIndex) * int(currNum)
              else:
                symbolDict[symbolAtIndex] = int(currNum)
          else:
            print("Not near symbol: ", currNum)

          currNum = ""
          nextToSymbol = False
          symbolAtIndex = tuple()
        
        elif not lines[i][0][j+1].isdigit():
          # check right side of number
          if lines[i-1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j])
          elif lines[i+1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j])
          elif lines[i-1][0][j+1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j+1]) 
          elif lines[i][0][j+1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i,j+1]) 
          elif lines[i+1][0][j+1] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j+1]) 

          if nextToSymbol:
            print("Near symbol: ", currNum)
            partNumSum += int(currNum)
            if symbolAtIndex:
              if symbolAtIndex in symbolDict:
                gearRatios += symbolDict.get(symbolAtIndex) * int(currNum)
              else:
                symbolDict[symbolAtIndex] = int(currNum)
          else:
            print("Not near symbol: ", currNum)
  
          currNum = ""
          nextToSymbol = False
          symbolAtIndex = tuple()
    
        else:
          # check just above an below current index
          if lines[i-1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i-1,j]) 
          elif lines[i+1][0][j] != ".":
            nextToSymbol = True
            symbolAtIndex = tuple([i+1,j]) 
      else:
        currNum = ""
        nextToSymbol = False
        symbolAtIndex = tuple()

print("Sum of part numbers: ", partNumSum)
print("Sum of gear ratios: ", gearRatios)
