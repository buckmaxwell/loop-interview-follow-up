from dataclasses import dataclass, field

from .category import Category


@dataclass
class Product:
    name: str = ""
    price: float = 0
    category: Category = field(default_factory=Category)

    def calculate_tax_amounts(self, quantity: int) -> tuple[float, float]:
        unitary_tax = round(self.price / 100 * self.category.tax_percentage, 2)
        unitary_taxed_amount = round((self.price + unitary_tax), 2)
        taxed_amount = round(unitary_taxed_amount * quantity, 2)
        tax_amount = unitary_tax * quantity

        return tax_amount, taxed_amount
