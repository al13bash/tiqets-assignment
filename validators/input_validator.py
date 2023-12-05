from functools import cached_property
from abc import ABC, abstractmethod
import sys


class InputValidator(ABC):
    def __init__(self, input):
        self.input = input

    def validate(self):
        print(self.invalid_input.to_string(index=False), file=sys.stderr)

        return self.valid_input

    @cached_property
    def valid_input(self):
        self._valid_input = self.input[~self.validation_mask]

        return self._valid_input

    @cached_property
    def invalid_input(self):
        self._invalid_input = self.input[self.validation_mask]

        return self._invalid_input

    @abstractmethod
    @cached_property
    def validation_mask(self):
        pass