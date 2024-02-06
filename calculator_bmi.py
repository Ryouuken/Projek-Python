# Membuat calculator BMI yang digunakan untuk mengetahui berat badan ideal

def calculator_bmi():
    berat_badan = float(input("Masukan berat badan anda (dalam kg) : "))
    tinggi_badan = float(input("Masukan tinggi badan anda (dalam cm) : "))

    bmi = berat_badan / ((tinggi_badan/100) * (tinggi_badan/100))

    print(f"Nilai BMI anda adalah = {bmi}")

    if bmi < 18.5:
        print("Berat badan kurang")
    elif 18.5 <= bmi <= 24.9:
        print("Berat badan normal")
    elif 25 <= bmi <= 29.9:
        print("Berat badan berlebih")
    elif 30 <= bmi <= 34.9:
        print("Obesitas kelas I")
    elif 35 <= bmi <= 39.9:
        print("Obesitas kelas II")
    else:
        print("Obesitas kelas III")

calculator_bmi()

