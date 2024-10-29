import aiohttp

# Function to fetch the wallet balance for a single address
async def get_wallet_balance(wallet_address: str, explorer_base_url: str, explorer_api_key: str) -> dict:
    print(f"Fetching balance for wallet address: {wallet_address}")
    
    url = f"{explorer_base_url}?module=account&action=balance&address={wallet_address}&tag=latest&apikey={explorer_api_key}"
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_address or not wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch wallet balance"))
                return data
    except Exception as error:
        print(f"Error fetching balance: {error}")
        raise

# Function to fetch the wallet balances for multiple addresses
async def get_wallets_balance(wallet_addresses: list, explorer_base_url: str, explorer_api_key: str) -> dict:
    print(f"Fetching balances for {len(wallet_addresses)} wallet addresses")
    
    addresses_param = ",".join(wallet_addresses)
    url = f"{explorer_base_url}?module=account&action=balancemulti&address={addresses_param}&tag=latest&apikey={explorer_api_key}"
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_addresses or not all(address.startswith("0x") for address in wallet_addresses):
            raise ValueError("Invalid wallet addresses")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch wallet balances"))
                return data
    except Exception as error:
        print(f"Error fetching balances: {error}")
        raise

# Function to fetch the list of transactions for a given wallet address
async def get_wallet_transactions(wallet_address: str, explorer_base_url: str, explorer_api_key: str, start_block: int = 0, end_block: int = 99999999, page: int = 1, offset: int = 10, sort: str = "asc") -> dict:
    print(f"Fetching transactions for wallet address: {wallet_address}")
    
    url = f"{explorer_base_url}?module=account&action=txlist&address={wallet_address}&startblock={start_block}&endblock={end_block}&page={page}&offset={offset}&sort={sort}&apikey={explorer_api_key}"
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_address or not wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch wallet transactions"))
                return data
    except Exception as error:
        print(f"Error fetching transactions: {error}")
        raise

# Function to fetch the list of internal transactions for a given wallet address
async def get_wallet_internal_transactions(wallet_address: str, explorer_base_url: str, explorer_api_key: str, start_block: int = 0, end_block: int = 99999999, page: int = 1, offset: int = 10, sort: str = "asc") -> dict:
    print(f"Fetching internal transactions for wallet address: {wallet_address}")
    
    url = f"{explorer_base_url}?module=account&action=txlistinternal&address={wallet_address}&startblock={start_block}&endblock={end_block}&page={page}&offset={offset}&sort={sort}&apikey={explorer_api_key}"
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_address or not wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch wallet internal transactions"))
                return data
    except Exception as error:
        print(f"Error fetching internal transactions: {error}")
        raise

# Function to fetch the list of ERC20 token transfers for a given wallet address
async def get_wallet_erc20_transfers(wallet_address: str, explorer_base_url: str, explorer_api_key: str, contract_address: str = None, start_block: int = 0, end_block: int = 99999999, page: int = 1, offset: int = 100, sort: str = "asc") -> dict:
    print(f"Fetching ERC20 token transfers for wallet address: {wallet_address}")
    
    url = f"{explorer_base_url}?module=account&action=tokentx&address={wallet_address}&startblock={start_block}&endblock={end_block}&page={page}&offset={offset}&sort={sort}&apikey={explorer_api_key}"
    if contract_address:
        url += f"&contractaddress={contract_address}"
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_address or not wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch wallet ERC20 token transfers"))
                return data
    except Exception as error:
        print(f"Error fetching ERC20 token transfers: {error}")
        raise

# Function to fetch the list of ERC721 (NFT) token transfers for a given wallet address
async def get_wallet_erc721_transfers(wallet_address: str, explorer_base_url: str, explorer_api_key: str, contract_address: str = None, start_block: int = 0, end_block: int = 99999999, page: int = 1, offset: int = 100, sort: str = "asc") -> dict:
    print(f"Fetching ERC721 token transfers for wallet address: {wallet_address}")
    
    url = f"{explorer_base_url}?module=account&action=tokennfttx&address={wallet_address}&startblock={start_block}&endblock={end_block}&page={page}&offset={offset}&sort={sort}&apikey={explorer_api_key}"
    if contract_address:
        url += f"&contractaddress={contract_address}"
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_address or not wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch wallet ERC721 token transfers"))
                return data
    except Exception as error:
        print(f"Error fetching ERC721 token transfers: {error}")
        raise

# Function to fetch the list of ERC1155 token transfers for a given wallet address
async def get_wallet_erc1155_transfers(wallet_address: str, explorer_base_url: str, explorer_api_key: str, contract_address: str = None, start_block: int = 0, end_block: int = 99999999, page: int = 1, offset: int = 100, sort: str = "asc") -> dict:
    print(f"Fetching ERC1155 token transfers for wallet address: {wallet_address}")
    
    url = f"{explorer_base_url}?module=account&action=token1155tx&address={wallet_address}&startblock={start_block}&endblock={end_block}&page={page}&offset={offset}&sort={sort}&apikey={explorer_api_key}"
    if contract_address:
        url += f"&contractaddress={contract_address}"
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_address or not wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch wallet ERC1155 token transfers"))
                return data
    except Exception as error:
        print(f"Error fetching ERC1155 token transfers: {error}")
        raise

# Function to fetch the list of blocks validated by a given wallet address
async def get_wallet_mined_blocks(wallet_address: str, explorer_base_url: str, explorer_api_key: str, block_type: str = "blocks", page: int = 1, offset: int = 10) -> dict:
    print(f"Fetching mined blocks for wallet address: {wallet_address}")
    
    url = f"{explorer_base_url}?module=account&action=getminedblocks&address={wallet_address}&blocktype={block_type}&page={page}&offset={offset}&apikey={explorer_api_key}"
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_address or not wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch mined blocks"))
                return data
    except Exception as error:
        print(f"Error fetching mined blocks: {error}")
        raise

# Function to fetch the beacon chain withdrawals for a given wallet address
async def get_wallet_beacon_withdrawals(wallet_address: str, explorer_base_url: str, explorer_api_key: str, start_block: int = 0, end_block: int = 99999999, page: int = 1, offset: int = 100, sort: str = "asc") -> dict:
    print(f"Fetching beacon chain withdrawals for wallet address: {wallet_address}")
    
    url = f"{explorer_base_url}?module=account&action=txsBeaconWithdrawal&address={wallet_address}&startblock={start_block}&endblock={end_block}&page={page}&offset={offset}&sort={sort}&apikey={explorer_api_key}"
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_address or not wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch beacon chain withdrawals"))
                return data
    except Exception as error:
        print(f"Error fetching beacon chain withdrawals: {error}")
        raise
    
# Function to fetch the latest transactions for a given wallet address
async def get_wallet_transactions(wallet_address: str, num_transactions: int,explorer_base_url:str, explorer_api_key:str) -> dict:

    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_address or not wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address")
        
        if not num_transactions or num_transactions < 1:
            raise ValueError("Number of transactions must be greater than 0")
        
        params = {
            "module": "account",
            "action": "txlist",
            "address": wallet_address,
            "startblock": "0",
            "endblock": "99999999",
            "page": "1",
            "offset": str(num_transactions),
            "sort": "desc",
            "apikey": explorer_api_key,
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(explorer_base_url, params=params) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch transactions"))
                return data
    
    except Exception as error:
        print(f"Error fetching transactions: {error}")
        raise


# Function to fetch the wallet balance for a given wallet address
async def get_wallet_balance(wallet_address: str, explorer_base_url:str, explorer_api_key:str) -> dict:
    print(f"Fetching balance for wallet address: {wallet_address}")
    
    url = f"{explorer_base_url}?module=account&action=balance&address={wallet_address}&tag=latest&apikey={explorer_api_key}"
    
    try: 
        if not explorer_base_url:
            raise ValueError("Base URL is required")
        
        if not explorer_api_key:
            raise ValueError("API key is required")
        
        if not wallet_address or not wallet_address.startswith("0x"):
            raise ValueError("Invalid wallet address")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch transactions"))
                return data
                   
    except Exception as error:
        print(f"Error fetching balance: {error}")
        raise
    

async def get_internal_transactions_by_hash(
    tx_hash: str,
    explorer_base_url: str,
    explorer_api_key: str
) -> dict:
   
    print(f"Fetching internal transactions for hash: {tx_hash}")
    
    url = (
        f"{explorer_base_url}"
        f"?module=account"
        f"&action=txlistinternal"
        f"&txhash={tx_hash}"
        f"&apikey={explorer_api_key}"
    )
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
            
        if not explorer_api_key:
            raise ValueError("API key is required")
            
        if not tx_hash or not tx_hash.startswith("0x"):
            raise ValueError("Invalid transaction hash")
            
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch internal transactions"))
                return data
                
    except Exception as error:
        print(f"Error fetching internal transactions: {error}")
        raise

async def get_internal_transactions_by_block_range(
    start_block: int,
    end_block: int,
    explorer_base_url: str,
    explorer_api_key: str,
    page: int = 1,
    offset: int = 10,
    sort: str = "asc"
) -> dict:
 
    print(f"Fetching internal transactions from block {start_block} to {end_block}")
    
    url = (
        f"{explorer_base_url}"
        f"?module=account"
        f"&action=txlistinternal"
        f"&startblock={start_block}"
        f"&endblock={end_block}"
        f"&page={page}"
        f"&offset={offset}"
        f"&sort={sort}"
        f"&apikey={explorer_api_key}"
    )
    
    try:
        if not explorer_base_url:
            raise ValueError("Base URL is required")
            
        if not explorer_api_key:
            raise ValueError("API key is required")
            
        if start_block < 0 or end_block < start_block:
            raise ValueError("Invalid block range")
            
        if sort not in ["asc", "desc"]:
            raise ValueError("Sort must be either 'asc' or 'desc'")
            
        if offset > 10000:
            raise ValueError("Maximum offset is 10000 records")
            
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch internal transactions"))
                return data
                
    except Exception as error:
        print(f"Error fetching internal transactions: {error}")
        raise