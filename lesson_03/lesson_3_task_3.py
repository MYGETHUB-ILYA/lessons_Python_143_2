from address import Address
from mailing import Mailing

address_start = Address("123456", "Камызяки", "Ленина", "5", "178")
address_finish = Address("987654", "Воронеж", "Лизюкова", "12", "41")

cost = 3456
track = "RU126733443E34"

mailing = Mailing(address_start, address_finish, cost, track)
str_f_text = mailing.from_address
str_t_text = mailing.to_address

print(f"Отправление {mailing.track} из {str_f_text.index}, {str_f_text.city}, "
      f"{str_f_text.street}, {str_f_text.house} - {str_f_text.flat} в "
      f"{str_t_text.index}, {str_t_text.city}, {str_t_text.street}, "
      f"{str_t_text.house} - {str_t_text.flat}."
      f"Стоимость {mailing.cost} рублей.")
