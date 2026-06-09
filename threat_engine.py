def get_threat_level(object_name):

    high_threat = ["car", "truck", "bus"]
    medium_threat = ["motorcycle", "bicycle"]

    if object_name in high_threat:
        return "HIGH"

    elif object_name in medium_threat:
        return "MEDIUM"

    else:
        return "LOW"