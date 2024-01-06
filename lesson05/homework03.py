#Написати функцію переведення розмірів жіночої білизни з міжнародної у решту. Всередині функції потрібно просто звертатися до правильно складеного словника.

woman_size = {
    'XXS': {'DEU': '36',
            'USA': '8',
            'FR': '38',
            'UK': '24'},
    'XS': {'DEU': '38',
            'USA': '10',
            'FR': '40',
            'UK': '26'},
    'S': {'DEU': '40',
            'USA': '12',
            'FR': '42',
            'UK': '28'},
    'M': {'DEU': '42',
            'USA': '14',
            'FR': '44',
            'UK': '30'},
    'L': {'DEU': '44',
            'USA': '16',
            'FR': '46',
            'UK': '32'},
    'XL': {'DEU': '46',
            'USA': '18',
            'FR': '48',
            'UK': '34'},
    'XXL': {'DEU': '48',
            'USA': '20',
            'FR': '50',
            'UK': '36'}
}

question = input("Enter your size (XXS - XXL): ")

if question in woman_size:
    size_info = woman_size[question]
    print(f"Your international size for DEU is: {size_info['DEU']}")
    print(f"Your international size for USA is: {size_info['USA']}")
    print(f"Your international size for FR is: {size_info['FR']}")
    print(f"Your international size for UK is: {size_info['UK']}")
else:
    print("Invalid size name!")