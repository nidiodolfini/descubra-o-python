from datetime import date, timedelta


def QuantosDiasFaltam(ano, mes, dia):
    hoje = date.today()
    dataProcurada = date(ano, mes, dia)
    delta = timedelta(days=100)
    quandotermina = dataProcurada + delta
    quantosDias = hoje - quandotermina

    mensagemRetorno = "Faltam " + str(quantosDias).replace("days, 0:00:00",
                                                           "") + " dias para a data " + quandotermina.strftime(
        "%d/%m/%y")

    print(mensagemRetorno)


QuantosDiasFaltam(2019, 12, 2)
