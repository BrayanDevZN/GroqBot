import inspect
from typing import Any
from pydantic import create_model


def _build_schema(func) -> dict:
    sig = inspect.signature(func)  # em bound method, o self já fica de fora

    fields = {
        name: (
            Any if p.annotation is p.empty else p.annotation,
            ... if p.default is p.empty else p.default,
        )
        for name, p in sig.parameters.items()
        if name not in ("self", "cls")
    }

    schema = create_model(func.__name__, **fields).model_json_schema()
    schema.pop("title", None)

    for prop in schema.get("properties", {}).values():
        prop.pop("title", None)

    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": inspect.getdoc(func),
            "parameters": schema,
        },
    }


def tool_schema(func):
    "Gera o schema da tool a partir da assinatura e da docstring"

    schema = _build_schema(func)

    # Método (bound): não aceita atributos, então devolve o dict direto
    if inspect.ismethod(func):
        return schema

    # Função solta: mantém o comportamento antigo
    func.schema = schema
    return func