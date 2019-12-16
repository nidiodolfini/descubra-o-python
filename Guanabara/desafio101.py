from datetime import date, datetime


def voto(anoNascimento):
    idade = datetime.now().year - anoNascimento
    print(idade)
    if idade <= 65:
        return f"com {idade}: voto obrigatório"
    if idade < 18:
        return f"com {idade}: não é possivel votar"
    else:
        return f"com {idade}: voto é opcinal"


print(voto(1986))
print(voto(1910))
print(voto(2008))
