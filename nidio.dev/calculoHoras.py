from datetime import datetime

horaEntrada = 0
horaAlmocoSaida = 0
horaAlmocoEntrada = 0
horaSaida = 0


horaEntrada = datetime.strptime("08:00:00", '%H:%M:%S')
paraHoraDoAlmoco = datetime.strptime("04:00:00", '%H:%M:%S')

print(horaEntrada)

# def calcularHoraAlmoco():
#     paraHoraDoAlmoco = datetime.strptime("04:00:00", '%H:%M:%S')
#     return horaEntrada + paraHoraDoAlmoco
#
#
# print(calcularHoraAlmoco())