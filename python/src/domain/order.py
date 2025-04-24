from dataclasses import dataclass, field

from .order_item import OrderItem
from .order_status import OrderStatus

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

    def _raise_if_order_shipped(self):
        if self.status == OrderStatus.SHIPPED:
            raise ShippedOrdersCannotBeChangedException()

    def _raise_if_order_was_rejected(self):
        if self.status == OrderStatus.REJECTED:
            raise RejectedOrderCannotBeApprovedException()

    def _raise_if_order_was_approved(self):
        if self.status == OrderStatus.APPROVED:
            raise ApprovedOrderCannotBeRejectedException()
