class InsufficientStockError(Exception):
    def __init__(self, item_name, available):
        self.item_name = item_name
        self.available = available
        super().__init__(f"\nInsufficient stock for '{item_name}' Available: {available}.")
