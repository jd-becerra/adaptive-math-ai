def next_difficulty(current: str, correct: bool) -> str:
    levels = ["easy", "medium", "hard"]
    if current not in levels:
        return "easy"

    index = levels.index(current)
    if correct and index < len(levels) - 1:
        return levels[index + 1]
    if not correct and index > 0:
        return levels[index - 1]
    return current
