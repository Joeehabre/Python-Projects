# Created by Joe Habre

CATEGORIES = {
    "1": "Length",
    "2": "Weight",
    "3": "Temperature",
    "4": "Speed",
    "5": "Volume",
}

# All non-temperature units are relative to a base unit (factor = 1 unit in base)
LENGTH_FACTORS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "inch": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mile": 1609.344,
}

WEIGHT_FACTORS = {
    "mg": 0.000001,
    "g": 0.001,
    "kg": 1.0,
    "tonne": 1000.0,
    "oz": 0.0283495,
    "lb": 0.453592,
}

SPEED_FACTORS = {
    "m/s": 1.0,
    "km/h": 1 / 3.6,
    "mph": 0.44704,
    "knot": 0.514444,
    "ft/s": 0.3048,
}

VOLUME_FACTORS = {
    "ml": 0.001,
    "l": 1.0,
    "m3": 1000.0,
    "tsp": 0.00492892,
    "tbsp": 0.0147868,
    "fl_oz": 0.0295735,
    "cup": 0.236588,
    "pint": 0.473176,
    "gallon": 3.78541,
}


def linear_convert(value, from_unit, to_unit, factors):
    return value * factors[from_unit] / factors[to_unit]


def temp_convert(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = {
        ("c", "f"): lambda v: v * 9 / 5 + 32,
        ("f", "c"): lambda v: (v - 32) * 5 / 9,
        ("c", "k"): lambda v: v + 273.15,
        ("k", "c"): lambda v: v - 273.15,
        ("f", "k"): lambda v: (v + 459.67) * 5 / 9,
        ("k", "f"): lambda v: v * 9 / 5 - 459.67,
    }
    fn = conversions.get((from_unit, to_unit))
    if fn is None:
        raise ValueError(f"Unknown conversion: {from_unit} → {to_unit}")
    return fn(value)


def show_units(category, units):
    print(f"\n🔄 {category} units: {', '.join(units)}")


def fmt(value):
    return f"{value:.6g}"


def run_conversion():
    print("\n📏 Unit Converter")
    for key, name in CATEGORIES.items():
        print(f"  {key}. {name}")

    category_choice = input("Choose a category (1-5): ").strip()
    if category_choice not in CATEGORIES:
        print("❌ Invalid category.")
        return

    category = CATEGORIES[category_choice]

    if category == "Length":
        factors, units = LENGTH_FACTORS, list(LENGTH_FACTORS)
    elif category == "Weight":
        factors, units = WEIGHT_FACTORS, list(WEIGHT_FACTORS)
    elif category == "Speed":
        factors, units = SPEED_FACTORS, list(SPEED_FACTORS)
    elif category == "Volume":
        factors, units = VOLUME_FACTORS, list(VOLUME_FACTORS)
    else:
        factors, units = None, ["c", "f", "k"]

    show_units(category, units)

    from_unit = input("Convert from: ").strip().lower()
    to_unit = input("Convert to: ").strip().lower()

    if from_unit not in units or to_unit not in units:
        print(f"❌ Invalid unit. Choose from: {', '.join(units)}")
        return

    try:
        value = float(input(f"Enter value in {from_unit}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    try:
        if category == "Temperature":
            result = temp_convert(value, from_unit, to_unit)
        else:
            result = linear_convert(value, from_unit, to_unit, factors)
        print(f"\n✅ {fmt(value)} {from_unit} = {fmt(result)} {to_unit}")
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    while True:
        run_conversion()
        again = input("\nConvert again? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Goodbye!")
            break


if __name__ == "__main__":
    main()
