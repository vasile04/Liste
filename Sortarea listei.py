x=list(eval(input('Introdu lista: ')))
print('Lista 1:', x)
lista2=sorted(x)
print('Lista sortata crescator:', lista2)
lista3=sorted(x, reverse=True)
print('Lista sortata descrescator:', lista3)
y=len(x)
print('Lungimea sirului este:', y)
print('Elementul maxim este:', max(x))
print('Elementul minim este:',  min(x))
print('Lista 1 cu extinderea lui 111:',x+[111])
x[2]=222
print('Lista 1 cu adaugarea lui 222 pe pozitia a 2-a:', x)