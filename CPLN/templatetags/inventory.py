from django import template
from CPLN.models import Inventory, Ingredient
register = template.Library()

@register.simple_tag
def Calculate(ingredient_qty, qty):
    return int(ingredient_qty) * int(qty)

@register.simple_tag
def GetFamilyInventory(prod_id, fly):
    inv_prod = Inventory.objects.filter(family__name = fly, product_id = prod_id).last()
    if not inv_prod:
        return 0
    return int(inv_prod.quantity)

@register.simple_tag
def DiffInvQty(qty_calculated, qty_inventory):
    return int(qty_inventory) - int(qty_calculated)

@register.filter
def positive(value):
    return int(value) * -1