# Created by Joe Habre
---

## 📏 **4. Unit Converter**

### 📁 Folder: `unit-converter/converter.py`

```python
def convert_units():
    conversions = {
        "cm": ("inch", 0.3937),
        "inch": ("cm", 2.54),
        "kg": ("lb", 2.2046),
        "lb": ("kg", 0.4536)
    }

    print("📏 Unit Converter")
    for key, (unit, _) in conversions.items():
        print(f"{key} → {unit}")

    from_unit = input("From unit (cm/inch/kg/lb): ").lower()
    value = float(input(f"Enter value in {from_unit}: "))
    
    if from_unit in conversions:
        to_unit, factor = conversions[from_unit]
        result = value * factor
        print(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
    else:
        print("❌ Unsupported unit.")

if __name__ == "__main__":
    convert_units()
