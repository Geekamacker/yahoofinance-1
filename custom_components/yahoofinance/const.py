"""Constants for Yahoo Finance sensor."""

from __future__ import annotations

from datetime import timedelta
import logging
from typing import Final

# Additional attributes exposed by the sensor
ATTR_CURRENCY_SYMBOL: Final = "currencySymbol"
ATTR_QUOTE_TYPE: Final = "quoteType"
ATTR_QUOTE_SOURCE_NAME: Final = "quoteSourceName"
ATTR_SYMBOL: Final = "symbol"
ATTR_TRENDING: Final = "trending"
ATTR_MARKET_STATE: Final = "marketState"
ATTR_ESG_POPULATED: Final = "esgPopulated"
ATTR_DIVIDEND_DATE: Final = "dividendDate"
ATTR_EXDIVIDEND_DATE: Final = "exDividendDate"
ATTR_REGULAR_MARKET_TIME: Final = "regularMarketTime"
ATTR_PRE_MARKET_TIME: Final = "preMarketTime"
ATTR_POST_MARKET_TIME: Final = "postMarketTime"
ATTR_FORWARD_PE: Final = "forwardPE"
ATTR_TRAILING_PE: Final = "trailingPE"
ATTR_MARKET: Final = "market"
ATTR_EXCHANGE_TIMEZONE_NAME: Final = "exchangeTimezoneName"
ATTR_FULL_EXCHANGE_NAME: Final = "fullExchangeName"
ATTR_LONG_NAME: Final = "longName"


# Hass data
HASS_DATA_CONFIG: Final = "config"
HASS_DATA_COORDINATORS: Final = "coordinators"

# JSON data pieces
DATA_CURRENCY_SYMBOL: Final = "currency"
DATA_FINANCIAL_CURRENCY: Final = "financialCurrency"
DATA_QUOTE_TYPE: Final = "quoteType"
DATA_QUOTE_SOURCE_NAME: Final = "quoteSourceName"
DATA_SHORT_NAME: Final = "shortName"
DATA_MARKET_STATE: Final = "marketState"
DATA_ESG_POPULATED: Final = "esgPopulated"
DATA_DIVIDEND_DATE: Final = "dividendDate"
DATA_EXDIVIDEND_DATE: Final = "exDividendDate"
DATA_REGULAR_MARKET_TIME: Final = "regularMarketTime"
DATA_PRE_MARKET_TIME: Final = "preMarketTime"
DATA_POST_MARKET_TIME: Final = "postMarketTime"
DATA_FORWARD_PE: Final = "forwardPE"
DATA_TRAILING_PE: Final = "trailingPE"
DATA_MARKET: Final = "market"
DATA_EXCHANGE_TIMEZONE_NAME: Final = "exchangeTimezoneName"
DATA_FULL_EXCHANGE_NAME: Final = "fullExchangeName"
DATA_LONG_NAME: Final = "longName"


DATA_REGULAR_MARKET_PREVIOUS_CLOSE: Final = "regularMarketPreviousClose"
DATA_REGULAR_MARKET_PRICE: Final = "regularMarketPrice"

CONF_DECIMAL_PLACES: Final = "decimal_places"
CONF_INCLUDE_FIFTY_DAY_VALUES: Final = "include_fifty_day_values"
CONF_INCLUDE_POST_VALUES: Final = "include_post_values"
CONF_INCLUDE_PRE_VALUES: Final = "include_pre_values"
CONF_INCLUDE_TWO_HUNDRED_DAY_VALUES: Final = "include_two_hundred_day_values"
CONF_INCLUDE_FIFTY_TWO_WEEK_VALUES: Final = "include_fifty_two_week_values"
CONF_SHOW_TRENDING_ICON: Final = "show_trending_icon"
CONF_SHOW_CURRENCY_SYMBOL_AS_UNIT = "show_currency_symbol_as_unit"
CONF_TARGET_CURRENCY: Final = "target_currency"
CONF_NO_UNIT: Final = "no_unit"

DEFAULT_CONF_DECIMAL_PLACES: Final = 2
DEFAULT_CONF_INCLUDE_FIFTY_DAY_VALUES: Final = True
DEFAULT_CONF_INCLUDE_POST_VALUES: Final = True
DEFAULT_CONF_INCLUDE_PRE_VALUES: Final = True
DEFAULT_CONF_INCLUDE_TWO_HUNDRED_DAY_VALUES: Final = True
DEFAULT_CONF_INCLUDE_FIFTY_TWO_WEEK_VALUES: Final = True
DEFAULT_CONF_SHOW_TRENDING_ICON: Final = False
DEFAULT_CONF_SHOW_CURRENCY_SYMBOL_AS_UNIT: Final = False
DEFAULT_CONF_NO_UNIT: Final = False

DEFAULT_NUMERIC_DATA_GROUP: Final = "default"

# Data keys grouped into categories. The values for the categories except for
# DEFAULT_NUMERIC_DATA_GROUP can be conditionally pulled into attributes. The
# first value of the set is the key and the second boolean value indicates if
# the attribute is a currency.
NUMERIC_DATA_GROUPS: Final = {
    DEFAULT_NUMERIC_DATA_GROUP: [
        ("averageDailyVolume10Day", False),
        ("averageDailyVolume3Month", False),
        ("regularMarketChange", True),
        ("regularMarketChangePercent", False),
        ("regularMarketDayHigh", True),
        ("regularMarketDayLow", True),
        (DATA_REGULAR_MARKET_PREVIOUS_CLOSE, True),
        (DATA_REGULAR_MARKET_PRICE, True),
        ("regularMarketVolume", False),
        (DATA_REGULAR_MARKET_TIME, False),
        (DATA_DIVIDEND_DATE, False),
        (DATA_EXDIVIDEND_DATE, False),
        (DATA_FORWARD_PE, False),
        (DATA_TRAILING_PE, False),
        ("ask", True),
        ("beta", False),
        ("bid", True),
        ("bookValue", True),
        ("dividendRate", True),
        ("dividendYield", False),
        ("epsForward", True),
        ("epsTrailingTwelveMonths", True),
        ("pegRatio", False),
        ("priceHint", False),
        ("priceToBook", False),
        ("priceToSales", False),
        ("regularMarketOpen", True),
        ("shortRatio", False),
        ("trailingAnnualDividendRate", True),
        ("trailingAnnualDividendYield", False),
        ("askSize", False),
        ("bidSize", False),
        ("heldPercentInsiders", False),
        ("heldPercentInstitutions", False),
        ("floatShares", False),
        ("marketCap", False),
        ("sharesOutstanding", False),
        ("sharesShort", False),
        ("impliedSharesOutstanding", False),
    ],
    CONF_INCLUDE_FIFTY_DAY_VALUES: [
        ("fiftyDayAverage", True),
        ("fiftyDayAverageChange", True),
        ("fiftyDayAverageChangePercent", False),
    ],
    CONF_INCLUDE_PRE_VALUES: [
        ("preMarketChange", True),
        ("preMarketChangePercent", False),
        (DATA_PRE_MARKET_TIME, False),
        ("preMarketPrice", True),
    ],
    CONF_INCLUDE_POST_VALUES: [
        ("postMarketChange", True),
        ("postMarketChangePercent", False),
        ("postMarketPrice", True),
        (DATA_POST_MARKET_TIME, False),
    ],
    CONF_INCLUDE_TWO_HUNDRED_DAY_VALUES: [
        ("twoHundredDayAverage", True),
        ("twoHundredDayAverageChange", True),
        ("twoHundredDayAverageChangePercent", False),
    ],
    CONF_INCLUDE_FIFTY_TWO_WEEK_VALUES: [
        ("fiftyTwoWeekLow", True),
        ("fiftyTwoWeekLowChange", True),
        ("fiftyTwoWeekLowChangePercent", False),
        ("fiftyTwoWeekHigh", True),
        ("fiftyTwoWeekHighChange", True),
        ("fiftyTwoWeekHighChangePercent", False),
    ],
}

PERCENTAGE_DATA_KEYS_NEEDING_MULTIPLICATION: Final = [
    "fiftyDayAverageChangePercent",
    "twoHundredDayAverageChangePercent",
    "fiftyTwoWeekLowChangePercent",
    "fiftyTwoWeekHighChangePercent",
    "trailingAnnualDividendYield",
]


# Defaults for missing numeric keys
NUMERIC_DATA_DEFAULTS: Final = {DATA_DIVIDEND_DATE: None}

STRING_DATA_KEYS: Final = [
    DATA_CURRENCY_SYMBOL,
    DATA_FINANCIAL_CURRENCY,
    DATA_QUOTE_TYPE,
    DATA_QUOTE_SOURCE_NAME,
    DATA_SHORT_NAME,
    DATA_MARKET_STATE,
    DATA_ESG_POPULATED,
    DATA_MARKET,
    DATA_EXCHANGE_TIMEZONE_NAME,
    DATA_FULL_EXCHANGE_NAME,
    DATA_LONG_NAME,
]


ATTRIBUTION: Final = "Data provided by Yahoo Finance"
BASE: Final = "https://query2.finance.yahoo.com/v7/finance/quote?fields=region,quoteType,quoteSourceName,triggerable,customPriceAlertConfidence,regularMarketChangePercent,regularMarketPrice,exchangeTimezoneName,exchangeTimezoneShortName,market,currency,marketState,exchange,longName,hasPrePostMarketData,priceHint,totalCash,floatShares,shortRatio,heldPercentInsiders,heldPercentInstitutions,postMarketChangePercent,postMarketTime,postMarketPrice,postMarketChange,regularMarketChange,regularMarketTime,regularMarketDayHigh,regularMarketDayLow,regularMarketVolume,sharesShort,regularMarketPreviousClose,bid,ask,bidSize,askSize,fullExchangeName,financialCurrency,regularMarketOpen,averageDailyVolume3Month,averageDailyVolume10Day,beta,fiftyTwoWeekLowChange,fiftyTwoWeekLowChangePercent,fiftyTwoWeekHighChange,fiftyTwoWeekHighChangePercent,fiftyTwoWeekLow,fiftyTwoWeekHigh,dividendDate,exDividendDate,isEarningsDateEstimate,trailingAnnualDividendRate,trailingPE,pegRatio,dividendRate,trailingAnnualDividendYield,dividendYield,revenue,priceToSales,epsTrailingTwelveMonths,epsForward,sharesOutstanding,impliedSharesOutstanding,bookValue,fiftyDayAverage,fiftyDayAverageChange,fiftyDayAverageChangePercent,twoHundredDayAverage,twoHundredDayAverageChange,twoHundredDayAverageChangePercent,marketCap,preMarketChange,preMarketChangePercent,preMarketTime,preMarketPrice&symbols="

INITIAL_URL: Final = "https://finance.yahoo.com/quote/NQ%3DF/"
CONSENT_HOST: Final = "consent.yahoo.com"
GET_CRUMB_URL: Final = "https://query2.finance.yahoo.com/v1/test/getcrumb"

INITIAL_REQUEST_HEADERS: Final = {
    "accept": "text/html,application/xhtml+xml,application/xml",
    "accept-language": "en-US,en;q=0.9",
}
""" Headers for INITIAL_URL. The limited headers are an attempt to avoid `Got more than 8190 byte` error. """

USER_AGENTS_FOR_XHR: Final = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Mozilla/5.0",
]

XHR_REQUEST_HEADERS: Final = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip,deflate,br,zstd",
    "accept-language": "en-US,en;q=0.9",
}
""" Headers for all XHR requests. """

CONF_SYMBOLS: Final = "symbols"
DEFAULT_CURRENCY: Final = "USD"
DEFAULT_CURRENCY_SYMBOL: Final = "$"
DOMAIN: Final = "yahoofinance1"
SERVICE_REFRESH: Final = "refresh_symbols"

DEFAULT_SCAN_INTERVAL: Final = timedelta(hours=1)
MANUAL_SCAN_INTERVAL: Final = "manual"
MINIMUM_SCAN_INTERVAL: Final = timedelta(seconds=30)

CRUMB_RETRY_DELAY: Final = 15
"""Default duration for crumb re-try request."""

CRUMB_RETRY_DELAY_429: Final = 60
"""Duration for crumb re-try when receiving 429 code."""

TOO_MANY_CRUMB_RETRY_FAILURES_DELAY: Final = 300
TOO_MANY_CRUMB_RETRY_FAILURES_COUNT: Final = 5

CURRENCY_CODES: Final = {
    "aud": "$",
    "bdt": "৳",
    "brl": "R$",
    "btc": "₿",
    "cad": "CA$",
    "chf": "₣",
    "cny": "¥",
    "eth": "Ξ",
    "eur": "€",
    "gbp": "£",
    "hkd": "HK$",
    "ils": "₪",
    "inr": "₹",
    "jpy": "¥",
    "krw": "₩",
    "kzt": "лв",
    "mxn": "MX$",
    "ngn": "₦",
    "nzd": "NZ$",
    "php": "₱",
    "rial": "﷼",
    "rub": "₽",
    "sign": "",
    "try": "₺",
    "twd": "NT$",
    "usd": "$",
    "vnd": "₫",
    "xaf": "FCFA",
    "xcd": "EC$",
    "xof": "F\u202fCFA",
    "xpf": "CFPF",
    "xxx": "¤",
}

LOGGER = logging.getLogger(__package__)
