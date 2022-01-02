per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB = 5.6/100
SKB = 5.9/100
VTB = 4.28/100
SBER = 4.0/100

money = int(input('Введите сумму '))

deposit = [TKB*money,SKB*money,VTB*money,SBER*money]


print('Максимальная сумма, которую вы можете заработать -')
print(max(deposit))




