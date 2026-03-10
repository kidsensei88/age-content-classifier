
def classify_content(text):

    sexual_keywords = ["kiss", "sex", "naked", "flirt"]
    violence_keywords = ["fight", "kill", "punch"]
    bad_words = ["fuck", "shit"]

    score = 0

    for word in sexual_keywords:
        if word in text.lower():
            score += 2

    for word in violence_keywords:
        if word in text.lower():
            score += 2

    for word in bad_words:
        if word in text.lower():
            score += 1

    if score >= 5:
        return "18+"
    elif score >= 3:
        return "16+"
    elif score >= 1:
        return "13+"
    else:
        return "7+"

text = input("Enter video transcript: ")

result = classify_content(text)

print("Suggested age rating:", result)
