class CustomAppException(Exception):
    pass


class SelfDependencyException(CustomAppException):
    pass


class CircularDependencyException(CustomAppException):
    pass


class UndefinedDependencyException(CustomAppException):
    pass


class UndefinedCommandException(CustomAppException):
    pass


class UndefinedBuildException(CustomAppException):
    pass
