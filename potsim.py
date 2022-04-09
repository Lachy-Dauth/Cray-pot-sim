money = 0
boats = 1
pots = 10
potsIn = 0
potsOut = 10
auto = False

def pick():
  global potsIn
  global potsOut
  print("you have ", pots, " pots")
  potsIn = int(input("How many pots in... "))
  potsOut = int(input("How many pots out... "))

def buy():
  global money
  global boats
  global pots
  global potsIn
  global potsOut
  buy = True
  while buy:
    buy = False
    while pots < boats*10:
      if money >= 5:
        pots += 1
        money -= 5
        buy = True
      else:
        break
    if money >= 100:
      boats += 1
      money -= 100
      buy = True
    if buy == False and pots+10 < boats*10:
      boats -= 1
      money += 80
      buy = True

def newTurn(weather, mult = 1):
  global money
  global pots
  global potsIn
  global potsOut
  if weather[0].lower() == "g":
    money += potsIn*2*mult
    money += potsOut*8*mult
    buy()
    potsOut = pots
    potsIn = 0
    if not auto:
      pick()
  elif weather[0].lower() == "q":
    quit()
  else:
    money += potsIn*4*mult
    pots -= potsOut*mult
    buy()
    potsIn = pots
    potsOut = 0
    if not auto:
      pick()
  print("money: ", money, "\nboats: ", boats, "\npots: ", pots)

def start(weather, pick):
  global potsIn
  global potsOut
  global auto
  if pick[0].lower() == "a":
    auto = True
  if weather[0].lower() == "g":
    potsOut = pots
    potsIn = 0
  else: 
    potsIn = pots
    potsOut = 0
start(input("starting weather (G)ood or (B)ad... "), input("do you want to pick if the pots in and out (A)uto or (M)anual... "))

round = 0
while True:
  newTurn(input("weather (G)ood or (B)ad or (Q)uit... "))
  round += 1
  print("round: ", round)