from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

securities = {}


class Action(Enum):
    """Enum for Order action."""

    BUY = "BUY"
    SELL = "SELL"


@dataclass
class Order:
    """Class for Order."""

    symbol: str
    action: Action
    quantity: Decimal


@dataclass
class Portfolio:
    """Class for Portfolio."""

    current_state: dict[str, Decimal] = field(default_factory=dict)
    desired_state: dict[str, Decimal] = field(default_factory=dict)

    def security_value(self, symbol: str) -> Decimal:
        """Calculate the value of a security in the portfolio."""
        security_price = securities[symbol]
        return security_price * Decimal(self.current_state.get(symbol, 0))

    def security_percentages(self) -> dict[str, Decimal]:
        """Calculate the percentage of each security in the portfolio."""
        total_value = sum(self.security_value(symbol) for symbol in self.current_state)
        return {
            symbol: self.security_value(symbol) / total_value
            for symbol in self.current_state
            if total_value != Decimal(0)
        }

    def rebalance(self) -> list[Order]:
        """Rebalance the portfolio."""
        orders = []
        total_desired = sum(self.desired_state.values())
        normalized_desired_state = {
            symbol: Decimal(value) / total_desired for symbol, value in self.desired_state.items()
        }
        total_value = sum(self.security_value(symbol) for symbol in self.current_state)

        for symbol, desired_ratio in normalized_desired_state.items():
            current_value = self.security_value(symbol)
            desired_value = total_value * desired_ratio
            quantity_change = (desired_value - current_value) / securities[symbol]
            action = Action.BUY if quantity_change > 0 else Action.SELL
            if quantity_change.__round__(12):
                orders.append(Order(symbol, action, abs(quantity_change)))

        return orders


if __name__ == "__main__":
    securities = {"A": Decimal(10), "B": Decimal(20), "C": Decimal(30)}

    # Desired allocation as parts
    desired_allocation = {"A": 1, "B": 1, "C": 1}

    # Current allocation as current quantities
    current_allocation = {"A": 10, "B": 10}

    p = Portfolio(current_allocation, desired_allocation)

    for order in p.rebalance():
        print(f"Symbol: {order.symbol}, Action: {order.action}, Quantity: {order.quantity.__round__(6)}")