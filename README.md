## Summary

A forked custom component from iprak to display stock information with a few added attributes from [Yahoo finance](https://finance.yahoo.com/).
Please go to the main yahoofinance to donate as this wouldn't be possible with their contribution. [iprak](https://github.com/iprak/yahoofinance).


Note: ```This integration will most only work in US mainland. Data privacy requirements like GDPR can cause requests to fail. This is as of release 1.2.12.```

## Installation

This can be installed by copying all the files from `custom_components/yahoofinance/` to `<config directory>/custom_components/yahoofinance/`.

## Configuration

Define the symbols to be tracked and optional parameters in `configuration.yaml`.

```yaml
# Example configuration.yaml entry
yahoofinance:
  symbols:
    - ISTNX
```

The above configuration will generate an entity with the id `sensor.yahoofinance1_SPGI` and current value as the state along with these attributes:

```
state_class: measurement
attribution: Data provided by Yahoo Finance
currencySymbol: $
symbol: SPGI
quoteType: EQUITY
quoteSourceName: Delayed Quote
marketState: POSTPOST
averageDailyVolume10Day: 1158610
averageDailyVolume3Month: 1178613
regularMarketChange: -3.79
regularMarketChangePercent: -0.71
regularMarketDayHigh: 531.22
regularMarketDayLow: 524.6
regularMarketPreviousClose: 530.18
regularMarketPrice: 526.39
regularMarketVolume: 890839
regularMarketTime: 2025-07-08T15:00:02-05:00
dividendDate: 2025-09-09
exDividendDate: 2025-08-25
forwardPE: 31.31
trailingPE: 41.68
ask: 531.84
beta: 1.2
bid: 524
bookValue: 108.81
dividendRate: 3.84
dividendYield: 0.73
epsForward: 16.81
epsTrailingTwelveMonths: 12.63
pegRatio: 0
priceHint: 2
priceToBook: 4.84
priceToSales: 11.22
regularMarketOpen: 529.99
shortRatio: 2.39
trailingAnnualDividendRate: 3.69
trailingAnnualDividendYield: 0.7
askSize: 1
bidSize: 1
heldPercentInsiders: 0.18
heldPercentInstitutions: 89.81
floatShares: 306028327
marketCap: 162597142528
sharesOutstanding: 306683008
sharesShort: 2600532
impliedSharesOutstanding: 308891008
fiftyDayAverage: 512.1
fiftyDayAverageChange: 14.29
fiftyDayAverageChangePercent: 2.79
preMarketChange: -1.08
preMarketChangePercent: -0.2
preMarketTime: 2025-07-08T08:17:58-05:00
preMarketPrice: 529.05
postMarketChange: 0
postMarketChangePercent: 0
postMarketPrice: 526.39
postMarketTime: 2025-07-08T18:38:18-05:00
twoHundredDayAverage: 506.89
twoHundredDayAverageChange: 19.5
twoHundredDayAverageChangePercent: 3.85
fiftyTwoWeekLow: 427.14
fiftyTwoWeekLowChange: 99.25
fiftyTwoWeekLowChangePercent: 23.24
fiftyTwoWeekHigh: 545.39
fiftyTwoWeekHighChange: -19
fiftyTwoWeekHighChangePercent: -3.48
esgPopulated: false
exchangeTimezoneName: America/New_York
fullExchangeName: NYSE
longName: S&P Global Inc.
market: us_market
trending: down
unit_of_measurement: USD
icon: mdi:trending-down
friendly_name: SPGI
```

#### Attributes
* The attributes can be null if there is no data present.
* The `dividendDate` is in ISO format (YYYY-MM-DD).



## Optional Configuration

### Integration

- Data fetch interval can be adjusted by specifying the `scan_interval` setting whose default value is 6 hours and the minimum value is 30 seconds.

  ```yaml
  scan_interval:
    hours: 4
  ```

  You can disable automatic update by passing `manual` for `scan_interval`.

- Trending icons (trending-up, trending-down or trending-neutral) can be displayed instead of currency based icon by specifying `show_trending_icon`.
  ```yaml
  show_trending_icon: true
  ```
- All numeric values are by default rounded to 2 places of decimal. This can be adjusted by the `decimal_places` setting. A value of 0 will return in integer values and -1 will suppress rounding.

  ```yaml
  decimal_places: 3
  ```

- The fifty_day, post, pre and two_hundred attributes can be suppressed as following. They are included by default.
  ```yaml
  include_fifty_day_values: false
  include_fifty_two_week_values: false
  include_post_values: false
  include_pre_values: false
  include_two_hundred_day_values: false
  ```

- The currency symbol e.g. $ can be show as the unit instead of USD by setting `show_currency_symbol_as_unit: true`.
  - **Note:** Using this setting will generate a warning like `The unit of this entity changed to '$' which can't be converted ...` You will have to manually resolve it by picking the first option to update the unit of the historicalvalues without convertion. This can be done from `Developer tools > STATISTICS`.


### Symbol

- An alternate target currency can be specified for a symbol using the extended declaration format. Here, the symbol EMIM.L is reported in USD but will be presented in EUR. The conversion would be based on the value of the symbol USDEUR=X.

  ```yaml
  symbols:
    - symbol: EMIM.L
      target_currency: EUR
  ```

  If data for the target currency is not found, then the display will remain in original currency. The conversion is only applied on the attributes representing prices.

- The data fetch interval can be fine tuned at symbol level. By default, the `scan_interval` from the integration is used. The minimum value is still 30 seconds. Symbols with the same `scan_interval` are grouped together and loaded through one data coordinator.

  If conversion data needs to be loaded, then that too will get added to the same coordinator. However, if conversion symbol is found in another coordinator, then that will get used.

  ```yaml
  scan_interval:
    hours: 4
  ```

  ```yaml
  scan_interval:
    minutes: 5
  ```

  ```yaml
  scan_interval: 300
  ```

- The `unit_of_measurement` can be suppressed by setting `no_unit: true`. This could be used for index symbols if no currency unit is desired to be displayed.

  ```yaml
    - symbol: BND
      no_unit: true
  ```
  - **Note:** Using this setting will generate a warning like `The unit of sensor.yahoofinance_gspc cannot be converted to the unit of previously compiled statistics (USD). Generation of long term statistics will be suppressed unless the unit changes back to USD or a compatible unit.` You will have to manually resolve it as mentioned in the message otherwise new data might not show in cards.

## Examples

- The symbol can also represent a financial index such as [this](https://finance.yahoo.com/world-indices/).

  ```yaml
  symbols:
    - ^SSMI
  ```

- Yahoo also provides currency conversion as a symbol.

  ```yaml
  symbols:
    - GBPUSD=X
  ```

- A complete sample

```
yahoofinance:
  include_post_values: false
  include_pre_values: false
  show_trending_icon: true
  decimal_places: 2
  scan_interval:
    hours: 4
  symbols:
    - USDINR=X
    - UNP
```

- The trending icons themselves cannot be colored but colors can be added using [lovelace-card-mod](https://github.com/thomasloven/lovelace-card-mod). Here [auto-entities](https://github.com/thomasloven/lovelace-auto-entities) is being used to simplify the code.

  ```yaml
  - type: custom:auto-entities
    card:
      type: entities
      title: Financial
    filter:
      include:
        - group: group.stocks
          options:
            entity: this.entity_id
            style: |
              :host {
                --paper-item-icon-color: {% set value=state_attr(config.entity,"trending") %}
                                        {% if value=="up" -%} green
                                        {% elif value=="down" -%} red
                                        {% else %} var(--paper-item-icon-color))
                                        {% endif %};
  ```

## Services

* The integration configuration can be reloaded from the `YAHOO FINANCE` option on `YAML` tab in `Developer tools`.

* The component exposes the service `yahoofinance.refresh_symbols` which can be used to refresh all the data.
