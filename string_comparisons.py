def naive_comparison(original_text, typed_text):
    max_score = len(original_text)
    current_score = 0

    for x, y in zip(original_text, typed_text):
        if x == y:
            current_score += 1

    print(current_score, max_score)

    accuracy = round(current_score/max_score, 2)*100

    return accuracy
