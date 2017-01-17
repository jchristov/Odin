from odin.portfolio import InteractiveBrokersPortfolio
from odin.utilities import params
from odin.handlers.fund_handler import FundHandler
from odin.fund import Fund
from handlers import events, dh, eh, posh_long, porth_long
from settings import (
    rebalance_period, manage_period, start_date, verbosity, delay, account
)
from strategy import BuySellStrategy


# Generate objects for the portfolios and strategies that the fund will trade.
portfolios = [
    InteractiveBrokersPortfolio(dh, posh_long, porth_long, account),
]
strategies = [
    BuySellStrategy(params.Directions.long_dir, portfolios[0]),
]
# Create the fund and fund handler objects.
fh = FundHandler(
    events, strategies, rebalance_period, manage_period, start_date
)
fund = Fund(dh, eh, fh, delay, verbosity)
