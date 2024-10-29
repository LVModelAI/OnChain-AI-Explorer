from openai import OpenAI
import json

# function definitions provided to the model
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_wallet_transactions",
            "description": "Fetch Ethereum transactions for a wallet address whenever user ask to show his last transactions. if user has not provided wallet address, ask for wallet address. if user has not provided number of transactions, default it to 5",
            "parameters": {
                "type": "object",
                "properties": {
                    "wallet_address": {
                        "type": "string",
                        "description": "Ethereum wallet address."
                    },
                    "num_of_transactions": {
                        "type": "number",
                        "description": "Number of transactions to fetch. Take default value as 5."
                    },
                    "start_block": {
                        "type": "number",
                        "description": "The starting block number to search for transactions. Default is 0."
                    },
                    "end_block": {
                        "type": "number",
                        "description": "The ending block number to search for transactions. Default is 99999999."
                    },
                    "page": {
                        "type": "number",
                        "description": "The page number for pagination. Default is 1."
                    },
                    "offset": {
                        "type": "number",
                        "description": "The number of transactions to display per page. Default is 10."
                    },
                    "sort": {
                        "type": "string",
                        "description": "The sorting order for the transactions. Can be 'asc' or 'desc'. Default is 'asc'."
                    }
                },
                "required": ["wallet_address", "num_of_transactions"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_wallet_balance",
            "description": "Fetch the Ether balance for a given Ethereum wallet address. If the user has not provided a wallet address, ask for the wallet address.",
            "parameters": {
                "type": "object",
                "properties": {
                    "wallet_address": {
                        "type": "string",
                        "description": "Ethereum wallet address."
                    }
                },
                "required": ["wallet_address"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_wallets_balance",
            "description": "Fetch the Ether balances for a list of Ethereum wallet addresses.",
            "parameters": {
                "type": "object",
                "properties": {
                    "wallet_addresses": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "A list of Ethereum wallet addresses."
                    }
                },
                "required": ["wallet_addresses"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_wallet_internal_transactions",
            "description": "Fetch the list of internal transactions for a given Ethereum wallet address.",
            "parameters": {
                "type": "object",
                "properties": {
                    "wallet_address": {
                        "type": "string",
                        "description": "Ethereum wallet address."
                    },
                    "start_block": {
                        "type": "number",
                        "description": "The starting block number to search for internal transactions. Default is 0."
                    },
                    "end_block": {
                        "type": "number",
                        "description": "The ending block number to search for internal transactions. Default is 99999999."
                    },
                    "page": {
                        "type": "number",
                        "description": "The page number for pagination. Default is 1."
                    },
                    "offset": {
                        "type": "number",
                        "description": "The number of internal transactions to display per page. Default is 10."
                    },
                    "sort": {
                        "type": "string",
                        "description": "The sorting order for the internal transactions. Can be 'asc' or 'desc'. Default is 'asc'."
                    }
                },
                "required": ["wallet_address"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_wallet_erc20_transfers",
            "description": "Fetch the list of ERC20 token transfers for a given Ethereum wallet address.",
            "parameters": {
                "type": "object",
                "properties": {
                    "wallet_address": {
                        "type": "string",
                        "description": "Ethereum wallet address."
                    },
                    "contract_address": {
                        "type": "string",
                        "description": "The contract address of the ERC20 token. If not provided, will fetch transfers for all ERC20 tokens."
                    },
                    "start_block": {
                        "type": "number",
                        "description": "The starting block number to search for ERC20 transfers. Default is 0."
                    },
                    "end_block": {
                        "type": "number",
                        "description": "The ending block number to search for ERC20 transfers. Default is 99999999."
                    },
                    "page": {
                        "type": "number",
                        "description": "The page number for pagination. Default is 1."
                    },
                    "offset": {
                        "type": "number",
                        "description": "The number of ERC20 transfers to display per page. Default is 100."
                    },
                    "sort": {
                        "type": "string",
                        "description": "The sorting order for the ERC20 transfers. Can be 'asc' or 'desc'. Default is 'asc'."
                    }
                },
                "required": ["wallet_address"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_wallet_erc721_transfers",
            "description": "Fetch the list of ERC721 (NFT) token transfers for a given Ethereum wallet address.",
            "parameters": {
                "type": "object",
                "properties": {
                    "wallet_address": {
                        "type": "string",
                        "description": "Ethereum wallet address."
                    },
                    "contract_address": {
                        "type": "string",
                        "description": "The contract address of the ERC721 token. If not provided, will fetch transfers for all ERC721 tokens."
                    },
                    "start_block": {
                        "type": "number",
                        "description": "The starting block number to search for ERC721 transfers. Default is 0."
                    },
                    "end_block": {
                        "type": "number",
                        "description": "The ending block number to search for ERC721 transfers. Default is 99999999."
                    },
                    "page": {
                        "type": "number",
                        "description": "The page number for pagination. Default is 1."
                    },
                    "offset": {
                        "type": "number",
                        "description": "The number of ERC721 transfers to display per page. Default is 100."
                    },
                    "sort": {
                        "type": "string",
                        "description": "The sorting order for the ERC721 transfers. Can be 'asc' or 'desc'. Default is 'asc'."
                    }
                },
                "required": ["wallet_address"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_wallet_erc1155_transfers",
            "description": "Fetch the list of ERC1155 token transfers for a given Ethereum wallet address.",
            "parameters": {
                "type": "object",
                "properties": {
                    "wallet_address": {
                        "type": "string",
                        "description": "Ethereum wallet address."
                    },
                    "contract_address": {
                        "type": "string",
                        "description": "The contract address of the ERC1155 token. If not provided, will fetch transfers for all ERC1155 tokens."
                    },
                    "start_block": {
                        "type": "number",
                        "description": "The starting block number to search for ERC1155 transfers. Default is 0."
                    },
                    "end_block": {
                        "type": "number",
                        "description": "The ending block number to search for ERC1155 transfers. Default is 99999999."
                    },
                    "page": {
                        "type": "number",
                        "description": "The page number for pagination. Default is 1."
                    },
                    "offset": {
                        "type": "number",
                        "description": "The number of ERC1155 transfers to display per page. Default is 100."
                    },
                    "sort": {
                        "type": "string",
                        "description": "The sorting order for the ERC1155 transfers. Can be 'asc' or 'desc'. Default is 'asc'."
                    }
                },
                "required": ["wallet_address"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_wallet_mined_blocks",
            "description": "Fetch the list of blocks mined by a given Ethereum wallet address.",
            "parameters": {
                "type": "object",
                "properties": {
                    "wallet_address": {
                        "type": "string",
                        "description": "Ethereum wallet address."
                    },
                    "block_type": {
                        "type": "string",
                        "description": "The type of blocks to fetch. Can be 'blocks' for canonical blocks or 'uncles' for uncle blocks. Default is 'blocks'."
                    },
                    "page": {
                        "type": "number",
                        "description": "The page number for pagination. Default is 1."
                    },
                    "offset": {
                        "type": "number",
                        "description": "The number of blocks to display per page. Default is 10."
                    }
                },
                "required": ["wallet_address"],
                "additionalProperties": False
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "get_internal_transactions_by_hash",
        "description": "Fetch the list of internal transactions performed within a specific transaction.",
        "parameters": {
            "type": "object",
            "properties": {
                "tx_hash": {
                    "type": "string",
                    "description": "The transaction hash to check for internal transactions."
                }
            },
            "required": ["tx_hash"],
            "additionalProperties": False
        }
    }
},
    {
    "type": "function",
    "function": {
        "name": "get_internal_transactions_by_block_range",
        "description": "Fetch the list of internal transactions performed within a specified block range.",
        "parameters": {
            "type": "object",
            "properties": {
                "start_block": {
                    "type": "number",
                    "description": "The starting block number to search for transactions. Default is 0."
                },
                "end_block": {
                    "type": "number",
                    "description": "The ending block number to search for transactions. Default is 99999999."
                },
                "page": {
                    "type": "number",
                    "description": "The page number for pagination. Default is 1."
                },
                "offset": {
                    "type": "number",
                    "description": "The number of transactions to display per page. Maximum is 10000. Default is 10."
                },
                "sort": {
                    "type": "string",
                    "description": "The sorting preference. Use 'asc' for ascending and 'desc' for descending. Default is 'asc'."
                }
            },
            "required": ["start_block", "end_block"],
            "additionalProperties": False
        }
    }
},
    {
        "type": "function",
        "function": {
            "name": "get_wallet_beacon_withdrawals",
            "description": "Fetch the list of beacon chain withdrawals for a given Ethereum wallet address.",
            "parameters": {
                "type": "object",
                "properties": {
                    "wallet_address": {
                        "type": "string",
                        "description": "Ethereum wallet address."
                    },
                    "start_block": {
                        "type": "number",
                        "description": "The starting block number to search for beacon chain withdrawals. Default is 0."
                    },
                    "end_block": {
                        "type": "number",
                        "description": "The ending block number to search for beacon chain withdrawals. Default is 99999999."
                    },
                    "page": {
                        "type": "number",
                        "description": "The page number for pagination. Default is 1."
                    },
                    "offset": {
                        "type": "number",
                        "description": "The number of beacon chain withdrawals to display per page. Default is 100."
                    },
                    "sort": {
                        "type": "string",
                        "description": "The sorting order for the beacon chain withdrawals. Can be 'asc' or 'desc'. Default is 'asc'."
                    }
                },
                "required": ["wallet_address"],
                "additionalProperties": False
            }
        }
    }
]

async def get_func_using_nlp(openai_api_key: str, prompt: str) -> (str):
    print("Understanding the query and determining suitable function call...\n")
    client = OpenAI(api_key=openai_api_key)
    # initialize the openai client
    # Initial system message for the assistant
    messages = [
        {"role": "system", "content": "You are an assistant who decides which function to call based on user input."},
        {"role": "user", "content": prompt}
    ]

    # Request model completion with function-calling capabilities
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=messages,
        tools=tools
    )
    # Extract the function name the model selects, if available
    response = response.choices[0]
    # print(" response ---------" , response)
                    
    # # if function call detected content will be None and response will have tool_calls
    if(response.message.content == None and response.message.tool_calls):
        # print("Tool call detected", response.message.tool_calls[0])
        function_obj = response.message.tool_calls[0]
        return {
            "status":"ok", 
            "function_obj":function_obj
        }
    
    else:
        return {
            "status":"error", 
        }
