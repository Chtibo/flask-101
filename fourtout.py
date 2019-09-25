PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'Me' }
    ]

print(len(PRODUCTS))
count = 1
print (count)
print(PRODUCTS)
for product in PRODUCTS:
    print(product)
    print(product["id"])
    if product["id"] == count:
        print(True)
        PRODUCTS.remove(product)
    else:
        print(False)
print(PRODUCTS)

PRODUCTS.append({"id": 5 ,"name" : "Here"})
print(PRODUCTS)
