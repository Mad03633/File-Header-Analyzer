
def analyze_entropy(file_path):
    import math
    from pathlib import Path
    from collections import Counter

    try:
        path = Path(file_path).resolve(strict=True)
        with open(str(path), 'rb') as f:
            data = f.read()
    except Exception as e:
        return {"error": f"Failed to read file: {e}"}

    if not data:
        return {"error": "File is empty"}

    byte_counts = Counter(data)
    total = len(data)

    entropy = -sum((count / total) * math.log2(count / total) for count in byte_counts.values())
    entropy = round(entropy, 4)

    if entropy > 7.8:
        category = "Very High"
        comment = "High randomness detected, possibly encrypted or packed content"
    elif entropy > 7.0:
        category = "High"
        comment = "Elevated entropy, possibly compressed or binary data"
    elif entropy > 5.0:
        category = "Moderate"
        comment = "Typical entropy for structured or document files"
    else:
        category = "Low"
        comment = "Low entropy, possibly plain text, zero-padded, or unstructured data"

    most_common_byte = byte_counts.most_common(1)[0][0]

    return {
        "entropy": entropy,
        "risk": "High" if entropy > 7.5 else "Low",
        "entropy_category": category,
        "top_byte": f"{most_common_byte:02X}",
        "length_bytes": total,
        "note": comment
    }
