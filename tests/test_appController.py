import json
import src.appController
import pytest

my_json_string = """{
    "text": "lykke"
}"""

to_python = json.loads(my_json_string)

def test_correct():
    assert src.appController.postendpoint(to_python) == to_python