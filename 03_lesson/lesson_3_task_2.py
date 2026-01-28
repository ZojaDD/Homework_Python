from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "15 Ultra", "+79999999999"),
    Smartphone("Honor", "200 Pro", "+78888888888"),
    Smartphone("Huawei", "Pura 80", "+77777777777"),
    Smartphone("Samsung", "Galaxy A55", "+76666666666"),
    Smartphone("Poco", "F6", "+75555555555")
]

for smartphone in catalog:
    print(f"{smartphone.brand_smartphone} - {smartphone.model_smartphone}. \
{smartphone.subscriber_number}")
