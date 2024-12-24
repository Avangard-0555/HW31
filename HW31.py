import time
import threading
import asyncio
from typing import Any
from datetime import datetime


# Модель светофора с цветами
class TrafficLight:
    def __init__(self):
        self.state = 'Red'  # Начальный цвет — Красный

    def set_state(self, state: str):
        """Устанавливает текущий цвет светофора"""
        self.state = state
        print(f"{datetime.now()} - Светофор: {self.state}")


# Синхронные функции для каждого цвета
def red_light(traffic_light: TrafficLight):
    traffic_light.set_state("Red")
    time.sleep(5)  # Задержка для красного цвета
    print(f"{datetime.now()} - Красный горит 5 секунд")


def yellow_light(traffic_light: TrafficLight):
    traffic_light.set_state("Yellow")
    time.sleep(2)  # Задержка для желтого цвета
    print(f"{datetime.now()} - Желтый горит 2 секунды")


def green_light(traffic_light: TrafficLight):
    traffic_light.set_state("Green")
    time.sleep(3)  # Задержка для зеленого цвета
    print(f"{datetime.now()} - Зеленый горит 3 секунды")


# Асинхронные функции для каждого цвета
async def async_red_light(traffic_light: TrafficLight):
    traffic_light.set_state("Red")
    await asyncio.sleep(5)
    print(f"{datetime.now()} - Красный горит 5 секунд (асинхронно)")


async def async_yellow_light(traffic_light: TrafficLight):
    traffic_light.set_state("Yellow")
    await asyncio.sleep(2)
    print(f"{datetime.now()} - Желтый горит 2 секунды (асинхронно)")


async def async_green_light(traffic_light: TrafficLight):
    traffic_light.set_state("Green")
    await asyncio.sleep(3)
    print(f"{datetime.now()} - Зеленый горит 3 секунды (асинхронно)")


# Многопоточные функции для каждого цвета
def thread_red_light(traffic_light: TrafficLight):
    traffic_light.set_state("Red")
    time.sleep(5)
    print(f"{datetime.now()} - Красный горит 5 секунд (многопоточно)")


def thread_yellow_light(traffic_light: TrafficLight):
    traffic_light.set_state("Yellow")
    time.sleep(2)
    print(f"{datetime.now()} - Желтый горит 2 секунды (многопоточно)")


def thread_green_light(traffic_light: TrafficLight):
    traffic_light.set_state("Green")
    time.sleep(3)
    print(f"{datetime.now()} - Зеленый горит 3 секунды (многопоточно)")


# Синхронный подход
def run_sync_traffic_light():
    print("\nСинхронный режим:")
    traffic_light = TrafficLight()

    red_light(traffic_light)
    yellow_light(traffic_light)
    green_light(traffic_light)


# Асинхронный подход
async def run_async_traffic_light():
    print("\nАсинхронный режим:")
    traffic_light = TrafficLight()

    # Запускаем все асинхронные функции
    await asyncio.gather(
        async_red_light(traffic_light),
        async_yellow_light(traffic_light),
        async_green_light(traffic_light)
    )


# Многопоточный подход
def run_threaded_traffic_light():
    print("\nМногопоточный режим:")
    traffic_light = TrafficLight()

    # Создаем потоки для каждого цвета
    red_thread = threading.Thread(target=thread_red_light, args=(traffic_light,))
    yellow_thread = threading.Thread(target=thread_yellow_light, args=(traffic_light,))
    green_thread = threading.Thread(target=thread_green_light, args=(traffic_light,))

    # Запускаем потоки
    red_thread.start()
    yellow_thread.start()
    green_thread.start()

    # Ждем завершения потоков
    red_thread.join()
    yellow_thread.join()
    green_thread.join()






















# Основная функция
if __name__ == "__main__":
    # Синхронный режим
    run_sync_traffic_light()

    # Асинхронный режим
    asyncio.run(run_async_traffic_light())

    # Многопоточный режим
    run_threaded_traffic_light()
