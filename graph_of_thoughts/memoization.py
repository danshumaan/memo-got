from operations.thought import Thought
from collections.import Counter

class ThoughtLite:
    current_data : str = ""
    phase :int = -1

    __init__(self, thought: Thought):
        self.current_data = thought["current"]
        self.phase = thought["phase"]

    def __eq__(self, other: ThoughtLite):
        return self.phase == other.phase && Counter(self.current_data) == Counter(other.current_data)

# Usage:

# Given:
# op_type
# instruction_func
# thought

# Code:
# thought_lite = ThoughtLite(thought)
# key = tuple(op_type, instruction_func, thought_lite)
