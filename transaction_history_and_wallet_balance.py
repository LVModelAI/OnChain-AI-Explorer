# This is the function that we want the model to be able to call
import aiohttp
import asyncio
from openai import OpenAI
from dotenv import load_dotenv
import json
import os


# initialize the openai client

load_dotenv()
EXPLORER_BASE_URL = os.getenv("EXPLORER_BASE_URL")
EXPLORER_API_KEY = os.getenv("EXPLORER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

# function to fetch the latest transactions for a given wallet address
async def get_wallet_transactions(wallet_address: str, num_transactions: int) -> dict:
    print(f"Fetching transactions for wallet address: {wallet_address}")
    try:
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
            "apikey": ETHERSCAN_API_KEY,
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(ETHERSCAN_BASE_URL, params=params) as response:
                data = await response.json()

                if data["status"] != "1" or data["message"] != "OK":
                    raise ValueError(data.get("message", "Failed to fetch transactions"))

                result = data["result"]
                print("\n\nresult ---------- \n", result, "\n\n")
                for tx in result:
                    print("\n\n")   
                return data["result"]
   
    except Exception as error:
        print(f"Error fetching transactions: {error}")
        raise   
    
# function to fetch the wallet balance for a given wallet address
async def get_wallet_balance(wallet_address: str) -> dict:
    print(f"Fetching balance for wallet address: {wallet_address}")

    url = f"{ETHERSCAN_BASE_URL}?module=account&action=balance&address={wallet_address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data['status'] == '1':
                    print("\n\ndata------------------", data)
                    return data
                else:
                    error_result = {"error": data['message']}
                    print(error_result)
                    return error_result
            else:
                error_result = {"error": f"HTTP Error: {response.status}"}
                print(error_result)
                return error_result
 
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
                        "description": "Ethereum wallet address.",
                    },
                    "num_of_transactions": {
                        "type": "number",
                        "description": "Number of transactions to fetch. Take default value as 1",
                    },
                },
                "required": ["wallet_address", "num_of_transactions"],
                "additionalProperties": False,
            },
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
                        "description": "Ethereum wallet address.",
                    },
                },
                "required": ["wallet_address"],
                "additionalProperties": False,
            },
        }
    }
]

async def handle_function_call(function_obj):
    function_name = function_obj.function.name
    function_args = function_obj.function.arguments
    
    #parsing the arguments
    function_args = json.loads(function_args)
    
    #calling the function
    if function_name == "get_wallet_transactions":
        await get_wallet_transactions(wallet_address=function_args["wallet_address"], num_transactions=function_args["num_of_transactions"])  
    
    elif  function_name == "get_wallet_balance":
        await get_wallet_balance(wallet_address=function_args["wallet_address"])
    
    else:
        print(f"Function {function_name} not found")
            

# main function
async def main():
    messages = []
    messages.append({"role": "system", "content": "You are a helpful customer support assistant. Use the supplied tools to assist the user."})

    while True:
        # getting input from user from cli
        prompt = input("enter message (type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        
        print("user ---- ", prompt, "\n")

        messages.append({"role": "user", "content": prompt})

        
        response = response.choices[0]
        # print(" response ---------" , response)
                     
        # # if function call detected content will be None and response will have tool_calls
        if(response.message.content == None and response.message.tool_calls):
            # print("Tool call detected", response.message.tool_calls[0])
            function_obj = response.message.tool_calls[0]
            
            #structure of function_obj
            '''
            tool_calls[0] = {
                id='',
                function=Function(
                    arguments='{}', 
                    name='get_wallet_transactions'
                ), 
                type='function'
            }
            '''
            await handle_function_call(function_obj)
        
        else:
            messages.append({"role": "assistant", "content": response.message.content})
            print(f"agent ---- " , response.message.content , "\n")

# running the main function
asyncio.run(main())

