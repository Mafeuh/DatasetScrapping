def print_progression(current_state: int, maximum: int, message):
    percent = round(current_state / maximum * 100)
    print(f"Progression: [{'=' * percent}{' ' * (100 - percent)}] ({current_state}/{maximum}) {percent}% :", message)


print_progression(1, 100, 'Test')