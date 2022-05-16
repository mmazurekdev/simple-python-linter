import ast
from typing import List, Any

from linter.registry import registry
from linter.rules.abstract import Rule


class Visitor(ast.NodeVisitor):
    def generic_visit(self, node: ast.stmt) -> Any:
        checkers: List[Rule.__class__] = registry.get_checkers(type(node))
        for checker in checkers:
            checker().run(node)

        super().generic_visit(node)


class Linter:
    def __init__(self):
        self.visitor: Visitor = Visitor()

    def add_rule(self, rule: Rule.__class__):
        if not hasattr(rule, 'NODE'):
            raise RuntimeError("Checker should have NODE attr")

        registry.add_checker(rule.NODE, rule)

    def run_linter(self, code: str):
        self.visitor.visit(ast.parse(code))
