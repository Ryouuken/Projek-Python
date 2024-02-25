from tabulate import tabulate

from math import sqrt

class Membership:

    # inisialisasi data
    data = {
        "Sumbul":"Platinum",
        "Ana":"Gold",
        "Cahya":"Platinum"
    }

    # inisialisai attribute
    def __init__(self, username):
        self.username = username

    # method untuk menampilkan benefit membership
    def show_benefit(self):
        tables = [
            ["Platinum", "15%", "Benefit Gold + Silver + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
            ["Silver", "8%", "Voucher Makanan"],
        ]

        headers = ["Membership", "Discount", "Another Benefit"]

        print("Benefit Membership PacCommerce")
        print("")
        print(tabulate(tables, headers, tablefmt='github', stralign="center"))
        
    # method untuk menampilkan requirements membership
    def show_requirement(self):
        tables = [
            ["Platinum", 8, 15],
            ["Gold", 6, 10],
            ["Silver", 5, 7]
        ]

        headers = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]

        print("Requirements Membership PacCommerce")
        print("")
        print(tabulate(tables, headers, tablefmt='github', numalign="center"))

    # Method untuk melakukan perdiksi membership
    # menggunakan euclidean distance   
    def predict_membership(self, username, monthly_expense, monthly_income):

        res = []

        membership_parameter = [[8,15], [6,10], [5,7]]

        for index, _ in enumerate(membership_parameter):
            tmp = round(sqrt((monthly_expense - membership_parameter[index][0])**2 + (monthly_income - membership_parameter[index][1])**2),2)

            res.append(tmp)

        res_dict = {
            "Platinum":res[0],
            "Gold":res[1],
            "Silver":res[2]
        }

        print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {res_dict}")

        for member, distance in res_dict.items():
            if distance == min(res):
                self.data[username] = member
                return member
            
        # method untuk menampilkan membership yang dimiliki
        # dari database yang dimiliki

    def show_membership(self, username):
        if username in self.data:
            return self.data.get(username)
            
        # Method untuk menghitung final price berdasarkan membership
    def calculate_price(self, username, list_harga):

        try:
            if username in self.data:
                membership = self.data.get(username)
                if membership == "Platinum":
                    total_harga = sum(list_harga) - (sum(list_harga) * 0.15)
                    return total_harga
                elif membership == "Gold":
                    total_harga = sum(list_harga) - (sum(list_harga) * 0.10)
                    return total_harga
                elif membership == "Silver":
                    total_harga = sum(list_harga) - (sum(list_harga) * 0.08)
                    return total_harga
                else:
                    raise Exception("Membership doesn't exist")
            else:
                raise Exception("Membership tidak ada di database")
        except:
            raise Exception("Invalid Process")
            

# Membuat instance
user_1 = Membership("Shandy")

# Mengecek data yang ada
print(user_1.data)

# melihat membership yang ada
print(user_1.show_benefit())

# melihat requirement
print(user_1.show_requirement())

# Melihat hasil perhitungan Euclidean Distance user 1
print(user_1.predict_membership(user_1.username, 9, 12))

#menampilkan data yang baru
print(user_1.data)

#Tampilkan membership berdasarkan username
print(user_1.show_membership(user_1.username))

# list barang yang harus dihitung
print(user_1.calculate_price(user_1.username, [150000, 200000, 400000]))

# case lain dengan member yang sudah ada
user_ana = Membership("Ana")


print(user_ana.data)

print(user_ana.calculate_price(user_ana.username, [150000, 200000, 400000]))

# case lain dengan user bambang
user_bambang = Membership("Bambang")

print(user_bambang.predict_membership(user_bambang.username, 3, 4))

print(user_bambang.show_membership(user_bambang.username))

print(user_bambang.calculate_price(user_bambang.username, [300000, 150000, 1250000, 15000]))