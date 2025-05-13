# Created by Joe Habre

def convert_length(value, from_unit, to_unit):
    factors = {
        "cm": 1,
        "m": 100,
        "inch": 2.54,
        "ft": 30.48
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    factors = {
        "kg": 1,
        "g": 0.001,
        "lb": 0.453592,
        "oz": 0.0283495
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "c" and to_unit == "f":
        return (value * 9/5) + 32
    if from_unit == "f" and to_unit == "c":
        return (value - 32) * 5/9
    if from_unit == "c" and to_unit == "k":
        return value + 273.15
    if from_unit == "k" and to_unit == "c":
        return value - 273.15
    if from_unit == "f" and to_unit == "k":
        return (value + 459.67) * 5/9
    if from_unit == "k" and to_unit == "f":
        return (value * 9/5) - 459.67

def main():
    print("📏 Unit Converter")
    categories = {
        "1": ("Length", convert_length, ["cm", "m", "inch", "ft"]),
        "2": ("Weight", convert_weight, ["kg", "g", "lb", "oz"]),
        "3": ("Temperature", convert_temperature, ["c", "f", "k"])
    }

    for key, (name, _, _) in categories.items():
        print(f"{key}. {name}")

    category_choice = input("Choose a category (1-3): ").strip()

    if category_choice not in categories:
        print("❌ Invalid category.")
        return

    category_name, convert_func, units = categories[category_choice]
    print(f"\n🔄 {category_name} units:", ", ".join(units))

    from_unit = input("Convert from: ").strip().lower()
    to_unit = input("Convert to: ").strip().lower()

    if from_unit not in units or to_unit not in units:
        print("❌ Invalid units.")
        return

    try:
        value = float(input(f"Enter value in {from_unit}: "))
        result = convert_func(value, from_unit, to_unit)
        print(f"✅ {value} {from_unit} = {round(result, 4)} {to_unit}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
