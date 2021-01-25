with open ('listaclasei.txt', 'r') as f:
    x=str((f.read()))
print(x)
y=sorted(x.split(','))
print(y)
with open ('listaclaseislectate.txt', 'w') as f:
    f.write(f'Lista clasei selectate in ordine alfabetica: {y} \n')