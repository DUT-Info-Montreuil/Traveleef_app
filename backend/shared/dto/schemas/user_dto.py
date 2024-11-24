user_dto = {
    "type": "object",
    "properties": {
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "role": {"type": "string", "enum": ["admin", "user"]},
        "password": {"type": "string"}
    },
    "required": ["first_name", "last_name", "email", "role"],
    "additionalProperties": False
}