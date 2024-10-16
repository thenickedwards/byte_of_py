# single alternative decision structure
weather = "cold"
if weather == "cold": print("Wear a jacket!")

# multi-way decision strucutre
x = 5
if x < 1:
    print("small")
elif x <= 9223372036854775807: #pyton 2 max jint value :D
    print("medium")
else:
    print("large")

# nested conditions [not preferred]
if x > 1:
    print("More than 1")
    if x < 100:
        print("Less than 100")
print(f"x is {x}")

# use logical operators to avoid nested conditions
if x > 1 and x < 100:
    print("More than 1")
    print("Less than 100")
print("Use logical operators to avoid nested conditions and make code simpler to read 🧑‍💻")