
import pytest
from aioresponses import aioresponses
import os
from web3ai import execute_function_from_prompt 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


# Initialize the functions
get_wallet_transactions, _ = execute_function_from_prompt(BASE_URL, API_KEY)

# test successful fetch
@pytest.mark.asyncio
async def test_get_wallet_transactions():
    wallet_address = "0x8f54751F441B7707AbA668f0cF4745daAE545D16"
    num_transactions = 5

    # Mock response data
    mock_response_data = {
        "status": "1",
        "message": "OK",
        "result": [
            {
                "hash": "0xTransactionHash1",
                "from": "0xFromAddress1",
                "to": "0xToAddress1",
                "value": "1000000000000000000",
                "gasUsed": "21000",
                "timeStamp": "1609459200",
                "functionName": "transfer"
            },
        ]
    }

    with aioresponses() as m:
        m.get(f"{BASE_URL}?module=account&action=txlist&address={wallet_address}&apikey={API_KEY}&endblock=99999999&offset={num_transactions}&page=1&sort=desc&startblock=0", payload=mock_response_data)

        result = await get_wallet_transactions(wallet_address, num_transactions)
        print("\n\nresult =------------------------\n\n",result ,"\n\n")
        # Assertions
        assert result['status'] == "1"
        assert result['message'] == "OK"

        # Optional: Check if the result contains transactions
        if 'result' in result:
            assert isinstance(result['result'], list)
            
# test fetch failed
@pytest.mark.asyncio
async def test_fetch_failed():
    wallet_address = "0x8f54751F441B7707AbA668f0cF4745daAE545D16"
    num_transactions = 5

    # Mock response data
    mock_response_data = {
        "status": "0",
        "message": "Failed to fetch transactions"
    }

    with aioresponses() as m:
        m.get(f"{BASE_URL}?module=account&action=txlist&address={wallet_address}&apikey={API_KEY}&endblock=99999999&offset={num_transactions}&page=1&sort=desc&startblock=0", payload=mock_response_data)

        with pytest.raises(ValueError, match="Failed to fetch transactions"):
            await get_wallet_transactions(wallet_address, num_transactions)
            

# test invalid wallet address
@pytest.mark.asyncio
async def test_invalid_wallet_address():
    invalid_wallet_address = "InvalidAddress"

    with pytest.raises(ValueError, match="Invalid wallet address"):
        await get_wallet_transactions(invalid_wallet_address, 5)

# test invalid num transactions
@pytest.mark.asyncio
async def test_invalid_num_transactions():
    wallet_address = "0x8f54751F441B7707AbA668f0cF4745daAE545D16"
    invalid_num_transactions = 0

    with pytest.raises(ValueError, match="Number of transactions must be greater than 0"):
        await get_wallet_transactions(wallet_address, invalid_num_transactions)

# test missing or invalid base URL
@pytest.mark.asyncio
async def test_missing_base_url():
    wallet_address = "0x8f54751F441B7707AbA668f0cF4745daAE545D16"
    num_transactions = 5
    invalid_base_url = ""

    with pytest.raises(ValueError, match="Base URL is required"):
        invalid_client, _ = execute_function_from_prompt(invalid_base_url, API_KEY)
        await invalid_client(wallet_address, num_transactions)


# test missing or invalid API key
@pytest.mark.asyncio
async def test_missing_api_key():
    wallet_address = "0x8f54751F441B7707AbA668f0cF4745daAE545D16"
    num_transactions = 5
    invalid_api_key = ""

    with pytest.raises(ValueError, match="API key is required"):
        invalid_client, _ = execute_function_from_prompt(BASE_URL, invalid_api_key)
        await invalid_client(wallet_address, num_transactions)
