from operations.thought import Thought
from collections import Counter

class ThoughtLite:
    current_data : str = ""
    original : str = ""
    phase :int = -1

    def __init__(self, thought: Thought):
        self.current_data = thought["current"]
        self.original = thought["original"]
        self.phase = thought["phase"]

    def __eq__(self, other: ThoughtLite):
        if self.current_data==None or self.current_data=="":
            return self.phase==other.phase and self.original==other.original
        return self.phase == other.phase and Counter(self.current_data) == Counter(other.current_data)

# Usage:

# Given:
# op_type
# instruction_func
# thought

# Code:
# thought_lite = ThoughtLite(thought)
# key = tuple(op_type, instruction_func, thought_lite)
