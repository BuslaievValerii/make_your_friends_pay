import numpy as np


class SolverException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class DebtProblemSolver():
    def __init__(self, needs, debts):
        self._needs = needs[:]
        self._debts = debts[:]
    
    def solve(self):
        count = len(self._needs)
        self._results = np.zeros((count, count))

        if len(self._needs) != len(self._debts):
            raise SolverException(f"Broken size of input vectors: {len(self._needs)} and {len(self._debts)}")

        for i in range(count):
            diag_el = np.min([self._needs[i], self._debts[i]])
            self._results[i][i] = diag_el
            self._needs[i] -= diag_el
            self._debts[i] -= diag_el

        stop = False
        while not stop:
            if np.sum(self._needs) == 0 and np.sum(self._debts) == 0:
                stop = True
            else:
                i = self._debts.index(np.max(self._debts))
                j = self._needs.index(np.max(self._needs))
                box_el = np.min([self._debts[i], self._needs[j]])
                self._results[i][j] = box_el
                self._needs[j] -= box_el
                self._debts[i] -= box_el

        return self._results

    @property
    def results(self):
        return self._results