from reporting import render_invoice


def checkout_preview(order):
    return render_invoice(order)
