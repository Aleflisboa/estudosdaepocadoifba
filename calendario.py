import holidays
import calendar
from datetime import date

hoje = date.today()
ano = hoje.year
mes = hoje.month

feriados = holidays.country_holidays("BR", years=2026)
cal = calendar.Calendar()


valores_do_dia = {
    0:13.3,
    1:13.3,
    2:13.3,
    3:13.3,
    4:13.3
}

def dias_do_mes(ano, mes):
    dias_mes = [
        dt for dt in cal.itermonthdates(ano, mes)
        if dt.month == mes
        and dt not in feriados
        and dt.weekday() in valores_do_dia
    ]

    total = 0

    for dia in dias_mes:
        
        indice_do_dia = dia.weekday()

        valor_do_dia = valores_do_dia[indice_do_dia]

        total += valor_do_dia


    print(f"\nTotal: R$ {total:.2f}")

    return total

dias_do_mes (ano, mes)


#print(feriados["2026-09-01":"2026-09-30"])