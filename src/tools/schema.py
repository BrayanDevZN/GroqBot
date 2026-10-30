import inspect
from pydantic import create_model

def tool(func):
    "Gera o schema da tool a partir da assinatura e da docstring"

    sig = inspect.signature(func)

    fields = {
        name: (p.annotation, ... if p.default is p.empty else p.default)
        for name, p in sig.parameters.items()
        if name != "self"
    }

    schema = create_model(func.__name__, **fields).model_json_schema()
    schema.pop("title", None)

    for prop in schema.get("properties", {}).values():
        prop.pop("title", None)

    func.schema = {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": inspect.getdoc(func),
            "parameters": schema,
        },
    }

    return func