from aiolava.exceptions.base_exceptions import BaseException


class LavaRequestError(BaseException):
    __module__ = 'aiolava.exceptions.request_exceptions'
    __qualname__ = 'LavaRequestError'
    __doc__ = 'Exception raised when a request fails'
    
    def __init__(self, data: dict, status: int, error: dict, status_check: bool):
        self.data = data
        self.status = status
        self.error = error
        self.status_check = status_check

    def __str__(self):
        return f"Request failed with status {self.status} and error {self.error}"
    

class LavaInvalidResponseError(BaseException):
    __module__ = 'aiolava.exceptions.request_exceptions'
    __qualname__ = 'LavaInvalidResponseError'
    __doc__ = 'Exception raised when a response is invalid'
    
    def __init__(self, status_code: int) -> None:
        self.status = status_code
    
    def __str__(self):
        return f"Response status code is {self.status}"



__all__ = [
    'LavaRequestError',
    'LavaInvalidResponseError',
]