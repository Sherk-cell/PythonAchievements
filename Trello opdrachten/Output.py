>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>>
>>> print('Mijn naam is <Byron>')
Mijn naam is <Byron>
>>> naam = '<Byron>'
>>> print(naam)
<Byron>
>>> print(naam.upper())
<BYRON>
>>> print(naam[0:2])
<B
>>> print(naam[::-1])
>noryB<
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo <Byron> ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>>
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar = leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print('Je bent precies ' + str(leeftijd) + ' jaar')
...
Over 2 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
768
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
408
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 408
>>>
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-16 11:43:06.053545
>>> datum.strftime('%A %d %B %Y')
'Wednesday 16 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 16 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 16 settembre 2020'