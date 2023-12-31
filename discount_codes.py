"""
        Ejemplo:
        "primavera2021" deberia devolver True, ya que al compararlo:
        vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
        vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o',
        'm', 'V', 'p', 'v')
        vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0',
        'x', 'e', 'd', 'p', 'r')
        vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i',
        'v', 'n',
        'o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
"""

AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code):
   
    for code in AVAILABLE_DISCOUNT_CODES:
        differences = sum(a != b for a, b in zip(discount_code, code))
        if differences < 3:
            return True    
    return False


print(validate_discount_code(input("Enter a code: ")))