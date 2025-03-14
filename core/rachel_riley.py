import operator
import itertools


class RachelRiley:
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv
        }

    def find_solution(self, target, selection):
        for r in range(1, len(selection) + 1):
            for perm in itertools.permutations(selection, r):
                for ops in itertools.product(self.operations.keys(), repeat=r - 1):
                    expression = self._build_expression(perm, ops)
                    try:
                        if eval(expression) == target:
                            return expression
                    except ZeroDivisionError:
                        continue
        return None

    def _build_expression(self, numbers, operations):
        expression = str(numbers[0])
        for i in range(1, len(numbers)):
            expression += f" {operations[i - 1]} {numbers[i]}"
        return expression

    def validate_solution(self, target, selection, solution):
        try:
            # Evaluate the solution
            result = eval(solution)

            # Check if the result matches the target
            if result != target:
                return abs(target - result)

            # Verify the solution uses only numbers from the selection and doesn't repeat usages
            used_numbers = []
            for number in selection:
                if str(number) in solution:
                    used_numbers.append(number)
                    solution = solution.replace(str(number), '', 1)

            if len(used_numbers) != len(selection):
                return abs(target - result)

            return 0
        except:
            return abs(target - eval(solution))