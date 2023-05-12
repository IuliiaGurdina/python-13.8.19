tickets = int(input("При покупке от 4 билетов действует скидка 10% от заказа!\n""Введите количество приобретаемых билетов:"))
price = 0
for i in range(0, tickets):
    age = int(input(f"Введите возраст посетителя: №{i + 1}:\n"))
    if age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    else:
        price += 1390
if tickets > 3:
    discount = price * 0.9
    print("Стоимость всех билетов со скидкой:", discount, "рублей")
else:
     print("Стоимость всех билетов:", price, "рублей")






