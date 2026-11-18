texto = input ("What is the answer to the great question of life, the universe, and everything? ").strip().lower()
match texto:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")