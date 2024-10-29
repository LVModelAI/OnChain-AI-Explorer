A natural language wrapper for blockchain explorer APIs

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python test_prompt.py
```

## Flow

1.  User inputs a query
2.  The query is processed by the NLP model in the `get_func_using_nlp.py` file
3.  The processed query returns function name
4.  The function name is used to call the respective function in the `handle_function_call.py`
5.  the arguments are passed to the function and the function is executed
6.  Output is returned
