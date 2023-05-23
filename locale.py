import locale

# Definindo as localidades
locales = {
    "Brasil": "pt_BR",
    "Japão": "ja_JP",
    "Estados Unidos": "en_US",
    "China": "zh_CN"
}

# Percorrendo as localidades e exibindo informações
for country, loc in locales.items():
    try:
        print(f"\n--- {country} ---")
        locale.setlocale(locale.LC_ALL, loc)
    
        # Obtendo o formato de moeda
        currency_format = locale.localeconv()["currency_symbol"]
        print("Símbolo da moeda:", currency_format)
    
        # Exibindo um valor monetário formatado
        value = 1234567.89
        formatted_value = locale.currency(value)
        print("Valor formatado:", formatted_value)
    
        # Obtendo o separador de milhares e o separador decimal
        thousands_sep = locale.localeconv()["thousands_sep"]
        decimal_sep = locale.localeconv()["decimal_point"]
        print("Separador de milhares:", thousands_sep)
        print("Separador decimal:", decimal_sep)
    except:
        ...
