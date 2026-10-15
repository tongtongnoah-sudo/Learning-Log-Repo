from dataclasses import dataclass
from typing import NamedTuple, TypedDict


class EntryDict(TypedDict):
    title: str
    message: str


class EntryTuple(NamedTuple):
    title: str
    message: str


@dataclass
class EntryClass:
    title: str
    message: str


my_entry: EntryDict = {
    "title": "King's Indian Defense",
    "message": "Respond to e4 with ...d6",
}
my_entry_tuple = EntryTuple(
    title="King's Indian Defense", message="Respond to e4 with ...d6"
)
my_entry_class = EntryClass(
    title="King's Indian Defense", message="Respond to e4 with ...d6"
)

my_entry["message"] = "Some opening"
# my_entry_tuple.message = "Some opening"
my_entry_class.message = "Some opening"

print(my_entry["message"])
print(my_entry_class.message)
print(my_entry_tuple.message)

# TypedDict is best of the code is one where flexibility is a strength.
# Use NamedTuple where mutable code can become a liability and lead to hard-to-track bugs.
# Dataclass is best for making data readable and is especially useful with heterogenous data.
