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

from enum import Enum


class IntegrationRuntimeState(Enum):

    initial = "Initial"
    stopped = "Stopped"
    started = "Started"
    starting = "Starting"
    stopping = "Stopping"
    need_registration = "NeedRegistration"
    online = "Online"
    limited = "Limited"
    offline = "Offline"


class ParameterType(Enum):

    object_enum = "Object"
    string = "String"
    int_enum = "Int"
    float_enum = "Float"
    bool_enum = "Bool"
    array = "Array"


class DependencyCondition(Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    skipped = "Skipped"
    completed = "Completed"


class TriggerRuntimeState(Enum):

    started = "Started"
    stopped = "Stopped"
    disabled = "Disabled"


class PipelineRunQueryFilterOperand(Enum):

    pipeline_name = "PipelineName"
    status = "Status"
    run_start = "RunStart"
    run_end = "RunEnd"


class PipelineRunQueryFilterOperator(Enum):

    equals = "Equals"
    not_equals = "NotEquals"
    in_enum = "In"
    not_in = "NotIn"


class PipelineRunQueryOrderByField(Enum):

    run_start = "RunStart"
    run_end = "RunEnd"


class PipelineRunQueryOrder(Enum):

    asc = "ASC"
    desc = "DESC"


class TriggerRunStatus(Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    inprogress = "Inprogress"


class SapHanaAuthenticationType(Enum):

    basic = "Basic"
    windows = "Windows"


class SftpAuthenticationType(Enum):

    basic = "Basic"
    ssh_public_key = "SshPublicKey"


class FtpAuthenticationType(Enum):

    basic = "Basic"
    anonymous = "Anonymous"


class HttpAuthenticationType(Enum):

    basic = "Basic"
    anonymous = "Anonymous"
    digest = "Digest"
    windows = "Windows"
    client_certificate = "ClientCertificate"


class MongoDbAuthenticationType(Enum):

    basic = "Basic"
    anonymous = "Anonymous"


class ODataAuthenticationType(Enum):

    basic = "Basic"
    anonymous = "Anonymous"


class TeradataAuthenticationType(Enum):

    basic = "Basic"
    windows = "Windows"


class Db2AuthenticationType(Enum):

    basic = "Basic"


class SybaseAuthenticationType(Enum):

    basic = "Basic"
    windows = "Windows"


class DatasetCompressionLevel(Enum):

    optimal = "Optimal"
    fastest = "Fastest"


class JsonFormatFilePattern(Enum):

    set_of_objects = "setOfObjects"
    array_of_objects = "arrayOfObjects"


class DayOfWeek(Enum):

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"


class DaysOfWeek(Enum):

    sunday = "Sunday"
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"


class RecurrenceFrequency(Enum):

    not_specified = "NotSpecified"
    minute = "Minute"
    hour = "Hour"
    day = "Day"
    week = "Week"
    month = "Month"
    year = "Year"


class WebActivityMethod(Enum):

    get = "GET"
    post = "POST"
    put = "PUT"


class CassandraSourceReadConsistencyLevels(Enum):

    all = "ALL"
    each_quorum = "EACH_QUORUM"
    quorum = "QUORUM"
    local_quorum = "LOCAL_QUORUM"
    one = "ONE"
    two = "TWO"
    three = "THREE"
    local_one = "LOCAL_ONE"
    serial = "SERIAL"
    local_serial = "LOCAL_SERIAL"


class StoredProcedureParameterType(Enum):

    string = "String"
    int_enum = "Int"
    decimal_enum = "Decimal"
    guid = "Guid"
    boolean = "Boolean"
    date_enum = "Date"


class HDInsightActivityDebugInfoOption(Enum):

    none = "None"
    always = "Always"
    failure = "Failure"


class AzureSearchIndexWriteBehaviorType(Enum):

    merge = "Merge"
    upload = "Upload"


class CopyBehaviorType(Enum):

    preserve_hierarchy = "PreserveHierarchy"
    flatten_hierarchy = "FlattenHierarchy"
    merge_files = "MergeFiles"


class PolybaseSettingsRejectType(Enum):

    value = "value"
    percentage = "percentage"


class SelfHostedIntegrationRuntimeNodeStatus(Enum):

    need_registration = "NeedRegistration"
    online = "Online"
    limited = "Limited"
    offline = "Offline"
    upgrading = "Upgrading"
    initializing = "Initializing"
    initialize_failed = "InitializeFailed"


class IntegrationRuntimeUpdateResult(Enum):

    succeed = "Succeed"
    fail = "Fail"


class IntegrationRuntimeInternalChannelEncryptionMode(Enum):

    not_set = "NotSet"
    ssl_encrypted = "SslEncrypted"
    not_encrypted = "NotEncrypted"


class IntegrationRuntimeAutoUpdate(Enum):

    on = "On"
    off = "Off"


class ManagedIntegrationRuntimeNodeStatus(Enum):

    starting = "Starting"
    available = "Available"
    recycling = "Recycling"
    unavailable = "Unavailable"


class IntegrationRuntimeSsisCatalogPricingTier(Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    premium_rs = "PremiumRS"


class IntegrationRuntimeAuthKeyName(Enum):

    auth_key1 = "authKey1"
    auth_key2 = "authKey2"
