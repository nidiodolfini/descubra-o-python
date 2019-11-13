#hora 3600
#minutos 60


entrada_segundos = int(input())

horas = entrada_segundos // 3600
resto = entrada_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print("{0}:{1}:{2}".format(horas, minutos,segundos))
