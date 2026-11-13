"""Retired same-process verification script."""
from reporting import _receipt_for, _confirm_receipt


def verify_sample(text):
    return _confirm_receipt(text, _receipt_for(text))
