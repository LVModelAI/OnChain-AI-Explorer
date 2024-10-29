import json
from .explorer_functions.account_functions import get_wallet_transactions
from .explorer_functions.account_functions import get_wallet_balance
from .explorer_functions.account_functions import get_wallets_balance
from .explorer_functions.account_functions import get_wallet_internal_transactions
from .explorer_functions.account_functions import get_wallet_erc20_transfers
from .explorer_functions.account_functions import get_wallet_erc721_transfers
from .explorer_functions.account_functions import get_wallet_erc1155_transfers
from .explorer_functions.account_functions import get_wallet_mined_blocks
from .explorer_functions.account_functions import get_wallet_beacon_withdrawals
from .explorer_functions.account_functions import get_internal_transactions_by_block_range
from .explorer_functions.account_functions import get_internal_transactions_by_hash

async def handle_function_call(function_obj, explorer_base_url, explorer_api_key):
    function_name = function_obj.function.name
    function_args = function_obj.function.arguments

    # Parsing the arguments
    function_args = json.loads(function_args)

    # Calling the appropriate function
    if function_name == "get_wallet_transactions":
        result = await get_wallet_transactions(
            wallet_address=function_args["wallet_address"],
            start_block=function_args.get("start_block", 0),
            end_block=function_args.get("end_block", 99999999),
            page=function_args.get("page", 1),
            offset=function_args.get("offset", 10),
            sort=function_args.get("sort", "asc"),
            explorer_api_key=explorer_api_key,
            explorer_base_url=explorer_base_url
        )
        return result

    elif function_name == "get_wallet_balance":
        result = await get_wallet_balance(
            wallet_address=function_args["wallet_address"],
            explorer_api_key=explorer_api_key,
            explorer_base_url=explorer_base_url
        )
        return result

    elif function_name == "get_wallets_balance":
        result = await get_wallets_balance(
            wallet_addresses=function_args["wallet_addresses"],
            explorer_api_key=explorer_api_key,
            explorer_base_url=explorer_base_url
        )
        return result

    elif function_name == "get_wallet_internal_transactions":
        result = await get_wallet_internal_transactions(
            wallet_address=function_args["wallet_address"],
            start_block=function_args.get("start_block", 0),
            end_block=function_args.get("end_block", 99999999),
            page=function_args.get("page", 1),
            offset=function_args.get("offset", 10),
            sort=function_args.get("sort", "asc"),
            explorer_api_key=explorer_api_key,
            explorer_base_url=explorer_base_url
        )
        return result

    elif function_name == "get_wallet_erc20_transfers":
        result = await get_wallet_erc20_transfers(
            wallet_address=function_args["wallet_address"],
            contract_address=function_args.get("contract_address", None),
            start_block=function_args.get("start_block", 0),
            end_block=function_args.get("end_block", 99999999),
            page=function_args.get("page", 1),
            offset=function_args.get("offset", 100),
            sort=function_args.get("sort", "asc"),
            explorer_api_key=explorer_api_key,
            explorer_base_url=explorer_base_url
        )
        return result

    elif function_name == "get_wallet_erc721_transfers":
        result = await get_wallet_erc721_transfers(
            wallet_address=function_args["wallet_address"],
            contract_address=function_args.get("contract_address", None),
            start_block=function_args.get("start_block", 0),
            end_block=function_args.get("end_block", 99999999),
            page=function_args.get("page", 1),
            offset=function_args.get("offset", 100),
            sort=function_args.get("sort", "asc"),
            explorer_api_key=explorer_api_key,
            explorer_base_url=explorer_base_url
        )
        return result

    elif function_name == "get_wallet_erc1155_transfers":
        result = await get_wallet_erc1155_transfers(
            wallet_address=function_args["wallet_address"],
            contract_address=function_args.get("contract_address", None),
            start_block=function_args.get("start_block", 0),
            end_block=function_args.get("end_block", 99999999),
            page=function_args.get("page", 1),
            offset=function_args.get("offset", 100),
            sort=function_args.get("sort", "asc"),
            explorer_api_key=explorer_api_key,
            explorer_base_url=explorer_base_url
        )
        return result

    elif function_name == "get_wallet_mined_blocks":
        result = await get_wallet_mined_blocks(
            wallet_address=function_args["wallet_address"],
            block_type=function_args.get("block_type", "blocks"),
            page=function_args.get("page", 1),
            offset=function_args.get("offset", 10),
            explorer_api_key=explorer_api_key,
            explorer_base_url=explorer_base_url
        )
        return result

    elif function_name == "get_wallet_beacon_withdrawals":
        result = await get_wallet_beacon_withdrawals(
            wallet_address=function_args["wallet_address"],
            start_block=function_args.get("start_block", 0),
            end_block=function_args.get("end_block", 99999999),
            page=function_args.get("page", 1),
            offset=function_args.get("offset", 100),
            sort=function_args.get("sort", "asc"),
            explorer_api_key=explorer_api_key,
            explorer_base_url=explorer_base_url
        )
        return result
    
    elif function_name == "get_internal_transactions_by_hash":
        result = await get_internal_transactions_by_hash(
            tx_hash=function_args["tx_hash"],
            explorer_base_url=explorer_base_url,
            explorer_api_key=explorer_api_key
        )
        return result
        
    elif function_name == "get_internal_transactions_by_block_range":
        result = await get_internal_transactions_by_block_range(
            start_block=function_args.get("start_block", 0),
            end_block=function_args.get("end_block", 99999999),
            explorer_base_url=explorer_base_url,
            explorer_api_key=explorer_api_key,
            page=function_args.get("page", 1),
            offset=function_args.get("offset", 10),
            sort=function_args.get("sort", "asc")
        )
        return result

    else:
        return "Function not found!"