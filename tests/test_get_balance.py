import pytest
from aioresponses import aioresponses
from web3ai import execute_function_from_prompt  # Adjust import based on actual module structure
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
EXPLORER_BASE_URL = os.getenv("EXPLORER_BASE_URL")
EXPLORER_API_KEY = os.getenv("EXPLORER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

wallet_address = "0x8f54751F441B7707AbA668f0cF4745daAE545D16"

# Initialize the functions
_, get_wallet_balance = execute_function_from_prompt(EXPLORER_BASE_URL, EXPLORER_API_KEY)

#test successful wallet balance fetch
@pytest.mark.asyncio
async def test_get_wallet_balance():

    # Mock balance response data (assuming 1 ETH in wei)
    mock_response_data = {
        "status": "1",
        "message": "OK",
        "result": str(10**18)  # 1 ETH in wei
    }

    with aioresponses() as m:
        m.get(f"{EXPLORER_BASE_URL}?module=account&action=balance&address={wallet_address}&tag=latest&apikey={EXPLORER_API_KEY}", payload=mock_response_data)

        result = await get_wallet_balance(wallet_address)
        
        # Assertions
        assert isinstance(result, dict)
        assert result["status"] == "1"
        assert result["message"] == "OK"
        assert result["result"] == str(10**18)  # 1 ETH in wei


#test fetch failed
@pytest.mark.asyncio
async def test_fetch_failed():
    # Mock balance response data
    mock_response_data = {
        "status": "0",
        "message": "Failed to fetch balance"
    }

    with aioresponses() as m:
        m.get(f"{EXPLORER_BASE_URL}?module=account&action=balance&address={wallet_address}&tag=latest&apikey={EXPLORER_API_KEY}", payload=mock_response_data)

        with pytest.raises(ValueError, match="Failed to fetch balance"):
            await get_wallet_balance(wallet_address)
            
# test invalid wallet address
@pytest.mark.asyncio
async def test_invalid_wallet_address():
    invalid_wallet_address = "InvalidAddress"

    with pytest.raises(ValueError, match="Invalid wallet address"):
        await get_wallet_balance(invalid_wallet_address)
        
# test invalid base url
@pytest.mark.asyncio
async def test_invalid_base_url():
    with pytest.raises(ValueError, match="Base URL is required"):
        _ , invalid_client = execute_function_from_prompt("", EXPLORER_API_KEY)
        await invalid_client(wallet_address)
        
# test invalid api key
@pytest.mark.asyncio
async def test_invalid_api_key():
    with pytest.raises(ValueError, match="API key is required"):
        _ , invalid_client = execute_function_from_prompt(EXPLORER_BASE_URL, "")
        await invalid_client(wallet_address)

