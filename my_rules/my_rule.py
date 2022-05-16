import ast
from typing import List

import linter.rules.abstract as abstract


class VariableNamesLengthRule(abstract.Rule):
    NODE: ast.stmt = ast.Assign
    LINT_CODE = 'Py123'

    def run(self, node: ast.Assign):
        names: List[ast.Name] = node.targets
        for name in names:
            if len(name.id) < 5:
                self.log.warn("Name %r is to short! Please be more verbose. ", name.id)

