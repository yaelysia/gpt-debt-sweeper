import json
from pathlib import Path
from .registry import get_backend
from .forwarder import Forwarder


def send_welcome(user):
    settings = json.loads((Path(__file__).parent / "settings.json").read_text(encoding="utf-8"))
    sender = Forwarder(get_backend(settings["backend"]))
    return sender.send(user, "welcome")
