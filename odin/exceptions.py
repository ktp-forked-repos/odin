# -*- coding: utf-8 -*-

NON_FIELD_ERRORS = '__all__'


class ValidationError(Exception):
    """An error while validating data."""
    def __init__(self, message, code=None, params=None):
        """
        ValidationError can be passed any object that can be printed (usually
        a string), a list of objects or a dictionary.
        """
        if isinstance(message, dict):
            self.message_dict = message

        if isinstance(message, list):
            self.messages = message
        else:
            self.messages = [message]
            self.code = code
            self.params = params

    def __str__(self):
        # This is needed because, without a __str__(), printing an exception
        # instance would result in this:
        # AttributeError: ValidationError instance has no attribute 'args'
        # See http://www.python.org/doc/current/tut/node10.html#handling
        if hasattr(self, 'message_dict'):
            return repr(self.message_dict)
        return repr(self.messages)

    def __repr__(self):
        return 'ValidationError(%s)' % self

    @property
    def error_messages(self):
        if hasattr(self, 'message_dict'):
            return self.message_dict
        else:
            return self.messages

    def update_error_dict(self, error_dict):
        if hasattr(self, 'message_dict'):
            if error_dict:
                for k, v in self.message_dict.items():
                    error_dict.setdefault(k, []).extend(v)
            else:
                error_dict = self.message_dict
        else:
            error_dict[NON_FIELD_ERRORS] = self.messages
        return error_dict


class RegistrationError(Exception):
    """
    Exception raised during registration of resources or mappings
    """


class MappingError(Exception):
    """
    Exceptions related to mapping, will typically be a more specific `MappingSetupError` or `MappingExecutionError`.
    """


class MappingSetupError(MappingError):
    """
    Exception raised during the setup of mapping rules.
    """


class MappingExecutionError(MappingError):
    """
    Exception raised during the execution of mapping rules.
    """
