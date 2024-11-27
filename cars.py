#Программа автосалон
from datetime import datetime
from typing import Dict, Union, List

#время открытия / закрытия автосалона
#количество автомобилей в салоне 5
#каждый автомобиль обладает: марка, модель, цвет, год выпуска, цена

#HomeWork:
#TODO: покупка автомобиля из салона
#TODO: расчет количества лет, месяцев, дней, для оплаты авто (10% от з\п в месяцах)

TODAY = datetime.today()
DAYS_IN_DIGIT_DICT = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday'}


def is_work_time(day_time: Dict[str, Union[List[int], List[str]]]) -> bool:
    time = day_time['time']
    days = day_time['days']
    if TODAY.weekday() in days and TODAY.hour in range(time[0], time[1]):
        return True
    else:
        return False
def get_key_by_value(data: Dict[int, str], value: str) -> Union[int, None]:
    return next((k for k, v in data.items() if v == value), None)

class Car:
    def __init__(self, brand, model, color, year, price):
        self.brand: str = brand
        self.model: str = model
        self.color: str = color
        self.year: int = year
        self.price: float = price

class CarSalon:
    __instance: 'CarSalon' = None
    def __init__(self, work: Dict[str, Union[List[str], List[int]]], cars: List[Car]) -> None:

        self.cars: List[Car] = cars
        self.work: Dict[str, Union[List[str], List[int]]] = work
        self.car_count: [int] = 0 #исключен из инициализатора и прописано дефолтное значение

        self.__post_init__(work, cars)  # Вызов метода __post_init__



    @staticmethod
    def string_days_to_int_days(work: Dict[str, Union[List[str], List[int]]]) -> None:
        new_days = []
        for day in work['days']:
            if day in DAYS_IN_DIGIT_DICT.values():
                key = get_key_by_value(DAYS_IN_DIGIT_DICT, day)
                if key is not None:  # Ensure key is not None
                    new_days.append(key)
        work['days'] = new_days

    def __post_init__(self, work: Dict[str, Union[List[str], List[int]]], cars: List[Car]) -> None:
        self.string_days_to_int_days(work)
        self.car_count = len(cars)


    @classmethod
    def open(cls):
        print('Добро пожаловать в автосалон Тигран и Ко!')
        print()
        print(car_salon.show_cars())


    def show_cars(self) -> None:
        print(f'В салоне есть {self.car_count} машин.')
        print('Вашему вниманию представлены следующие автомобили:')
        for car in self.cars:
            print(f'Марка: {car.brand}, Модель: {car.model}, Цвет: {car.color}, Год выпуска: {car.year}, Цена: {car.price} y.e.')

#создаем экземпляр объекта класса CarSalon
car_salon = CarSalon(work={'days': ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'],
                           'time': [9, 20]
                           },
                     cars=[Car('Toyota', 'Camry','red', 2015, 10000),
                                       Car('Honda', 'Accord', 'blue', 2017, 15000),
                                       Car('Ford', 'Mustang', 'black', 2016, 12000),
                                       Car('Tesla', 'Model S', 'white', 2019, 20000),
                                       Car('BMW', 'X5','silver', 2018, 18000)]
                     )


if __name__ == "__main__":
    if is_work_time(car_salon.work):
        CarSalon.open()
    else:
        print("Не рабочее время")