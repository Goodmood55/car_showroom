#Программа автосалон
from datetime import datetime

#время открытия / закрытия автосалона
#количество автомобилей в салоне 5
#каждый автомобиль обладает: марка, модель, цвет, год выпуска, цена
#покупка автомобиля из салона
#расчет количества лет, месяцев, дней, для оплаты авто (10% от з\п в месяцах)

TODAY = datetime.today()
DAYS_IN_DIGIT_DICT = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday'}


def is_work_time(day_time: dict):
    time = day_time['time']
    days = day_time['days']
    if TODAY.weekday() in days and TODAY.hour in range(time[0], time[1]):
        return True
    else:
        return False


class CarSalon:
    __instance = None
    def __init__(self, work, car_count, car):
        self.work = work
        self.car_count = car_count
        self.car = car

        self.__post_init__(work)  # Вызов метода __post_init__

    @staticmethod
    def get_key_by_value(data, value):
        return next((k for k, v in data.items() if v == value), None)


    def __post_init__(self, work):
        for day in self.work['days']:
            if day in DAYS_IN_DIGIT_DICT.values():
                self.work['days'][work['days'].index(day)] = self.get_key_by_value(DAYS_IN_DIGIT_DICT, day)


    @classmethod
    def open(cls):
        print('Добро пожаловать в автосалон Тигран и Ко')




#создаем экземпляр объекта класса CarSalon
car_salon = CarSalon(work={'days': ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'],
                           'time': [9, 20]
                           },
                     car_count=5, car=['bmw', 'chevrolet', 'porsche']
                     )


if __name__ == "__main__":
    if is_work_time(car_salon.work):
        CarSalon.open()
    else:
        print("Не рабочее время")