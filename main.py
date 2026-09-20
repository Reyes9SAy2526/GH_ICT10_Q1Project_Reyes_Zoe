# The Generator
from pyscript import display, document

def order(e):

    document.getElementById("result").innerHTML = ""

    book1 = float(document.getElementById("book1").value)
    book2 = float(document.getElementById("book2").value)
    book3 = float(document.getElementById("book3").value)
    book4 = float(document.getElementById("book4").value)

    price1 = 350
    price2 = 420
    price3 = 380
    price4 = 310

    total1 = book1 * price1
    total2 = book2 * price2
    total3 = book3 * price3
    total4 = book4 * price4

    subtotal = total1 + total2 + total3 + total4

    vat = subtotal * 0.12
    total = subtotal + vat

    display(f"Subtotal: ₱{subtotal:.2f}", target="result")
    display(f"VAT (12%): ₱{vat:.2f}", target="result")
    display(f"Total Amount: ₱{total:.2f}", target="result")


def make_sku(e):

    document.getElementById("skuResult").innerHTML = ""

    category = document.getElementById("category").value
    title = document.getElementById("productName").value
    quantity = document.getElementById("stockQty").value

    sku = category + "-" + title + "-" + quantity

    display(f"Generated SKU: {sku}", target="skuResult")