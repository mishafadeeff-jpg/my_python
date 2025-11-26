from address import Address
from mailing import Mailing

to_addr = Address("123456", "Киров", "Ленина", "10", "58")
from_addr = Address("610035", "Санкт-Петербург", "Невский", "20", "101")
mail = Mailing(to_addr, from_addr, 3250, "TRACK12345RU")

print(f"Отправление {mail.track} из {mail.from_address.index}, "
      f"{mail.from_address.city}, "
      f"{mail.from_address.street}, {mail.from_address.house} -"
      f" {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, "
      f"{mail.to_address.street}, "
      f"{mail.to_address.house} - {mail.to_address.apartment}. "
      f"Стоимость {mail.cost} рублей.")
