def apply_discount(product: dict, given_discount: int):
    price = product['price'] * (1.0 - (given_discount/100))
    assert 0 <= price <= product['price']
    return price


product_1 = {
    "name": "milk",
    "price": 1.5
}

discount = int(input("What discount do you have?"))

final_price = apply_discount(product_1, discount)
print("Your final price is:  {}".format(final_price))
