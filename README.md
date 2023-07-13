# **Smart Price Changes Agent - Rug Pulls**

---

## Description

This agent monitors any critical price changes for all trading pools for all protocols that support the pool's
Uniswap-like ABI (at least 3500+ pools on one Ethereum network). The price in each pool is analyzed separately using
machine learning, namely the Prophet library. All information is stored in a local asynchronous database, which ensures
the reliability of information storage in case of unexpected node failures.

## Features

- Fully asynchronous local database
- Bot is stable after the sudden restart
- Prices are analyzed for each protocol separately
- Works for all pools with Uniswap-like ABI for all protocols in all networks

## Chains

- Full support
    - Ethereum
    - Polygon - should work but requires more tests
    - Avalanche - should work but requires more tests
    - Fantom - should work but requires more tests
    - BSC - should work but requires more tests
    - Optimism - should work but requires more tests
    - Arbitrum - should work but requires more tests

## Settings

You can specify your own settings in the `src/config.py`:

```python
test_mode = False  # The mode when the bot uses test database
debug_logs_enabled = False  # Print the debug logs
history_capacity = 6300 * 4  # The amount of blocks to store in the database
minimal_capacity_to_forecast = 100  # The minimal amount of the blocks to start forecasting
critical_enable = True  # Enables critical alerts
high_enable = False  # Enables high alerts
medium_enable = False  # Enables medium alerts
low_enable = False  # Enables low alerts
```

## Alerts

- SMART-PRICE-CHANGES
    - Fired when the token price is very different from the forecasted value
    - Severity depends on how higher it is:
        - `Critical` - abs(token price - forecasted price) > 2 * (forecasted upper price - forecasted lower price)
        - `High` - abs(token price - forecasted fee) > 1.5 * (forecasted upper price - forecasted lower price)
        - `Medium` - abs(token price - forecasted fee) > forecasted upper price - forecasted lower price
        - `Low` - token price > forecasted price upper or token price < forecasted price lower
    - Type is always set to "Suspicious"
    - Metadata contains:
        - `protocol_address` - the address of the protocol
        - `pool_address` - the address of the pool
        - `pool_name` - the name of the pool
        - `excepted_price` - the forecasted price
        - `real_price` - real price in the Swap event
        - `tx_hash` - the hash of the transaction

## Tests

Tests and test data use database preset `test/database_presets/test_14442765-14489802.db` that contains real collected
data. It should be moved to `./test.db` e.g.

```bash
cp ./test/database_presets/test.db ./test.db
```

There are 4 tests that should pass:

```python
test_returns_zero_finding_if_the_price_change_is_small()
test_returns_critical_findings_if_the_price_is_very_big()
test_returns_critical_findings_if_the_price_is_very_low()
test_for_price_and_pool_returns_zero_or_one_finding_depending_on_the_seasonality()
```

## Test Data

Example of the alert:

```
1 findings for transaction 0xbfc18c36a4ee0d3f052c1d4a91ee9af03b3a72086f0f5f9516b94b8bda848688 {
  "name": "Critical Shina Inu/Wrapped Ether Price Changes in Uniswap",
  "description": "Price changes Shina Inu/Wrapped Ether in Uniswap is critically higher than excepted!",
  "alertId": "SMART-PRICE-CHANGES",
  "protocol": "ethereum",
  "severity": "Critical",
  "type": "Suspicious",
  "metadata": {
    "protocol_address": "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45",
    "pool_address": "0x959c7d5706ac0b5a29f506a1019ba7f2a1c70c70",
    "pool_name": "Shina Inu/Wrapped Ether",
    "excepted_price": 2194735087,
    "real_price": 3236835676.966687,
    "tx_hash": "0xbfc18c36a4ee0d3f052c1d4a91ee9af03b3a72086f0f5f9516b94b8bda848688"
  },
  "addresses": []
}

```
