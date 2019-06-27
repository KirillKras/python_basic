import json
import requests
import datetime
import sqlite3
import pandas as pd
from collections import namedtuple


def get_key():
    with open('app.id', 'r') as f:
        return f.read()


def get_cities():
    df = pd.read_json('city.list.json')
    df.index = df.id
    df = df[['country', 'name']]
    return df


WEATHER_KEY = get_key()
df_cities = get_cities()

def create_table():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather
    (
        city_id integer PRIMARY KEY,
        city varchar(250),
        date DATE,
        temp integer,
        id_weather integer
    )
    ''')
    conn.commit()
    return conn


def select_weather(city_id, now):
    cursor = CONN.cursor()
    date_cal = 2
    cursor.execute(
        '''
            SELECT * FROM weather 
            WHERE city_id = ?
        ''',
        (city_id,))

    result = cursor.fetchall()
    result_exists = len(result)

    if result_exists:
        for row in result:
            if row[date_cal] == str(now):
                return 'exists'
        else:
            return 'update'
    return 'insert'


def insert_weather(city_id, city, temp, weather_id):
    now = datetime.datetime.now().date()
    cursor = CONN.cursor()
    cursor.execute(
        '''
            INSERT INTO weather
            VALUES (?, ?, ?, ?, ?)
        ''',
        (city_id, city, now, temp, weather_id))
    CONN.commit()
    print(
        f'''
          Write to DB: 
              city_id = {city_id}, 
              city = {city}, 
              date = {now}, 
              temp = {temp}, 
              weather_id = {weather_id}
        ''')


def update_weather(city_id, temp):
    cursor = CONN.cursor()
    cursor.execute(
        '''
             UPDATE weather
             SET temp = ?
             WHERE city_id = ?
        ''', (temp, city_id)
    )
    CONN.commit()
    print(
        f'''
          Update DB:  
              city = {city},  
              temp = {temp}
        ''')


def process_weather(city_id, city, temp, weather_id):
    now = datetime.datetime.now().date()
    select_code = select_weather(city_id, now)
    if select_code == 'insert':
        insert_weather(city_id, city, temp, weather_id)
    elif select_code == 'update':
        update_weather(city_id, temp)
    elif select_code == 'exists':
        print('\n\tWeather exists\n')



def find_city_idx(country_code, city_name):
    result = df_cities[(df_cities.country == country_code) & (df_cities.name == city_name)].index
    if len(result):
        return result[0]
    return None


def find_cities_idx(country_code):
    result = df_cities[(df_cities.country == country_code)].name
    if len(result):
        return result.items()
    return None


def get_weather(city_id, city):
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&appid={WEATHER_KEY}")
    result = json.loads(response.text)
    try:
        weather_id = result['weather'][0]['id']
        temp = result['main']['temp']
        process_weather(int(city_id), city, int(weather_id), int(temp))
    except KeyError:
        print('Погода не найдена')


def get_weather_cities(cities_idx):
    for city_id, city in cities_idx:
        get_weather(city_id, city)


CONN = create_table()


enter = ''

while enter != 'e':
    enter = input('Введите "cc" - поиск погоды по страна+город, "c" - поиск погоды по всем городам страны, "e" - завершение работы (англ. раскладка): ')
    if enter == 'cc':
        country = input('Введите код страны: ')
        city = input('Введите название города: ')
        city_id = find_city_idx(country, city)
        get_weather(city_id, city)
    elif enter == 'c':
        country = input('Введите код страны: ')
        cities_idx = find_cities_idx(country)
        get_weather_cities(cities_idx)

CONN.close()