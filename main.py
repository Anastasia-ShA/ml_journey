
def calculate_average(stats: list[int]) -> float:
    total_sum = sum(stats)
    count = len(stats)

    if count == 0:
        return 0.0

    return total_sum / count



hero_stats = [85, 92, 78, 90, 88]


result = calculate_average(hero_stats)

print(f"Среднее значение характеристик героя: {result}")
