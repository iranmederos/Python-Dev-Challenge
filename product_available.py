import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": [
                           "Chocolate", "Granizado", "Limon", "Dulce de Leche"], "quantity": [3, 10, 0, 5]})


def is_product_available(product_name, quantity, limit_attempts=3):

    attempts = 0

    while (attempts < limit_attempts):
        product_row = _PRODUCT_DF[_PRODUCT_DF["product_name"] == product_name]

        if not product_row.empty:
            available_quantity = product_row["quantity"].iloc[0]
            if available_quantity >= quantity:
                return True

        attempts += 1
        print(f"{product_name} unaviable or insufficient, remaining attempts: {limit_attempts - attempts} ")
        print("Available products:")
        print(_PRODUCT_DF[["product_name", "quantity"]])
        product_name = input("Enter product name: ")
        quantity = int(input("Enter a quantity: "))
    return False


product_name = input("Enter a product name: ")
quantity = int(input("Enter a quantity: "))

print(is_product_available(product_name, quantity))
