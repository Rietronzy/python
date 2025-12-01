# currency_converter.py

def convert_currency(amount, from_currency, to_currency):
    # Exchange rate as of November 2025 (example)
    if from_currency.lower() == "usd" and to_currency.lower() == "zar":
        return amount * 18.5
    elif from_currency.lower() == "zar" and to_currency.lower() == "usd":
        return amount / 18.5
    else:
        print("Unsupported currency conversion.")
        return None

def main():
    amount = float(input("Enter amount: "))
    from_currency = input("Convert from (USD/ZAR): ")
    to_currency = input("Convert to (USD/ZAR): ")
    result = convert_currency(amount, from_currency, to_currency)
    if result is not None:
        print(f"{amount} {from_currency.upper()} is {result:.2f} {to_currency.upper()}")

if __name__ == "__main__":
    main()