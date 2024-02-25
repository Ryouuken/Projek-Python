print("\nProgram Konversi Temperatur\n")

#Celcius
celcius = float(input("masukan suhu dalam celcius: "))

print("Suhu adalah : ", celcius, "Celcius")

#Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah :", reamur, "Reamur")


#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah :", fahrenheit, "Fahrenheit")

#Kelvin
kelvin =  celcius + 273
print("Suhu dalam kelvin adalah :", kelvin, "Kelvin")

#Tugas Perubahan Suhu
## fahrenheit ke kelvin
fahrenheit = float(input('Masukkan Suhu dalam Fahrenheit: '))
celcius = ((5/9) * fahrenheit) - 32
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin)

## kelvin ke fahrenheit
kelvin = float(input("Masukan Suhu Dalam Kelvin: "))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah :",fahrenheit, "Fahrenheit" )