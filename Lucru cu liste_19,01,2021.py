with open('input.txt', 'r') as f:
    x=list(eval(f.readline()))
lista2=sorted(x)
lista3=sorted(x, reverse=True)
y=len(x)
del(x[2])
x[2]=222
with open('output.txt', 'w') as f:
    f.write(f'Prima lista: {x}  \n')
    f.write(f'Lista sortata crescator: {lista2}   \n')
    f.write(f'Lista sortata in ordine descresctoare: {lista3} \n')
    f.write(f'Lungimea listei initiale este: {y}  \n')
    f.write(f'Elementul maxim este:{ max(x)}  \n')
    f.write(f'Elementul minim este: {min(x)} \n')
    f.write(f'Lista 1 cu adaugarea lui 111:{ x+[111]} \n')
    f.write(f'Lista intai cu adaugarea lui 222 pe pozitia a doua: {x} \n')