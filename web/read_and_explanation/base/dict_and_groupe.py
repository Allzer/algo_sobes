data = [
    {"city": "Moscow", "value": 10},
    {"city": "SPB", "value": 5},
    {"city": "Moscow", "value": 15},
    {"city": "Kazan", "value": 7},
    {"city": "SPB", "value": 10},
]

result = {}

for item in data:
    value = result.get(item["city"], 0)

    result[item["city"]] = result.get(item["city"], 0) + item["value"]

print(result)