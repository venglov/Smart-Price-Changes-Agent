from src.config import ETHER_protocols, POLYGON_protocols, AVALANCHE_protocols, known_contracts


def extract_argument(event: dict, argument: str) -> any:
    """
    the function extract specified argument from the event
    :param event: dict
    :param argument: str
    :return: argument value
    """
    return event.get('args', {}).get(argument, "")


def get_protocols_by_chain(chain_id):
    if chain_id == 1:
        return ETHER_protocols
    elif chain_id == 137:
        return POLYGON_protocols
    elif chain_id == 43114:
        return AVALANCHE_protocols


def get_key_by_value(my_dict: dict, value):
    try:
        return list(my_dict.keys())[[x.lower() for x in my_dict.values()].index(value)]
    except Exception as _:
        return "Unknown Protocol"


def get_full_info(object_inst):
    values = vars(object_inst)
    values['block'] = vars(values['block'])
    values['logs'] = [vars(log) for log in values['logs']]
    values['traces'] = [vars(trace) for trace in values['traces']]
    values['transaction'] = vars(values['transaction'])

    return values


def get_token_name(contract, abi, web3):
    token_contract = web3.eth.contract(address=contract, abi=abi)
    try:
        name = token_contract.functions.name().call()
    except Exception as _:
        name = contract
        for known_contract in list(known_contracts.keys()):
            if known_contract == contract:
                name = known_contracts.get(contract, contract)
                break

    return name
