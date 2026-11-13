from .provider import TextProvider

_REGISTRY = {"text": TextProvider}


def get_backend(name):
    return _REGISTRY[name]()
