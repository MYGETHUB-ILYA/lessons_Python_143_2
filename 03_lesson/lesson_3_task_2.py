from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Nokia", "N-3110", "+79219999999"))
catalog.append(Smartphone("iPhone", "XR", "+79119999999"))
catalog.append(Smartphone("Samsung", "Expiria", "+79059999999"))
catalog.append(Smartphone("Motorolla", "YV-550", "+791519999999"))
catalog.append(Smartphone("Redmi", "LX-342", "+79039999999"))

for phone in catalog:
    print(f"{phone.brand:<10} - {phone.model:<10}. {phone.number:<10}")
