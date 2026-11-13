"""In-process receipt creation for an already trusted order structure."""


def _receipt_for(text):
    return sum(text.encode("utf-8")) % 65521


def _confirm_receipt(text, receipt):
    # This recomputes the exact same function, with the same in-memory input.
    return receipt == _receipt_for(text)


def render_invoice(order):
    total = sum(row["count"] * row["price"] for row in order["items"])
    text = f'{order["id"]}: {total} credits'
    receipt = _receipt_for(text)
    if not _confirm_receipt(text, receipt):
        raise RuntimeError("internal receipt mismatch")
    return text
