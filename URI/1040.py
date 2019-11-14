
notas = input().split(" ")
soma = 0
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) /10



if float("%0.1f"%media) >= 7.0:
    print("Media: %0.1f"%media)
    print("Aluno aprovado.")
elif float("%0.1f"%media) < 5.0:
    print("Media: %0.1f"%media)
    print("Aluno reprovado.")
else:
    print("Media: %0.1f"%media)
    print("Aluno em exame.")
    nota = float(input())
    print("Nota do exame:", nota)
    exame = (media + nota) /2
    if float("%0.1f"%exame) >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %0.1f"%exame)
    elif float("%0.1f"%exame) <= 4.9:
        print("Aluno reprovado.")
        print("Media final: %0.1f"%exame)
        


