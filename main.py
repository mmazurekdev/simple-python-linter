import ast
from typing import List

import linter.rules.abstract as abstract
from linter import Linter


class VariableNamesLengthRule(abstract.Rule):
    NODE: ast.stmt = ast.Assign
    LINT_CODE = 'Py123'

    def run(self, node: ast.Assign):
        names: List[ast.Name] = node.targets
        for name in names:
            if len(name.id) < 5:
                self.log.warning("Name %r is to short! Please be more verbose. ", name.id)


code = """
test = 5
test2 = test + 4
"""

linter: Linter = Linter()
linter.add_rule(VariableNamesLengthRule)
linter.run_linter(code)
