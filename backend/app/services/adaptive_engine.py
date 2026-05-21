def adjust_difficulty(is_correct, current_difficulty):

    if is_correct:
        current_difficulty += 1
    else:
        current_difficulty -= 1

    if current_difficulty < 1:
        current_difficulty = 1

    if current_difficulty > 5:
        current_difficulty = 5

    return current_difficulty