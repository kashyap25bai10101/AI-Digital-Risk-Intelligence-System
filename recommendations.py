def get_recommendations(risk):
    if risk == "High":
        return [
            "Enable 2FA immediately",
            "Avoid suspicious links",
            "Use strong unique passwords"
        ]
    elif risk == "Medium":
        return [
            "Improve password strength",
            "Be cautious with unknown emails"
        ]
    else:
        return [
            "Maintain your current security practices"
        ]
