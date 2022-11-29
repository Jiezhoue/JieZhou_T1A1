def weather(raining, temperature):
    match raining:
        case True if temperature < 15:
            return "It's wet and cold"
        case False if temperature < 15:
            return "It's not raining but cold"
        case False if temperature >= 15:
            return "It's warm but not raining"
        case _:
            return "It's warm and raining"

print(weather(True, 13))
print(weather(False, 14))
print(weather(False, 15))
print(weather(True, 34))