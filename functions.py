def get_melon_order_price(price, quantity):
    """Calculate the cost for an order of melons."""

    tax = 0.075

    return price * quantity + (tax * price * quantity)




def main():
    tax = 0.40
    price = 50
    quantity = 1

    print(price, quantity, tax)   # before function is called

    print(get_melon_order_price(5, 10))

    print(price, quantity, tax)   # after function is called


main()
