from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class Action(Enum):
    """Enum for Order action."""

    BUY = "BUY"
    SELL = "SELL"


@dataclass
class Security:
    """Abstract class for Security."""

    symbol: str
    price: Decimal
    precision: int


@dataclass
class Order:
    """Abstract class for Order."""

    security: Security
    quantity: Decimal
    action: Action


@dataclass
class Portfolio:
    """Class for Portfolio."""

    securities: dict[str, Security]
    desired_allocation: dict[str, Decimal]
