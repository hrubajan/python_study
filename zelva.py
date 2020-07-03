from turtle import forward, backward, left, right, exitonclick, penup, pendown, shape
shape('turtle')

# hexagon*6 = medova plastev
for _ in range(6):
  for _ in range(6):
    forward(100)
    left(60)
  forward(100)
  right(60)
exitonclick()

""" # hexagon
for i in range(6):
  forward(100)
  left(60)
exitonclick() """

""" # schody
for i in range(5):
  forward(50)
  left(90)
  forward(50)
  right(90)
exitonclick() """

""" # prerusovana cara
for i in range(20):
  forward(i) # ruzna delka cary, kdybych chtela stejnou misto i dosadim cislo
  penup()
  forward(5)
  pendown()
exitonclick() """

""" # ctverec pomoci cyklu
for i in range(4):
    forward(50)
    left(90)
exitonclick() """

""" # 3 ctverce s jinym uhlem
for j in range(3):
  for i in range(4):
      forward(50)
      left(90)
  left(20)
exitonclick() """

""" # obdelnik
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)
forward(50)
left(90)
exitonclick() """