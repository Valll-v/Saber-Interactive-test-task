class SelfDependencyException(Exception):
    pass


class CircularDependencyException(Exception):
    pass


class UndefinedDependencyException(Exception):
    pass


class UndefinedCommandException(Exception):
    pass
