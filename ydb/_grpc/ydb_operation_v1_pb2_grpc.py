# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ydb._grpc.protos import ydb_operation_pb2 as protos_dot_ydb__operation__pb2


class OperationServiceStub(object):
    """All rpc calls to YDB are allowed to be asynchronous. Response message
    of an rpc call contains Operation structure and OperationService
    is used for polling operation completion.

    Operation has a field 'ready' to notify client if operation has been
    completed or not. If result is ready a client has to handle 'result' field,
    otherwise it is expected that client continues polling result via
    GetOperation rpc of OperationService. Polling is made via unique
    operation id provided in 'id' field of Operation.

    Note: Currently some operations have synchronous implementation and their result
    is available when response is obtained. But a client must not make any
    assumptions about synchronous or asynchronous nature of any operation and
    be ready to poll operation status.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOperation = channel.unary_unary(
                '/Ydb.Operation.V1.OperationService/GetOperation',
                request_serializer=protos_dot_ydb__operation__pb2.GetOperationRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__operation__pb2.GetOperationResponse.FromString,
                )
        self.CancelOperation = channel.unary_unary(
                '/Ydb.Operation.V1.OperationService/CancelOperation',
                request_serializer=protos_dot_ydb__operation__pb2.CancelOperationRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__operation__pb2.CancelOperationResponse.FromString,
                )
        self.ForgetOperation = channel.unary_unary(
                '/Ydb.Operation.V1.OperationService/ForgetOperation',
                request_serializer=protos_dot_ydb__operation__pb2.ForgetOperationRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__operation__pb2.ForgetOperationResponse.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/Ydb.Operation.V1.OperationService/ListOperations',
                request_serializer=protos_dot_ydb__operation__pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__operation__pb2.ListOperationsResponse.FromString,
                )


class OperationServiceServicer(object):
    """All rpc calls to YDB are allowed to be asynchronous. Response message
    of an rpc call contains Operation structure and OperationService
    is used for polling operation completion.

    Operation has a field 'ready' to notify client if operation has been
    completed or not. If result is ready a client has to handle 'result' field,
    otherwise it is expected that client continues polling result via
    GetOperation rpc of OperationService. Polling is made via unique
    operation id provided in 'id' field of Operation.

    Note: Currently some operations have synchronous implementation and their result
    is available when response is obtained. But a client must not make any
    assumptions about synchronous or asynchronous nature of any operation and
    be ready to poll operation status.

    """

    def GetOperation(self, request, context):
        """Check status for a given operation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelOperation(self, request, context):
        """Starts cancellation of a long-running operation,
        Clients can use GetOperation to check whether the cancellation succeeded
        or whether the operation completed despite cancellation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ForgetOperation(self, request, context):
        """Forgets long-running operation. It does not cancel the operation and returns
        an error if operation was not completed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations that match the specified filter in the request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OperationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOperation,
                    request_deserializer=protos_dot_ydb__operation__pb2.GetOperationRequest.FromString,
                    response_serializer=protos_dot_ydb__operation__pb2.GetOperationResponse.SerializeToString,
            ),
            'CancelOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelOperation,
                    request_deserializer=protos_dot_ydb__operation__pb2.CancelOperationRequest.FromString,
                    response_serializer=protos_dot_ydb__operation__pb2.CancelOperationResponse.SerializeToString,
            ),
            'ForgetOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.ForgetOperation,
                    request_deserializer=protos_dot_ydb__operation__pb2.ForgetOperationRequest.FromString,
                    response_serializer=protos_dot_ydb__operation__pb2.ForgetOperationResponse.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=protos_dot_ydb__operation__pb2.ListOperationsRequest.FromString,
                    response_serializer=protos_dot_ydb__operation__pb2.ListOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Ydb.Operation.V1.OperationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OperationService(object):
    """All rpc calls to YDB are allowed to be asynchronous. Response message
    of an rpc call contains Operation structure and OperationService
    is used for polling operation completion.

    Operation has a field 'ready' to notify client if operation has been
    completed or not. If result is ready a client has to handle 'result' field,
    otherwise it is expected that client continues polling result via
    GetOperation rpc of OperationService. Polling is made via unique
    operation id provided in 'id' field of Operation.

    Note: Currently some operations have synchronous implementation and their result
    is available when response is obtained. But a client must not make any
    assumptions about synchronous or asynchronous nature of any operation and
    be ready to poll operation status.

    """

    @staticmethod
    def GetOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Operation.V1.OperationService/GetOperation',
            protos_dot_ydb__operation__pb2.GetOperationRequest.SerializeToString,
            protos_dot_ydb__operation__pb2.GetOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Operation.V1.OperationService/CancelOperation',
            protos_dot_ydb__operation__pb2.CancelOperationRequest.SerializeToString,
            protos_dot_ydb__operation__pb2.CancelOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ForgetOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Operation.V1.OperationService/ForgetOperation',
            protos_dot_ydb__operation__pb2.ForgetOperationRequest.SerializeToString,
            protos_dot_ydb__operation__pb2.ForgetOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Operation.V1.OperationService/ListOperations',
            protos_dot_ydb__operation__pb2.ListOperationsRequest.SerializeToString,
            protos_dot_ydb__operation__pb2.ListOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
