import eth_abi

from forta_agent import FindingSeverity, create_transaction_event, create_block_event
from web3 import Web3
from eth_utils import keccak, encode_hex

from src.agent import provide_handle_transaction, provide_handle_block
from src.utils import get_protocols_by_chain

FREE_ETH_ADDRESS = "0xE0dD882D4dA747e9848D05584e6b42c6320868be"
protocols = get_protocols_by_chain(1)
protocols_addresses = list(map(lambda x: Web3.toChecksumAddress(x).lower(), protocols.values()))
SWAP = "Swap(address,address,int256,int256,uint160,uint128,int24)"


def swap_event(amount0, amount1, address_):
    hash = keccak(text=SWAP)
    data = eth_abi.encode_abi(["int256", "int256", "uint160", "uint128", "int24"], [amount0, amount1, 1, 1, 1])
    data = encode_hex(data)
    address1 = eth_abi.encode_abi(["address"], [FREE_ETH_ADDRESS])
    address1 = encode_hex(address1)
    address2 = eth_abi.encode_abi(["address"], [FREE_ETH_ADDRESS])
    address2 = encode_hex(address2)
    topics = [hash, address1, address2]
    return {'topics': topics,
            'data': data,
            'address': address_}


class TestSmartPriceChangeAgent:

    def test_returns_zero_finding_if_the_price_change_is_small(self):
        tx_event = create_transaction_event({
            'transaction': {
                'from': FREE_ETH_ADDRESS,
                'to': FREE_ETH_ADDRESS,

            },
            'block': {
                'number': 14506125,
                'timestamp': 1648894338,
            },
            'logs': [swap_event(2190163565, 1, '0x959c7d5706ac0b5a29f506a1019ba7f2a1c70c70')]})

        block_event = create_block_event({
            'block': {
                'number': 14506125,
                'timestamp': 1648894338,
            }
        })

        provide_handle_block()(block_event)
        findings = provide_handle_transaction()(tx_event)
        assert len(findings) == 0

    def test_returns_critical_findings_if_the_price_is_very_big(self):
        tx_event = create_transaction_event({
            'transaction': {
                'from': FREE_ETH_ADDRESS,
                'to': FREE_ETH_ADDRESS,

            },
            'block': {
                'number': 14506125,
                'timestamp': 1648894338,
            },
            'logs': [swap_event(2190163565000, 1, '0x959c7d5706ac0b5a29f506a1019ba7f2a1c70c70')]})

        findings = provide_handle_transaction()(tx_event)
        assert len(findings) == 1
        assert findings[0].severity == FindingSeverity.Critical

    def test_returns_critical_findings_if_the_price_is_very_low(self):
        tx_event = create_transaction_event({
            'transaction': {
                'from': FREE_ETH_ADDRESS,
                'to': FREE_ETH_ADDRESS,

            },
            'block': {
                'number': 14506125,
                'timestamp': 1648894338,
            },
            'logs': [swap_event(2, 1, '0x959c7d5706ac0b5a29f506a1019ba7f2a1c70c70')]})

        findings = provide_handle_transaction()(tx_event)
        assert len(findings) == 1
        assert findings[0].severity == FindingSeverity.Critical

    def test_for_price_and_pool_returns_zero_or_one_finding_depending_on_the_seasonality(self):
        tx_event = create_transaction_event({
            'transaction': {
                'from': FREE_ETH_ADDRESS,
                'to': FREE_ETH_ADDRESS,

            },
            'block': {
                'number': 14506125,
                'timestamp': 1648894338,
            },
            'logs': [swap_event(2890163565, 1, '0x959c7d5706ac0b5a29f506a1019ba7f2a1c70c70')]})

        findings = provide_handle_transaction()(tx_event)
        assert len(findings) == 1

        tx_event = create_transaction_event({
            'transaction': {
                'from': FREE_ETH_ADDRESS,
                'to': FREE_ETH_ADDRESS,

            },
            'block': {
                'number': 14506125,
                'timestamp': 1648897980,
            },
            'logs': [swap_event(2890163565, 1, '0x959c7d5706ac0b5a29f506a1019ba7f2a1c70c70')]})

        findings = provide_handle_transaction()(tx_event)
        assert len(findings) == 0
