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


class ActivityPolicy(Model):
    """Execution policy for an activity.

    :param timeout: Specifies the timeout for the activity to run. The default
     timeout is 7 days. Type: string (or Expression with resultType string),
     pattern: ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type timeout: object
    :param retry: Maximum ordinary retry attempts. Default is 0. Type: integer
     (or Expression with resultType integer), minimum: 0.
    :type retry: object
    :param retry_interval_in_seconds: Interval between each retry attempt (in
     seconds). The default is 30 sec.
    :type retry_interval_in_seconds: int
    """

    _validation = {
        'retry_interval_in_seconds': {'maximum': 86400, 'minimum': 30},
    }

    _attribute_map = {
        'timeout': {'key': 'timeout', 'type': 'object'},
        'retry': {'key': 'retry', 'type': 'object'},
        'retry_interval_in_seconds': {'key': 'retryIntervalInSeconds', 'type': 'int'},
    }

    def __init__(self, timeout=None, retry=None, retry_interval_in_seconds=None):
        self.timeout = timeout
        self.retry = retry
        self.retry_interval_in_seconds = retry_interval_in_seconds
