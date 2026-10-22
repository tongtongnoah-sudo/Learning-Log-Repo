from pydantic import BaseModel, ValidationError


class TopicItem(BaseModel):
    name: str
    timestamp: str
    identification: int


incoming_data = {"topic": 33, "timestamp": "12:30:33", "identification": "3523"}

try:
    topic = TopicItem.model_validate(incoming_data)
    print("Topic added:", topic)
except ValidationError as error:
    print("Topic invalid; must be str")
    print(error)
