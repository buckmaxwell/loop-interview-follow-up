from ..domain.order import Order
from ..repository.order_repository import OrderRepository
from ..repository.product_catalog import ProductCatalog
from .exceptions import UnknownProductException
from .sell_items_request import SellItemsRequest


class OrderCreationUseCase:
    def __init__(
        self, order_repository: OrderRepository, product_catalog: ProductCatalog
    ):
        self._order_repository = order_repository
        self._product_catalog = product_catalog

    def run(self, request: SellItemsRequest) -> None:
        order = (
            Order()
        )  # NOTE: a create method on Order could be good, but for now direct init is fine

        for item_request in request.requests:
            product = self._product_catalog.get_by_name(item_request.product_name)

            if product is None:
                raise UnknownProductException()

            order.add_item(product, item_request.quantity)

        self._order_repository.save(order)
