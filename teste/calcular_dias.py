from datetime import date, timedelta


def QuantosDiasFaltamDuo(diasFeitos):
    hoje = date.today()
    ano = 365
    diasFaltantes = ano - diasFeitos
    delta = timedelta(days=diasFaltantes)
    resultado = hoje + delta
    print('Faltam:', diasFaltantes, 'dias, vai acabar no dia: ', resultado.strftime("%d/%m/%y"))

def QuantosDiasFaltam(ano, mes, dia, quantosDias):
    hoje = date.today()
    dataProcurada = date(ano, mes, dia)
    delta = timedelta(days=quantosDias)
    quandotermina = dataProcurada + delta
    quantosDiasParaTerminar = quandotermina - hoje
    jaForam = delta - quantosDiasParaTerminar
    mensagemRetorno = "Faltam " + str(quantosDiasParaTerminar).replace("days, 0:00:00",
                                                                       "") + "dias para terminar, termina no dia " + quandotermina.strftime(
        "%d/%m/%y") + " Já foram " + str(jaForam).replace("days, 0:00:00", "" )

    print(mensagemRetorno)


QuantosDiasFaltam(2019, 12, 2, 100)

QuantosDiasFaltamDuo(345)