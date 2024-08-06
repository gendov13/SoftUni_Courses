countries = input().split(", ")
capitals = input().split(", ")

countires_capitals = dict(zip(countries,capitals))
for country, capital in countires_capitals.items():
    print(f"{country} -> {capital}")
