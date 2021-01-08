from collections import defaultdict

class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = BetterCountMissing()
print(counter() == 0)
print(callable(counter))

