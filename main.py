# 1) Принять у пользователя 10 чисел и вывести с 2 по 8
nums_10 = []

print("Enter 10 values! ")
for i in range(10):
    num = int(input("Enter values -> "))
    nums_10.append(num)
if len(nums_10) == 10:
    print("Your array", nums_10, "slices betwee 2 and 8 -> ", nums_10[1:8])

# 2) Принять у пользователя размер массива и заполнить его случайными числами от 1 до 10
# 	После чего вывести срез между минимальным и максимальным числом
import random

nums_input_v = []
min_i = -1
max_i = -1
max_v = 0
min_v = 100
len_nums_input_v = abs(int(input("Enter length of array -> ")))
if len_nums_input_v > 0:
    for i in range(len_nums_input_v):
        num_r = random.randrange(1,10)
        nums_input_v.append(num_r)
        if num_r >= max_v:
            max_v = num_r
            max_i = i
        if num_r <= min_v:
            min_v = num_r
            min_i = i
if len(nums_input_v) == len_nums_input_v:
    print("Your array -> ", nums_input_v, "min value -> ", min_v, "index of min value -> ", min_i, "max value -> ", max_v, "index of max value -> ", max_i )
    if min_i > max_i:
        min_i, max_i = max_i, min_i
    print("Slice from min to max values -> ", nums_input_v[min_i:max_i + 1])
else:
    print("Check length of array!")

# # 3) Принять у пользователя название автомобильных марок и проверить, что среди них есть лучшая - Хонда
cars_brands_req = ["Audi", "BMW", "Chevrolet", "Ford", "Honda", "Hyundai", "Jaguar", "Kia", "Lexus", "Mercedes-Benz", "Nissan", "Porsche", "Subaru", "Tesla", "Toyota", "Volkswagen", "Volvo"]
cars_brands = []
len_cars_brands = abs(int(input("How many brands of cars do you want to add? ")))
if len_cars_brands > 0:
    for i in range(len_cars_brands):
        brand = input("Enter brand of car -> ")
        while brand not in cars_brands_req:
            print("Invalid brand of car! Try again!")
            brand = input("Enter brand of car -> ")
            continue
        cars_brands.append(brand)
if len_cars_brands == len(cars_brands):
    print("Brands of cars -> ", cars_brands, "Is Honda in your array?", "Honda" in cars_brands)
else:
    print("Check length of array!")

# 4) Принять у пользователя 5 названий фруктов и проверить, что среди них есть яблоко
fruits_req = ["apple","banana","orange","strawberry","mango","pineapple","watermelon","grapes","kiwi","blueberry","raspberry","lemon","lime","peach","pear","cherry","plum","papaya","avocado","pomegranate","coconut","grapefruit","apricot","fig","guava","melon","cantaloupe","cranberry","blackberry","passion fruit","lychee","dragon fruit","persimmon","nectarine","olive","tangerine","date","jackfruit","kiwifruit","raspberry","boysenberry","elderberry","gooseberry","mulberry","star fruit","quince","plantain","ackee","durian","breadfruit"]
fruits = []

for i in range(5):
    fruit = input("Enter name fruit -> ")
    while fruit not in fruits_req:
        print("Invalid name of fruit! Try again! ")
        fruit = input("Enter name fruit -> ")
        continue
    fruits.append(fruit)
if len(fruits) == 5:
    print("Your array of fruits -> ",fruits, "Is the apple in array of fruits?", "apple" in fruits)
else:
    print("Check length of array!")


# 5) Принять у пользователя 10 чисел в диапазоне [0.1-0.9] и вывести те, что при разнице с 0.2 дают 0
nums_01_09 = []
nums_diff_02 = []
pos_nums_01_09 = []

print("Enter values 10 times! ")
for i in range(10):
    n = abs(float(input("Enter value from 0.1 to 0.9  -> ")))
    while n > 0.9 or n < 0.1:
        print("Invalid value! Try again! Enter value from 0.1 to 0.9 -> ")
        n = abs(float(input("Enter value from 0.1 to 0.9  -> ")))
        continue
    nums_01_09.append(n)
    if n - 0.2 == 0:
        nums_diff_02.append(n)
        pos_nums_01_09.append(i)
if len(nums_01_09) == 10:
    print("Your array -> ", nums_01_09, "vals - 0.2 == 0 -> ", nums_diff_02, "position in array -> ", pos_nums_01_09)
else:
    print("Check length of your arr!")

# 6) Принять у пользователя размер массив
# Заполнить массив случайными в диапазоне [0.1 - 9.9999]
# Вывести количество 2 в любом разряде всех ячеек

import random

amount_n2 = 0
rand_val_01_9 = []
len_rand_val_01_9 = abs(int(input("Enter length of array -> ")))

if len_rand_val_01_9 > 0:
    for i in range(len_rand_val_01_9):
        r_val = round(random.uniform(0.1, 9.9999), 4)
        rand_val_01_9.append(r_val * 10000)

    for random_val_f in rand_val_01_9:
        random_val_int = int(random_val_f)
        while random_val_int:
            is_2 = random_val_int % 10 == 2
            if is_2:
                amount_n2 += 1
            random_val_int = random_val_int // 10
    print("Your array -> ",rand_val_01_9, "and amount of 2 in array -> ",amount_n2, "times" )
