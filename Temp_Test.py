# Simple Thermometer App
# This program checks temperature and provides fun feedback

print("🌡️  Welcome to the Temperature Checker! 🌡️")
print("=" * 45)

# Get temperature input from user
try:
    temperature = float(input("\nEnter the temperature in degrees: "))
    
    # Determine temperature status using conditional statements
    if temperature < 10:
        status = "FREEZING ❄️"
        comment = "Brrr! Time to bundle up like a burrito! 🥶"
    
    elif temperature >= 10 and temperature < 15:
        status = "CHILLY 🧊"
        comment = "Grab a jacket, it's nippy out there!"
    
    elif temperature >= 15 and temperature <= 25:
        status = "COLD 🧥"
        comment = "Perfect sweater weather! Cozy up! ☕"
    
    elif temperature > 25 and temperature < 30:
        status = "MILD 🍃"
        comment = "Not too hot, not too cold - just right!"
    
    elif temperature >= 30 and temperature <= 50:
        status = "WARM ☀️"
        comment = "Nice and toasty! Great day to be outside! 😊"
    
    elif temperature > 50 and temperature < 60:
        status = "GETTING HOT 🌤️"
        comment = "Things are heating up! Stay hydrated!"
    
    elif temperature >= 60 and temperature <= 90:
        status = "HOT 🔥"
        comment = "Sizzling! Time for ice cream and shade! 🍦"
    
    elif temperature > 90 and temperature < 100:
        status = "VERY HOT 🥵"
        comment = "Extreme heat! Stay cool and drink water!"
    
    else:  # temperature >= 100
        status = "BOILING 💧"
        comment = "Water turns to steam! That's scorching! 🌋"
    
    # Display results
    print("\n" + "=" * 45)
    print(f"Temperature: {temperature}°")
    print(f"Status: {status}")
    print(f"Comment: {comment}")
    print("=" * 45)

except ValueError:
    print("\n❌ Oops! Please enter a valid number!")
except Exception as e:
    print(f"\n❌ An error occurred: {e}")