ntumalunoum=float(input("Insira a nota obtida aqui: "))
ntdoisalunoum=float(input("Insira a nota obtida aqui: "))
media=(ntumalunoum+ntdoisalunoum)/2
if media >= 9:
    print("A")
elif media>=7.5:
    print("B")
elif media == 7:
    print("C")
else:
    print ("D")
