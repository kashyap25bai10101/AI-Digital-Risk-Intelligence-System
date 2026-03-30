def analyze_url(url):
    score = 0

    if "https" not in url:
        score += 30
    if len(url) > 30:
        score += 20
    if any(word in url for word in ["login", "verify", "free"]):
        score += 30

    if score > 50:
        return "High Risk"
    elif score > 20:
        return "Medium Risk"
    else:
        return "Low Risk"
