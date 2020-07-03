import random
soucet = 0 
while soucet < 21:
  print(f'Mas {soucet} bodu')
  odpoved = input('Otocit kartu? ')
  if odpoved == 'ano':
    karta = random.randint(2,10)
    print(f'Otocil/a si {karta}')
    soucet += karta
  elif odpoved == 'ne':
    break
  else:
    print('Nerozumim, odpovidej "ano" nebo "ne"')

if soucet == 21:
  print('Gratuluju! Vyhral/a si!')
elif soucet > 21:
  print(f'Smula {soucet} bodu je moc')
else:
  print(f'Chybelo jen {21-soucet} bodu')
