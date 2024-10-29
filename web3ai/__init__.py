from .get_func_using_nlp import get_func_using_nlp 
from .handle_function_call import handle_function_call

async def execute_function_from_prompt(explorer_base_url: str, explorer_api_key: str, openai_api_key: str, prompt: str):
    result =await get_func_using_nlp( openai_api_key, prompt)
    if result.get("status") == "ok" and "function_obj" in result:
        return await handle_function_call(function_obj=result.get("function_obj"), explorer_api_key=explorer_api_key, explorer_base_url=explorer_base_url)
    else: 
        # If no function call was detected, return an error message
        return ValueError("No function call detected by the model.")
        