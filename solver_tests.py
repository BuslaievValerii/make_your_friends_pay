import sys
sys.path.insert(0, "../source/")

from solver import DebtProblemSolver, SolverException


__GREEN  = "\033[1;32m"
__RED    = "\033[1;31m"
__NORMAL = "\033[0m"


def __format(text, color):
    return color+text+__NORMAL


def __run_test_suite(test_suite):
    suite_not_failed = True
    for test in test_suite:
        result, error = test()
        if not result:
            print(__format(error, __RED))
            suite_not_failed = False
        else:
            print(f"{test.__name__} succeeded")

    if suite_not_failed:
        print(__format(f"All {len(test_suite)} tests were correct!", __GREEN))


def __call_solver(needs, debts, expected_result):
    solver = DebtProblemSolver(needs, debts)
    real_result = solver.solve()
    return all(map(all, real_result == expected_result))


def __expected_exception(needs, debts, exception_type):
    try:
        solver = DebtProblemSolver(needs, debts)
        result = solver.solve()
    except Exception as e:
        return isinstance(e, exception_type)
    return False


def test_solver_is_correct():
    needs = [1600, 500, 800, 800]
    debts = [1050, 1050, 700, 900]
    expected_result = [[1050,   0,   0,   0],
                       [ 550, 500,   0,   0],
                       [   0,   0, 700,   0],
                       [   0,   0, 100, 800]]
    return __call_solver(needs, debts, expected_result), "test_solver_is_correct has failed"


def test_solver_is_wrong():
    needs = [1600, 500, 800, 800]
    debts = [1050, 1050, 700, 900]
    expected_result = [[1050,   0,   0, 0],
                       [ 550, 500,   0, 0],
                       [   0,   0, 700, 0],
                       [   0,   0, 100, 0]]
    return not __call_solver(needs, debts, expected_result), "test_solver_is_wrong has failed"


def test_needs_and_debts_have_different_lenght_raises():
    needs = [1600, 500, 800, 800]
    debts = [1050, 1050, 700]
    return __expected_exception(needs, debts, SolverException), "test_needs_and_debts_have_different_lenght_raises has failed: expected SolverException"


def test_one_person_is_inactive():
    needs = [1600, 500, 800, 0, 800]
    debts = [1050, 1050, 700, 0, 900]
    expected_result = [[1050,   0,   0, 0,   0],
                       [ 550, 500,   0, 0,   0],
                       [   0,   0, 700, 0,   0],
                       [   0,   0,   0, 0,   0],
                       [   0,   0, 100, 0, 800]]
    return __call_solver(needs, debts, expected_result), "test_one_person_is_inactive has failed"


def test_no_people_are_okay():
    needs, debts, expected_result = [], [], []
    return __call_solver(needs, debts, expected_result), "test_no_people_are_okay has failed"


def test_no_transactions_between_people_are_okay():
    needs = debts = [1600, 500, 800, 800]
    expected_result = [[1600,   0,   0,   0],
                       [   0, 500,   0,   0],
                       [   0,   0, 800,   0],
                       [   0,   0,   0, 800]]
    return __call_solver(needs, debts, expected_result), "test_no_transactions_between_people_are_okay has failed"


def test_no_debts_are_okay():
    needs = debts = [0,0,0,0]
    expected_result = [[0,0,0,0],
                       [0,0,0,0],
                       [0,0,0,0],
                       [0,0,0,0]]
    return __call_solver(needs, debts, expected_result), "test_no_debts_are_okay has failed"


ALL_TESTS_SUITE = [
    test_solver_is_correct,
    test_solver_is_wrong,
    test_needs_and_debts_have_different_lenght_raises,
    test_one_person_is_inactive,
    test_no_people_are_okay,
    test_no_transactions_between_people_are_okay,
    test_no_debts_are_okay
]


if __name__ == "__main__":
    __run_test_suite(ALL_TESTS_SUITE)