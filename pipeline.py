import json
from typing import Any

from pydantic import BaseModel, ValidationError


class EntryItem(BaseModel):
    opening: str
    tactic: str
    phase: str


def load_entries(path: str) -> list[dict[str, Any]]:
    with open(path, "r") as f:
        data = json.load(f)
    return data


entries_data = load_entries("legacy_entries.json")

accepted: list[EntryItem] = []
error_list: list[str] = []

for entry in entries_data:
    try:
        passed_entry = EntryItem.model_validate(entry)
        accepted.append(passed_entry)
    except ValidationError as e:
        problem_one = e.errors()[0]
        name = entry.get("name", "Unknown")
        error_list.append(f"{name} -> {problem_one['msg']}")

print(f"{len(accepted)} entries are valid: ")
for i in accepted:
    print(i)

print(f"{len(error_list)} entries are invalid: ")
for error_i in error_list:
    print(error_i)
