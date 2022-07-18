ntum=float(input("insira a nota aqui: "))
ntdois=float(input("insira a nota aqui: "))
media=((ntum+ntdois)/2)
if media==10:
    print("Aprovado com distincao")
elif media>7:
    print("Aprovado")
#elif: é como um subtopico de "if"
elif media==0:
    print("Reprovado, necessario aulas de reforco")
else:
    print("Reprovado")

