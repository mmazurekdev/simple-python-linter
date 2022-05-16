from collections import defaultdict
from typing import List, Dict

from linter.rules.abstract import Rule


class Registry:
    def __init__(self):
        self._checkers: Dict[str, List[Rule]] = defaultdict(lambda: [])

    def add_checker(self, node_name: str, _class: Rule) -> None:
        self._checkers[node_name].append(_class)

    def get_checkers(self, node_name: str) -> List[Rule]:
        return self._checkers[node_name]


registry = Registry()
