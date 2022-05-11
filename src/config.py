test_mode = False  # The mode when the bot uses test database
debug_logs_enabled = True  # Print the debug logs
history_capacity = 6300  # The amount of blocks to store in the database
minimal_capacity_to_forecast = 20  # The minimal amount of swaps for the pool to start forecasting
critical_enable = True  # Enables critical alerts
high_enable = False  # Enables high alerts
medium_enable = False  # Enables medium alerts
low_enable = False  # Enables low alerts

#
# All the information below is just used to make the alerts more informative. The agent can work without the information
# below
#

known_contracts = {
    '0x4cb18386e5d1f34dc6eea834bf3534a970a3f8e7': 'USDC'
}

# Specify your own protocols for the Ethereum here
ETHER_protocols = {
    "Uniswap": "0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45",
    "1Inch": "0x1111111254fb6c44bAC0beD2854e76F90643097d",
    "Metamask_DEX": "0x881D40237659C251811CEC9c364ef91dC08D300C",
    "MevBot": "0x4cb18386e5d1f34dc6eea834bf3534a970a3f8e7"
}

# Specify your own protocols for the Polygon here
POLYGON_protocols = {
    "Uniswap": "0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"
}

# Specify your own protocols for the Avalanche here
AVALANCHE_protocols = {
    "JoeRouter": "0x60aE616a2155Ee3d9A68541Ba4544862310933d4"
}

# Specify your own protocols for the Fantom here
FANTOM_protocols = {
    "SpookySwap": "0xF491e7B69E4244ad4002BC14e878a34207E38c29"
}

# Specify your own protocols for the BSC here
BSC_protocols = {
    "PancakeSwap": "0x10ED43C718714eb63d5aA57B78B54704E256024E"
}

# Specify your own protocols for the OPTIMISM here
OPTIMISM_protocols = {

}

# Specify your own protocols for the ARBITRUM here
ARBITRUM_protocols = {

}
