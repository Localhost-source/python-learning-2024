# JSON stands for Javascript Object Notation
# It is a data format to communicate between / among the entities
# For example, Frontend and Backend, Backend-Backend, Mobile-Backend, Between microservices etc.

# Valid JSON Formats
"""
{
    "name": "Alex",
    "age": 20,
    "ids": [1, 9, 12],
    "info":{
        "email": "",
        "address": ""
    }
}
[
{
    "name": "Alex",
    "age": 20,
    "ids": [1, 9, 12],
    "info":{
        "email": "",
        "address": ""
    },
    {
    "name": "Alex",
    "age": 20,
    "ids": [1, 9, 12],
    "info":{
        "email": "",
        "address": ""
    }
}
}
]
"""


# Invalid JSON Formats
"""
{'id': 1, 'name': 'alex'}  # Invalid due to single quotes
{1, 2, 3}
"""