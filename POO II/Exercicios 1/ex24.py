n = int(input())

if n >= 1:
    dia = n
    mes = 'Janeiro'
if n > 31:
    dia = n - 31
    mes = 'Fevereiro'
if n > 59:
    dia = n - 59
    mes = 'Março'
if n > 90:
    dia = n - 90
    mes = 'Abril'
if n > 120:
    dia = n - 120
    mes = 'Maio'
if n > 151:
    dia = n - 151
    mes = 'Junho'
if n > 181:
    dia = n - 181
    mes = 'Julho'
if n > 212:
    dia = n - 212
    mes = 'Agosto'
if n > 243:
    dia = n - 243
    mes = 'Setembro'
if n > 273:
    dia = n - 273
    mes = 'Outubro'
if n > 304:
    dia = n - 304
    mes = 'Novembro'
if n > 334:
    dia = n - 334
    mes = 'Dezembro'

if (n-1) % 7 == 0:
    dia_semana = 'Quinta-feira'
if (n-1) % 7 == 1:
    dia_semana = 'Sexta-feira'
if (n-1) % 7 == 2:
    dia_semana = 'Sábado'
if (n-1) % 7 == 3:
    dia_semana = 'Domingo'
if (n-1) % 7 == 4:
    dia_semana = 'Segunda-feira'
if (n-1) % 7 == 5:
    dia_semana = 'Terça-feira'
if (n-1) % 7 == 6:
    dia_semana = 'Quarta-feira'

print('%s, %d de %s de 2015' % (dia_semana,dia,mes))