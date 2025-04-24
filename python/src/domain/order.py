from dataclasses import dataclass, field

from .order_item import OrderItem
from .order_status import OrderStatus

from python.src.domain.product import Product
from python.src.domain.order_item import OrderItem

from python.src.use_case.exceptions import (
    ShippedOrdersCannotBeChangedException,
    RejectedOrderCannotBeApprovedException,
    ApprovedOrderCannotBeRejectedException,
)


@dataclass
class Order:
    id: int = 0
    total: float = 0
    currency: str = "EUR"
    items: list[OrderItem] = field(default_factory=list)
    tax: float = 0
    status: OrderStatus = OrderStatus.CREATED

    def approve(self):
        self._raise_if_order_shipped()
        self._raise_if_order_was_rejected()
        self.status = OrderStatus.APPROVED

    def reject(self):
        self._raise_if_order_shipped()
        self._raise_if_order_was_approved()
        self.status = OrderStatus.REJECTED

    def add_item(self, product: Product, quantity: int):
        tax_amount, taxed_amount = product.calculate_tax_amounts(quantity)

        order_item = OrderItem(
            product=product,
            quantity=quantity,
            tax=tax_amount,
            taxed_amount=taxed_amount,
        )
        self.items.append(order_item)
        self.total += taxed_amount
        self.tax += tax_amount

    def _raise_if_order_shipped(self):
        if self.status == OrderStatus.SHIPPED:
            raise ShippedOrdersCannotBeChangedException()

    def _raise_if_order_was_rejected(self):
        if self.status == OrderStatus.REJECTED:
            raise RejectedOrderCannotBeApprovedException()

    def _raise_if_order_was_approved(self):
        if self.status == OrderStatus.APPROVED:
            raise ApprovedOrderCannotBeRejectedException()
