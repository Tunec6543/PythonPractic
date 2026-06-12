numbers = input("Водные данные: ").split(",")
numbers = [x.strip() for x in numbers]
print("Список:", numbers)
print("Кортеж:", tuple(numbers))