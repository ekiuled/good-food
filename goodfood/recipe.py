from dataclasses import dataclass, asdict
import json
from dacite import from_dict


@dataclass
class Recipe:
    title: str
    description: str
    nutrition: dict
    ingredients: dict
    method: list[str]

    def to_json(self):
        return json.dumps(asdict(self))

    @classmethod
    def from_json(cls, json_str):
        return from_dict(data_class=cls, data=json.loads(json_str))
