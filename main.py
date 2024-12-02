# Класс для задания 8.1.1
class Vehicle:
    def init(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheels):
        if wheels == 2:
            return f"Это мотоцикл марки {self.name}."
        elif wheels == 3:
            return f"Это трицикл марки {self.name}."
        elif wheels == 4:
            return f"Это автомобиль марки {self.name}."
        else:
            return f"Я не знаю таких ТС марки {self.name}."

    def get_vehicle_advice(self):
        if self.mileage < 50000:
            return f"Неплохо ({self.name}) можно брать."
        elif 50001 <= self.mileage <= 100000:
            return f"({self.name}) надо внимательно проверить."
        elif 100001 <= self.mileage <= 150000:
            return f"({self.name}) надо провести полную диагностику."
        else:
            return f"({self.name}) лучше не покупать."


vehicles = [
    Vehicle("BMW", 45000),
    Vehicle("Toyota", 95000),
    Vehicle("Ford", 130000),
    Vehicle("Lada", 180000)
]

for vehicle in vehicles:
    print(vehicle.get_vehicle_type(4))
    print(vehicle.get_vehicle_advice())

# Класс для задания 8.1.2
class HotelBooking:
    def init(self, hotel_name, room_number, stay_dates, guest_name=None):
        self.hotel_name = hotel_name
        self.room_number = room_number
        self.stay_dates = stay_dates
        self.guest_name = guest_name
        self.is_booked = False

    def check_availability(self):
        if self.is_booked:
            return f"Номер {self.room_number} в {self.hotel_name} в данный момент забронирован."
        return f"Номер {self.room_number} в {self.hotel_name} доступен."

    def book(self, guest_name):
        if self.is_booked:
            return f"Не удалось забронировать номер {self.room_number}. Он уже забронирован."
        self.guest_name = guest_name
        self.is_booked = True
        return f"Номер {self.room_number} в {self.hotel_name} успешно забронирован для {guest_name}."

    def cancel(self):
        if not self.is_booked:
            return f"Номер {self.room_number} не забронирован, поэтому его нельзя отменить."
        canceled_guest = self.guest_name
        self.guest_name = None
        self.is_booked = False
        return f"Бронирование для {canceled_guest} в номере {self.room_number} отменено."

    def modify_booking(self, new_stay_dates=None, new_guest_name=None):
        if not self.is_booked:
            return f"Невозможно изменить бронирование номера {self.room_number}. Бронирование отсутствует."
        if new_stay_dates:
            self.stay_dates = new_stay_dates
        if new_guest_name:
            self.guest_name = new_guest_name
        return f"Бронирование для номера {self.room_number} изменено."



booking1 = HotelBooking("Grand Hotel", 101, "2024-12-01 по 2024-12-10")
booking2 = HotelBooking("City Inn", 202, "2024-12-05 по 2024-12-15")

print(booking1.check_availability())
print(booking1.book("Джон Доу"))
print(booking1.modify_booking(new_stay_dates="2024-12-02 по 2024-12-12"))
print(booking1.cancel())

print(booking2.check_availability())
print(booking2.book("Джейн Смит"))