# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class ApiError(Model):
    """Api error.

    :param details: The Api error details
    :type details: list[~azure.mgmt.imagebuilder.models.ApiErrorBase]
    :param inner_error: The Api inner error
    :type inner_error: ~azure.mgmt.imagebuilder.models.InnerError
    :param code: The error code.
    :type code: str
    :param target: The target of the particular error.
    :type target: str
    :param message: The error message.
    :type message: str
    """

    _attribute_map = {
        'details': {'key': 'details', 'type': '[ApiErrorBase]'},
        'inner_error': {'key': 'innerError', 'type': 'InnerError'},
        'code': {'key': 'code', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApiError, self).__init__(**kwargs)
        self.details = kwargs.get('details', None)
        self.inner_error = kwargs.get('inner_error', None)
        self.code = kwargs.get('code', None)
        self.target = kwargs.get('target', None)
        self.message = kwargs.get('message', None)


class ApiErrorException(HttpOperationError):
    """Server responsed with exception of type: 'ApiError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ApiErrorException, self).__init__(deserialize, response, 'ApiError', *args)