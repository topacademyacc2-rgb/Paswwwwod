import string, secrets
exit = 0
chars = ""
print("Выберите компоненты вашего пароля\n")
comps = input("1. Заглавные символы (y/n): ")
if comps == "y":
    chars += string.ascii_uppercase
comps = input("2. Символы нижнего регистра (y/n): ")
if comps == "y":
    chars += string.ascii_lowercase
comps = input("3. Цифры (y/n): ")
if comps == "y":
    chars += string.digits
comps = input("4. Спец-символы (y/n): ")
if comps == "y":
    chars += string.punctuation
while True:
    user_input = input("Длина пароля: ").strip()
    if user_input == "":
        length = 16
        break
    try:
        length = int(user_input)
        if length < 1:
            print("Длина должна быть больше 0")
            continue
        break
    except ValueError:
        print("Введите корректное число")
pwd = ''.join(secrets.choice(chars) for _ in range(length))
print("Пароль: ", pwd)
    