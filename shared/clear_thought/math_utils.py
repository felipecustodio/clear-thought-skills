def normalize(value: float, min_v: float, max_v: float) -> float:
    if max_v == min_v:
        return 0.0
    return (value - min_v) / (max_v - min_v)
