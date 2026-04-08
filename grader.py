def grade(state):
    temps = [t for row in state["temperature"] for t in row]
    avg_temp = sum(temps) / len(temps)

    if avg_temp < 31:
        return 1.0
    elif avg_temp < 34:
        return 0.7
    elif avg_temp < 36:
        return 0.4
    else:
        return 0.0