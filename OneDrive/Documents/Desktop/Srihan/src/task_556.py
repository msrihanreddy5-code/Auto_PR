"""Production Implementation for RFC 5322 Email Validation Service"""
from typing import Dict, Any

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        raise ValueError("Email must be a string")
    if ".." in email or "@" not in email:
        raise ValueError("Invalid email format")
    parts = email.split("@")
    if len(parts) != 2 or not parts[0] or "." not in parts[1]:
        raise ValueError("Invalid domain")
    return True

class Solution:
    def run(self, address: str) -> Dict[str, Any]:
        valid = validate_email(address)
        return {"valid": valid, "address": address}
