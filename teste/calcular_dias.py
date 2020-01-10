from datetime import date, timedelta


def QuantosDiasFaltam(ano, mes, dia, quantosDias):
    hoje = date.today()
    dataProcurada = date(ano, mes, dia)
    delta = timedelta(days=quantosDias)
    quandotermina = dataProcurada + delta
    quantosDiasParaTerminar = hoje - quandotermina

    mensagemRetorno = "Faltam " + str(quantosDiasParaTerminar).replace("days, 0:00:00",
                                                                       "") + " dias para a data " + quandotermina.strftime(
        "%d/%m/%y")

    print(mensagemRetorno)


QuantosDiasFaltam(2019, 12, 2, 100)
