import os
import asyncio
import aiohttp
from dotenv import load_dotenv
from datetime import datetime
import ssl

# Настройка SSL контекста
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

env_path = os.path.join(os.path.dirname(__file__), 'kluch.env')
load_dotenv(env_path)

api_url_city = 'https://api.api-ninjas.com/v1/city'
api_url_cats = 'https://api.api-ninjas.com/v1/cats'

X_API_KEY = os.getenv('X_API_KEY')
if not X_API_KEY:
    print("ОШИБКА: Ключ API не найден!")
    exit(1)

async def make_async_request(session, url, params=None):
    try:
        async with session.get(
            url,
            headers={'X-Api-Key': X_API_KEY},
            params=params,
            ssl=ssl_context
        ) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Ошибка HTTP {response.status}: {await response.text()}")  
                return None
    except Exception as e:
        print(f"Ошибка запроса к {url}: {str(e)}")
        return None

async def get_cats_async(session):
    print("\nЗагрузка данных о кошках")
    params = {'min_life_expectancy': 1}
    data = await make_async_request(session, api_url_cats, params)
    return data if data else []

async def display_cats_async(cats, current_page, total_pages):
    print(f"\nСтраница кошек {current_page}/{total_pages}")
    
    start_idx = (current_page - 1) * 10
    end_idx = start_idx + 10
    current_cats = cats[start_idx:end_idx]
    
    for idx, cat in enumerate(current_cats, 1):
        print(f"{idx}. {cat.get('name', 'Без имени')}")
        print(f"   Минимальный возраст: {cat.get('min_life_expectancy', 'N/A')} лет")
        print(f"   Максимальный возраст: {cat.get('max_life_expectancy', 'N/A')} лет")
        print(f"   Происхождение: {cat.get('origin', 'Неизвестно')}")
        print("   ---")

def sort_cats(cats, sort_key):
    if sort_key == 'age':
        return sorted(cats, key=lambda x: float(x.get('max_life_expectancy', 0)), reverse=True)
    elif sort_key == 'country':
        return sorted(cats, key=lambda x: x.get('origin', '').lower())
    return cats

async def cats_mode(session):
    cats = await get_cats_async(session)
    if not cats:
        print("Не удалось загрузить данные о кошках")
        return

    print("\nСортировка кошек:")
    print("1) по умолчанию (как от API)")
    print("2) по максимальному возрасту (по убыванию)")
    print("3) по стране происхождения")
    sort_choice = input("Выберите вариант сортировки (1-3): ")
    
    if sort_choice == '2':
        cats = sort_cats(cats, 'age')
    elif sort_choice == '3':
        cats = sort_cats(cats, 'country')
    
    total_pages = (len(cats) + 9) // 10
    current_page = 1

    while True:
        await display_cats_async(cats, current_page, total_pages)

        if current_page == 1 and total_pages > 1:
            nav_choice = input("\n1. Следующая страница\n2. Изменить сортировку\n0. Выход\nВыберите: ")
        elif current_page == total_pages and total_pages > 1:
            nav_choice = input("\n2. Предыдущая страница\n3. Изменить сортировку\n0. Выход\nВыберите: ")
        elif total_pages > 1:
            nav_choice = input("\n1. Следующая\n2. Предыдущая\n3. Изменить сортировку\n0. Выход\nВыберите: ")
        else:
            nav_choice = input("\n2. Изменить сортировку\n0. Выход\nВыберите: ")

        if nav_choice == '0':
            break
        elif nav_choice == '1' and current_page < total_pages:
            current_page += 1
        elif nav_choice == '2' and current_page > 1:
            current_page -= 1
        elif nav_choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nСортировка кошек:")
            print("1) по умолчанию (как от API)")
            print("2) по максимальному возрасту (по убыванию)")
            print("3) по стране происхождения")
            sort_choice = input("Выберите вариант сортировки (1-3): ")
            
            if sort_choice == '2':
                cats = sort_cats(cats, 'age')
            elif sort_choice == '3':
                cats = sort_cats(cats, 'country')
            
            current_page = 1 

        os.system('cls' if os.name == 'nt' else 'clear')

async def get_cities(session, per_page):
    print(f"\nЗагрузка данных о городах (лимит: {per_page})")
    params = {'per_page': per_page}
    data = await make_async_request(session, api_url_city, params)
    return data if data else []

def sort_cities(cities, sort_key):
    if sort_key == '1':
        return sorted(cities, key=lambda x: x.get('population', 0), reverse=True)
    elif sort_key == '2':
        return sorted(cities, key=lambda x: x.get('latitude', 0))
    elif sort_key == '3':
        return sorted(cities, key=lambda x: x.get('name', '').lower())
    return cities

async def display_cities(cities, current_page, total_pages):
    print(f"\nСтраница городов {current_page}/{total_pages}")
    
    start_idx = (current_page - 1) * 10
    end_idx = start_idx + 10
    current_cities = cities[start_idx:end_idx]
    
    for idx, city in enumerate(current_cities, 1):
        print(f"{idx}. {city.get('name', 'Без названия')}")
        print(f"   Страна: {city.get('country', 'N/A')}")
        print(f"   Население: {city.get('population', 'N/A')}")
        print(f"   Широта: {city.get('latitude', 'N/A')}")
        print(f"   Долгота: {city.get('longitude', 'N/A')}")
        print("   ---")

async def city_mode(session):
    while True:
        try:
            per_page = int(input("Введите количество городов для загрузки (1-100): "))
            if 1 <= per_page <= 100:
                break
            print("Пожалуйста, введите число от 1 до 100")
        except ValueError:
            print("Пожалуйста, введите корректное число")

    cities = await get_cities(session, per_page)
    if not cities:
        print("Не удалось загрузить данные о городах")
        return

    print("\nСортировка городов:")
    print("1) По населению (по убыванию)")
    print("2) По широте")
    print("3) По названию")
    sort_choice = input("Выберите вариант сортировки (1-3): ")
    
    cities = sort_cities(cities, sort_choice)
    
    total_pages = (len(cities) + 9) // 10
    current_page = 1

    while True:
        await display_cities(cities, current_page, total_pages)

        if current_page == 1 and total_pages > 1:
            nav_choice = input("\n1. Следующая страница\n2. Изменить сортировку\n0. Выход\nВыберите: ")
        elif current_page == total_pages and total_pages > 1:
            nav_choice = input("\n2. Предыдущая страница\n3. Изменить сортировку\n0. Выход\nВыберите: ")
        elif total_pages > 1:
            nav_choice = input("\n1. Следующая\n2. Предыдущая\n3. Изменить сортировку\n0. Выход\nВыберите: ")
        else:
            nav_choice = input("\n2. Изменить сортировку\n0. Выход\nВыберите: ")

        if nav_choice == '0':
            break
        elif nav_choice == '1' and current_page < total_pages:
            current_page += 1
        elif nav_choice == '2' and current_page > 1:
            current_page -= 1
        elif nav_choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\nСортировка городов:")
            print("1) По населению (по убыванию)")
            print("2) По широте")
            print("3) По названию")
            sort_choice = input("Выберите вариант сортировки (1-3): ")
            cities = sort_cities(cities, sort_choice)
            current_page = 1

        os.system('cls' if os.name == 'nt' else 'clear')

async def main():
    print("1) население")
    print("2) информация о кошках")
    choice = input("Выберите что хотит посмотреть (1-2): ")

    connector = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=connector) as session:
        if choice == '1':
            await city_mode(session)
        elif choice == '2':
            await cats_mode(session)

if __name__ == "__main__":
    asyncio.run(main())
