import string, secrets
from dotenv import load_dotenv, set_key

ENV_PATH = '.env.example'

def save_password_to_env(service_name, password):
    key_name = f"{service_name.upper()}_PASSWORD"
    set_key(ENV_PATH, key_name, password)
    print(f"Пароль успешно сохранен под ключом {key_name}!")

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
save_password_to_env("last_generated", pwd)