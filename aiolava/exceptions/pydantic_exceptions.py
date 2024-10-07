from aiolava.exceptions.base_exceptions import BaseException


class LavaValidationError(BaseException):
    __module__ = 'aiolava.exceptions.pydantic_exceptions'
    __qualname__ = 'LavaValidationError'
    __doc__ = 'Exception raised when a pydantic model fails to validate'
    pass


class LavaMissingFieldError(LavaValidationError):
    __module__ = 'aiolava.exceptions.pydantic_exceptions'
    __qualname__ = 'LavaMissingFieldError'
    __doc__ = 'Exception raised when a required field is missing'
    pass


class LavaInvalidTypeError(LavaValidationError):
    __module__ = 'aiolava.exceptions.pydantic_exceptions'
    __qualname__ = 'LavaInvalidTypeError'
    __doc__ = 'Exception raised when a field has an invalid type'
    pass


class LavaValueError(LavaValidationError):
    __module__ = 'aiolava.exceptions.pydantic_exceptions'
    __qualname__ = 'LavaValueError'
    __doc__ = 'Exception raised when a field has an invalid value'
    pass

