def szybkie_sortowanie(lista):
  if len(lista)<2:
    return lista
  else:
    a=lista[0]
    x=[i for i in lista[1:] if i<=a]
    y=[i for i in lista[1:] if i>a]
    return szybkie_sortowanie(x)+[a]+szybkie_sortowanie(y)

print szybkie_sortowanie([20,2,14,1,9])