import abc
import ast
import logging


class ContextFilter(logging.Filter):

    def __init__(self, lint_code: str, name: str = ''):
        super().__init__(name)
        self.lint_code = lint_code

    def filter(self, record):
        record.lint_code = self.lint_code
        return True


class Rule:
    NODE: ast.stmt
    LINT_CODE: str = ''

    def __init__(self):
        self.log = logging.getLogger()
        custom_filter = ContextFilter(self.LINT_CODE)
        self.log.addFilter(custom_filter)
        logging.basicConfig(format='%(asctime)-15s %(levelname)-8s %(lint_code)-5s: %(message)s')

    @abc.abstractmethod
    def run(self, node: ast.stmt):
        pass
