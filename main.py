import random
from asyncio import sleep

# Список персонажей
characters = [
    {
        "name": "Traveler",
        "element": "Anemo",
        "weapon": "Sword",
        "health": 100,
        "attack": 40,
        "dialogues": [
            "Этот мир так прекрасен!",
            "Приключения ждут нас впереди!",
            "Мы сможем преодолеть любые трудности!"
        ]
    },
    {
        "name": "Amber",
        "element": "Pyro",
        "weapon": "Bow",
        "health": 80,
        "attack": 35,
        "dialogues": [
            "Помощь всегда придет!",
            "Дайте мне лук, и я покажу вам свою меткость!",
            "Вместе мы сможем победить любого врага!"
        ]
    },
    {
        "name": "Lisa",
        "element": "Electro",
        "weapon": "Catalyst",
        "health": 90,
        "attack": 30,
        "dialogues": [
            "Знание - источник силы.",
            "Моя магия поможет нам в битвах!",
            "Пусть молния обрушится на наших врагов!"
        ]
    },
    {
        "name": "Kaeya",
        "element": "Cryo",
        "weapon": "Sword",
        "health": 85,
        "attack": 38,
        "dialogues": [
            "Спокойствие - ключ к победе.",
            "Мое оружие пронзит сердца врагов!",
            "Следуйте за мной, и мы достигнем успеха!"
        ]
    }
]

# Список монстров
monsters = [
    {
        "name": "Слеза анемо",
        "health": 200,
        "attack": 30
    },
    {
        "name": "Огненный скорпион",
        "health": 180,
        "attack": 35
    },
    {
        "name": "Электро-птица",
        "health": 220,
        "attack": 28
    },
    {
        "name": "Ледяная голем",
        "health": 250,
        "attack": 32
    }
]

# Словарь инвентаря
inventory = {
    "Меч": 1,
    "Лук": 1,
    "Катализатор": 1,
    "Артефакт доблести": 0,
    "Артефакт силы": 0,
    "Артефакт мудрости": 0
}

# Функция для атаки монстра
def battle(Pl=None):
    # Код для выполнения битвы в "Genshin Impact"
    xp = 1000  # Количество опыта, которое получает персонаж после битвы
    Pl.Xp += xp

    # Здесь вы можете добавить код для проверки условия повышения уровня и вызова функции LevelUp()
    if Pl.Xp >= 1000:
        LevelUp()

    # После битвы продолжайте выполнение остальной части программы

# Функция для повышения уровня
def LevelUp(Pl=None, WolfsGravestone=None):
    case = {
        1000: "Повышение урона",
        2000: "Больше монет с монстров",
        3000: "Повышение урона от огня",
        4000: "Повышение урона от теневой магии"
    }

    for xp, upgrade in case.items():
        if Pl.Xp >= xp:
            Pl.Level += 1
            print("Поздравляем, вы достигли", Pl.Level, "Уровня!")
            print("Выберите улучшение:")
            print("1) Повышение урона")
            print("2) Больше монет с монстров")
            print("3) Повышение урона от огня")
            print("4) Повышение урона от теневой магии")
            choice = input("Введите номер улучшения: ")

            if choice == "1":
                Pl.Damage += 2
                print("Урон увеличен на 2 единицы, теперь у вас", Pl.Damage, "урона!")
                sleep(0.2)
                return True
            elif choice == "2":
                Pl.PlusMonsterCoinDrop += 1
                print("Дроп увеличен!")
                sleep(0.2)
                return True
            elif choice == "3":
                WolfsGravestone.FireDamage += 2
                print("Урон от огня увеличен!")
                sleep(0.2)
                return True
            elif choice == "4":
                WolfsGravestone.CorruptionDamage += 2
            print("Урон от теневой магии увеличен!")
        sleep(0.2)
        return True
    else:
        print("Вы выбрали что-то не то!")
        print()
        return False

        xp = Pl.Xp
        xp = random.randint(999, 1000)
        loot = random.randint(1, 50) * Pl.Level
        Pl.Coins += loot
        Pl.Xp += xp
        print("Тебе удалось одолеть монстра, за что ты получил", loot, "монет, и", xp, "опыта")
        print()

# Функция для отображения инвентаря
def show_inventory():
    print("Инвентарь:")
    for item, count in inventory.items():
        print(f"{item}: {count}")
    print()

# Функция для сохранения инвентаря
import json

def save_inventory_json():
     with open("inventory.json", "w") as file:
         json.dump(inventory, file)
     print("Инвентарь сохранен в формате JSON!")
     
import csv

def save_inventory_csv():
    with open("inventory.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Count"])  # Записываем заголовки столбцов
        for item, count in inventory.items():
            writer.writerow([item, count])
    print("Инвентарь сохранен в формате CSV!")


# Функция для загрузки инвентаря
def load_inventory():
    try:
        with open("inventory.json", "inventory.csv" "r") as file:
            for line in file:
                item, count = line.strip().split(": ")
                inventory[item] = int(count)
    except FileNotFoundError:
        print("Инвентарь не найден. Создан новый инвентарь.")

# Функция для получения случайного предмета из сундука
def open_chest():
    print("Открываем сундук...")
    items = [
        "Артефакт доблести",
        "Артефакт силы",
        "Артефакт мудрости",
        "Меч",
        "Лук",
        "Катализатор"
    ]
    item = random.choice(items)
    inventory[item] += 1
    print(f"Вы получили предмет: {item}")
    print()

# Функция для разговора персонажей
def talk_to_character(character):
    dialogue = random.choice(character["dialogues"])
    print(f"{character['name']}: {dialogue}")
    print()

# Функция для запуска игры
def play_game():
    print("Добро пожаловать в игру \"Геншин Импакт\"!")
    print()

    load_inventory()

    selected_character = None
    for character in characters:
        print(f"{character['name']}: Элемент - {character['element']}, Оружие - {character['weapon']}")
    print()

    while selected_character is None:
        character_name = input("Выберите персонажа: ")
        for character in characters:
            if character_name.lower() == character['name'].lower():
                selected_character = character
        if selected_character is None:
            print("Такого персонажа не существует. Повторите выбор.")

    print(f"Вы выбрали персонажа: {selected_character['name']}")
    print(f"Ваше здоровье: {selected_character['health']}")
    print()

    while True:
        selected_action = None
        while selected_action is None:
            print("Доступные действия:")
            print("1. Атаковать монстра")
            print("2. Посмотреть инвентарь")
            print("3. Открыть сундук")
            print("4. Поговорить с персонажем")
            print("5. Сохранить инвентарь")
            print("6. Выход из игры")

            action = input("Выберите действие: ")
            if action == "1":
                selected_action = "attack"
            elif action == "2":
                selected_action = "inventory"
            elif action == "3":
                selected_action = "open_chest"
            elif action == "4":
                selected_action = "talk"
            elif action == "5":
                selected_action = "save"
            elif action == "6":
                selected_action = "exit"
            else:
                print("Некорректный выбор. Повторите попытку.")
            print()

        if selected_action == "attack":
            selected_monster = random.choice(monsters)
            print(f"Ваш персонаж атакует монстра {selected_monster['name']}!")
            if selected_monster['health'] <= 0:
                print(f"Поздравляем! Вы победили монстра {selected_monster['name']}!")
                print()
        elif selected_action == "inventory":
            show_inventory()
        elif selected_action == "open_chest":
            open_chest()
        elif selected_action == "talk":
            talk_to_character(selected_character)
        elif selected_action == "savejson":
            save_inventory_json()
        elif selected_action == "savecsv":
            save_inventory_csv()
        elif selected_action == "exit":
            print("Спасибо за игру! До новых встреч!")
            break

play_game()