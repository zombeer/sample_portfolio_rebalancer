from decimal import Decimal

from rebalancer import Action, Order, Portfolio  # Replace 'your_module' with the actual name of your module


# Test for security value calculation
def test_security_value():
    securities = {"A": Decimal(10)}
    portfolio = Portfolio(securities, {"A": 5}, {})
    assert portfolio.security_value("A") == Decimal(50)


# Test for security percentages calculation
def test_security_percentages():
    securities = {"A": Decimal(10), "B": Decimal(20)}

    portfolio = Portfolio(securities, {"A": 5, "B": 2}, {})
    percentages = portfolio.security_percentages()
    total_value = Decimal(5 * 10 + 2 * 20)

    assert percentages["A"] == Decimal(50) / total_value
    assert percentages["B"] == Decimal(40) / total_value


# Test for portfolio rebalancing
def test_rebalance_2_orders():
    securities = {"A": Decimal(1), "B": Decimal(1)}
    portfolio = Portfolio(
        securities=securities,
        current_state={"A": 2, "B": 1},
        desired_state={"A": 1, "B": 2},
    )
    orders = portfolio.rebalance()

    assert len(orders) == 2  # noqa: PLR2004
    assert orders[0] == Order("A", Action.SELL, Decimal(1))
    assert orders[1] == Order("B", Action.BUY, Decimal(1))


# Test for portfolio rebalancing with no change
def test_rebalance_no_change():
    securities = {"A": Decimal(1), "B": Decimal(1)}
    portfolio = Portfolio(
        securities=securities,
        current_state={"A": 1, "B": 1},
        desired_state={"A": 1, "B": 1},
    )
    orders = portfolio.rebalance()

    assert len(orders) == 0


# Test for portfolio rebalancing with no securities
def test_rebalance_no_securities():
    securities = {}
    portfolio = Portfolio(securities, {}, {})
    orders = portfolio.rebalance()

    assert len(orders) == 0


# Test for portfolio rebalancing with no desired state
def test_rebalance_no_desired_state():
    securities = {"A": Decimal(1)}
    portfolio = Portfolio(securities, {"A": 1}, {})
    orders = portfolio.rebalance()

    assert len(orders) == 0


# Test for portfolio rebalancing with 3 securities
def test_rebalance_3_securities():
    securities = {"A": Decimal(1), "B": Decimal(1), "C": Decimal(1)}
    portfolio = Portfolio(
        securities=securities,
        current_state={"A": 3, "B": 2, "C": 1},
        desired_state={"A": 1, "B": 1, "C": 1},
    )
    orders = portfolio.rebalance()
    assert len(orders) == 2  # noqa: PLR2004
    assert orders[0] == Order("A", Action.SELL, Decimal(1))
    assert orders[1] == Order("C", Action.BUY, Decimal(1))


# Test desired_state normalization
def test_desired_state_normalization():
    desired_state1 = {"A": 1, "B": 1}
    desired_state2 = {"A": 100, "B": 100}

    current_state = {"A": 4, "B": 1}
    securities = {"A": Decimal(1), "B": Decimal(1)}

    p1 = Portfolio(securities, current_state, desired_state1)
    p2 = Portfolio(securities, current_state, desired_state2)

    assert p1.rebalance() == p2.rebalance()


# Test  float in desired_state
def test_float_in_desired_state():
    desired_state1 = {"A": 1, "B": 1}
    desired_state2 = {"A": 1.00, "B": 1.00}

    current_state = {"A": 4, "B": 1}
    securities = {"A": Decimal(1), "B": Decimal(1)}

    p1 = Portfolio(securities, current_state, desired_state1)
    p2 = Portfolio(securities, current_state, desired_state2)

    assert p1.rebalance() == p2.rebalance()
