import random

# Membuat list berisi integer dari 1 sampai 150
integer_list = list(range(1, 151))

# Memilih satu nomor secara acak dari list
random_number = random.sample(integer_list, 1)[0]

print("List integer:", integer_list)
print("Nomor acak:", random_number)