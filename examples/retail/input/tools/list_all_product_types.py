# Copyright Sierra
import json
from typing import Any, Dict
from langchain.tools import StructuredTool


class ListAllProductTypes():
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        products = data["products"].set_index('product_id', drop=False).to_dict(orient='index')
        product_dict = {
            product["name"]: product["product_id"] for product in products.values()
        }
        product_dict = dict(sorted(product_dict.items()))
        return json.dumps(product_dict)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_all_product_types",
                "description": "List the name and product id of all product types. Each product type has a variety of different items with unique item ids and options. There are only 50 product types in the store.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }

list_all_product_types_schema = ListAllProductTypes.get_info()
list_all_product_types = StructuredTool.from_function(
        func=ListAllProductTypes.invoke,
        name=list_all_product_types_schema['function']["name"],
        description=list_all_product_types_schema['function']["description"],
    )