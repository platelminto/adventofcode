def total_calories(food_calories: str) -> int:
    return sum(int(calories) for calories in food_calories.strip().split("\n"))


with open("input.txt", "r") as f:
    text = f.read()

print(max([total_calories(food_calories) for food_calories in text.split("\n\n")]))
