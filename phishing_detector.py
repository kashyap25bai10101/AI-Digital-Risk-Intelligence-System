def detect_phishing(text):
    suspicious_keywords = ["login", "verify", "bank", "free", "urgent", "click"]

    score = 0
    for word in suspicious_keywords:
        if word in text.lower():
            score += 1

    if score >= 2:
        return "Likely Phishing"
    else:
        return "Safe"
