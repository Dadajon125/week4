print("SHOPPING CART CALCULATOR")
print("=======================================")

input("Order Receipt for:")
def calculate_item_total (quantity_unit_price):
    return ("quantity * unit_price")
def apply_bulk_discount (total_quantity):
    if ("quantity") >=10:
        rate = 0.10
    elif ("quantity") >=5:
        rate = 0.5
    else:
        rate = 0.0
    return ("total * rate")
def calculate_tax ( subtotal, tax_rate):
    tax_rate = 'percent' ( 8 )
    return 'subtotal'( tax_rate / 100 )
def is_eligible_for_free_shipping(subtotal):
    return subtotal >=50
def process_order(item_name, quantity, unit_price, tax_rate):
    item_total = calculate_item_total(quantity, unit_price)
    discount = apply_bulk_discount(item_total, quantity)
    subtotal_after_discount = item_total - discount
    tax = calculate_tax(subtotal_after_discount, tax_rate)
    total = subtotal_after_discount + tax
    free_shipping = is_eligible_for_free_shipping(subtotal_after_discount)
 

print(f"receipt for: {'item-name'}")
print(f"quantity: {'quantity'}")
print(f"  Unit price: ${'unit_price:.2f'}")
print(f"  Item total: ${'item_total:.2f'}")
discount_rate = ('discount / item_total * 100') if 'item_total' else '0'
print(f"  Bulk discount: {'discount_rate:.0f'}%  (-${'discount:.2f'})")
print(f"  Subtotal after discount: ${'subtotal_after_discount:.2f'}")
print(f"  Tax ({'tax_rate:.2f'}%): ${'tax:.2f'}")
print(f"  Free shipping eligible: {'Yes' if 'free_shipping' else 'No'}")
print(f"  Total: ${'total:.2f'}")
print("-" * 40)





        
    


