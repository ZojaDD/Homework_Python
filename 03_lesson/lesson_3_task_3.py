from address import Address
from mailing import Mailing

to_address = Address(101000, "Москва", "Арбатский переулок", 49, 102)
from_address = Address(410000, "Саратов", "Проспект Энтузиастов", 10, 7)
track = 1234567890123456
cost = 300.00

mailing = Mailing(to_address, from_address, cost, track)
print(mailing)
