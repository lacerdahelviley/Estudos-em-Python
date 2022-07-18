tipo=input("insira o tipo de combustível: ")
qtd=float(input("insira a quantidade de combustível em litros: "))
if tipo=="alcool" or tipo=="etanol":
    val=1.9*qtd
    if qtd<=20:
        mult=val-(val*0.03)
    else:
        mult=val-(val*0.05)
    print("valor com desconto:",mult)
elif tipo=="gasolina":
    val=2.5*qtd
    if qtd<=20:
        mult=val-(val*0.04)
    else:
        mult=val-(val*0.06)
    print("valor com desconto: ",mult)
else:
    print("Mensagem inválida.")