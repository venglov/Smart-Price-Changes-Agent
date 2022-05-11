from forta_agent import Finding, FindingType, FindingSeverity
from src.utils import get_key_by_value


class SmartPriceChangesFindings:

    @staticmethod
    def critical(protocols, protocol, pool, excepted_price, real_price, tx_hash, name0, name1):
        name = get_key_by_value(my_dict=protocols, value=protocol)
        return Finding({
            'name': f'Critical {name0}/{name1} Price Changes in {name}',
            'description': f'Price changes {name0}/{name1} in {name} '
                           f'is critically higher than excepted!',
            'alert_id': 'SMART-PRICE-CHANGES',
            'type': FindingType.Suspicious,
            'severity': FindingSeverity.Critical,
            'metadata': {
                'protocol_address': protocol,
                'pool_address': pool,
                'pool_name': f'{name0}/{name1}',
                'excepted_price': excepted_price,
                'real_price': real_price,
                'tx_hash': tx_hash,
            }
        })

    @staticmethod
    def high(protocols, protocol, pool, excepted_price, real_price, tx_hash, name0, name1):
        name = get_key_by_value(my_dict=protocols, value=protocol)
        return Finding({
            'name': f'High {name0}/{name1} Price Changes in {name}',
            'description': f'Price changes {name0}/{name1} in {name} '
                           f'is much higher than excepted!',
            'alert_id': 'SMART-PRICE-CHANGES',
            'type': FindingType.Suspicious,
            'severity': FindingSeverity.High,
            'metadata': {
                'protocol_address': protocol,
                'pool_address': pool,
                'pool_name': f'{name0}/{name1}',
                'excepted_price': excepted_price,
                'real_price': real_price,
                'tx_hash': tx_hash,
            }
        })

    @staticmethod
    def medium(protocols, protocol, pool, excepted_price, real_price, tx_hash, name0, name1):
        name = get_key_by_value(my_dict=protocols, value=protocol)
        return Finding({
            'name': f'Average Higher Then Excepted {name0}/{name1} Price Changes in {name}',
            'description': f'Price changes {name0}/{name1} in {name} '
                           f'is average higher than excepted!',
            'alert_id': 'SMART-PRICE-CHANGES',
            'type': FindingType.Info,
            'severity': FindingSeverity.Medium,
            'metadata': {
                'protocol_address': protocol,
                'pool_address': pool,
                'pool_name': f'{name0}/{name1}',
                'excepted_price': excepted_price,
                'real_price': real_price,
                'tx_hash': tx_hash,
            }
        })

    @staticmethod
    def low(protocols, protocol, pool, excepted_price, real_price, tx_hash, name0, name1):
        name = get_key_by_value(my_dict=protocols, value=protocol)
        return Finding({
            'name': f'A Little Bit Higher Then Excepted {name0}/{name1} Price Changes in {name}',
            'description': f'Price changes {name0}/{name1} in {name} '
                           f'is a little bit higher than excepted!',
            'alert_id': 'SMART-PRICE-CHANGES',
            'type': FindingType.Info,
            'severity': FindingSeverity.Low,
            'metadata': {
                'protocol_address': protocol,
                'pool_address': pool,
                'pool_name': f'{name0}/{name1}',
                'excepted_price': excepted_price,
                'real_price': real_price,
                'tx_hash': tx_hash,
            }
        })
