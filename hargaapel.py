apple_price = 2
money = 10

input_count = input('Mau berapa apel?: ')
count = int(input_count)
total_price = apple_price * count

print('Anda akan membeli ' + str(count) + ' apel')
print('Harga total adalah ' + str(total_price) + ' dolar')

#control flownya
if money > total_price:
    print ('Anda telah membeli ___ apel')
    print ('Dompet Anda kosong')
elif money == total_price:
    print ('Anda telah membeli ___ apel')
    print ('Dompet Anda kosong')
else :
    print ('Uang Anda tidak mencukupi')
    print ('Anda tidak dapat membeli apel sebanyak itu')