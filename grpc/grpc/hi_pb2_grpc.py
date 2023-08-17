# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from grpc import hi_pb2 as grpc_dot_hi__pb2


class HiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHi = channel.unary_unary(
                '/hi.Hi/SayHi',
                request_serializer=grpc_dot_hi__pb2.HiRequest.SerializeToString,
                response_deserializer=grpc_dot_hi__pb2.HiReply.FromString,
                )
        self.SayHello = channel.unary_unary(
                '/hi.Hi/SayHello',
                request_serializer=grpc_dot_hi__pb2.HelloRequest.SerializeToString,
                response_deserializer=grpc_dot_hi__pb2.HelloReply.FromString,
                )
        self.AnotherSayHi = channel.unary_unary(
                '/hi.Hi/AnotherSayHi',
                request_serializer=grpc_dot_hi__pb2.HiRequest.SerializeToString,
                response_deserializer=grpc_dot_hi__pb2.HiReply.FromString,
                )


class HiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHi(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AnotherSayHi(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHi': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHi,
                    request_deserializer=grpc_dot_hi__pb2.HiRequest.FromString,
                    response_serializer=grpc_dot_hi__pb2.HiReply.SerializeToString,
            ),
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=grpc_dot_hi__pb2.HelloRequest.FromString,
                    response_serializer=grpc_dot_hi__pb2.HelloReply.SerializeToString,
            ),
            'AnotherSayHi': grpc.unary_unary_rpc_method_handler(
                    servicer.AnotherSayHi,
                    request_deserializer=grpc_dot_hi__pb2.HiRequest.FromString,
                    response_serializer=grpc_dot_hi__pb2.HiReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hi.Hi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi.Hi/SayHi',
            grpc_dot_hi__pb2.HiRequest.SerializeToString,
            grpc_dot_hi__pb2.HiReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi.Hi/SayHello',
            grpc_dot_hi__pb2.HelloRequest.SerializeToString,
            grpc_dot_hi__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AnotherSayHi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi.Hi/AnotherSayHi',
            grpc_dot_hi__pb2.HiRequest.SerializeToString,
            grpc_dot_hi__pb2.HiReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
