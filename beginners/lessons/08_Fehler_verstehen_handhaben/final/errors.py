# Division durch null (führt zu ZeroDivisionError)
# print(10 / 0)

# Fehler abfangen
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Durch null teilen geht nicht!")

# else und finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Fehler!")
else:
    print("Alles gut, Ergebnis:", x)
finally:
    print("Fertig.")

# Sichere Division
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print("Sichere Division:", safe_divide(10, 2))
print("Sichere Division:", safe_divide(10, 0))

# Robuste Eingabe
while True:
    try:
        num = int(input("Gib eine Zahl ein: "))
        print("Danke, deine Zahl ist:", num)
        break
    except ValueError:
        print("Bitte eine gültige Zahl eingeben!")
