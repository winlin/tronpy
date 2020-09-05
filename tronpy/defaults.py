CONF_MAINNET = {
    "fullnode": "https://api.trongrid.io",
    "event": "https://api.trongrid.io",
}

# The long running, maintained by the tron-us community
CONF_SHASTA = {
    "fullnode": "https://api.shasta.trongrid.io",
    "event": "https://api.shasta.trongrid.io",
    "faucet": "https://www.trongrid.io/faucet",
}

# Maintained by the official team
CONF_NILE = {
    "fullnode": "https://api.nileex.io",
    "event": "https://event.nileex.io",
    "faucet": "http://nileex.io/join/getJoinPage",
}

# Maintained by the official team
CONF_TRONEX = {
    "fullnode": "https://testhttpapi.tronex.io",
    "event": "https://testapi.tronex.io",
    "faucet": "http://testnet.tronex.io/join/getJoinPage",
}

ALL = {
    "mainnet": CONF_MAINNET,
    "nile": CONF_NILE,
    "shasta": CONF_SHASTA,
    "tronex": CONF_TRONEX,
}


def conf_for_name(name: str) -> dict:
    return ALL.get(name, None)

def merge_dicts(dict1, dict2):
    """ Recursively merges dict2 into dict1 """
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return dict2
    for k in dict2:
        if k in dict1:
            dict1[k] = merge_dicts(dict1[k], dict2[k])
        else:
            dict1[k] = dict2[k]
    return dict1