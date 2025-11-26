from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79111234567"),
    Smartphone("Samsung", "Galaxy ", "+79221234567"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79331234567"),
    Smartphone("Google", "Pixel ", "+79441234567"),
    Smartphone("Honor", "50 Lite", "+79551234567"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.number}")
