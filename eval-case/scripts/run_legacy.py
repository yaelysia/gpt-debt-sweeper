"""Old developer-only diagnostic; no runtime registration."""
from plugins.legacy import LegacyCommand


def check_retired_plugin():
    return LegacyCommand().run() == "RETIRED"
