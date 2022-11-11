# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ydb._grpc.protos import ydb_discovery_pb2 as protos_dot_ydb__discovery__pb2


class DiscoveryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListEndpoints = channel.unary_unary(
                '/Ydb.Discovery.V1.DiscoveryService/ListEndpoints',
                request_serializer=protos_dot_ydb__discovery__pb2.ListEndpointsRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__discovery__pb2.ListEndpointsResponse.FromString,
                )
        self.WhoAmI = channel.unary_unary(
                '/Ydb.Discovery.V1.DiscoveryService/WhoAmI',
                request_serializer=protos_dot_ydb__discovery__pb2.WhoAmIRequest.SerializeToString,
                response_deserializer=protos_dot_ydb__discovery__pb2.WhoAmIResponse.FromString,
                )


class DiscoveryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListEndpoints(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WhoAmI(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiscoveryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListEndpoints': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEndpoints,
                    request_deserializer=protos_dot_ydb__discovery__pb2.ListEndpointsRequest.FromString,
                    response_serializer=protos_dot_ydb__discovery__pb2.ListEndpointsResponse.SerializeToString,
            ),
            'WhoAmI': grpc.unary_unary_rpc_method_handler(
                    servicer.WhoAmI,
                    request_deserializer=protos_dot_ydb__discovery__pb2.WhoAmIRequest.FromString,
                    response_serializer=protos_dot_ydb__discovery__pb2.WhoAmIResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Ydb.Discovery.V1.DiscoveryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DiscoveryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListEndpoints(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Discovery.V1.DiscoveryService/ListEndpoints',
            protos_dot_ydb__discovery__pb2.ListEndpointsRequest.SerializeToString,
            protos_dot_ydb__discovery__pb2.ListEndpointsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WhoAmI(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ydb.Discovery.V1.DiscoveryService/WhoAmI',
            protos_dot_ydb__discovery__pb2.WhoAmIRequest.SerializeToString,
            protos_dot_ydb__discovery__pb2.WhoAmIResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
