from typing import Any, Dict

from rest_framework_simplejwt.tokens import Token


class StaleToken(Token):
    token_type = "stale"

    def __init__(self, payload: Dict[str, Any]):
        self.payload = payload
