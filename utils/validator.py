import re

def validate_document(text):
    result = {
        "document_type": "Unknown",
        "fields": {},
        "valid_score": 0
    }

    # Aadhaar
    if re.search(r"\b\d{4} \d{4} \d{4}\b", text):
        result["document_type"] = "Aadhaar Card"
        result["fields"]["Aadhaar Number"] = "✅"
        result["fields"]["DOB/Year of Birth"] = "✅" if re.search(r"\d{4}", text) else "❌"
        result["fields"]["Gender"] = "✅" if re.search(r"Male|Female|Other", text, re.IGNORECASE) else "❌"

    # PAN
    elif re.search(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b", text):
        result["document_type"] = "PAN Card"
        result["fields"]["PAN Number"] = "✅"
        result["fields"]["DOB"] = "✅" if re.search(r"\d{2}/\d{2}/\d{4}", text) else "❌"
        result["fields"]["Father's Name"] = "✅" if "Father" in text else "❌"

    # Score
    total = len(result["fields"])
    valid = list(result["fields"].values()).count("✅")
    result["valid_score"] = int((valid / total) * 100) if total > 0 else 0

    return result
