# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ex1_pb2 as ex1__pb2


class ex1Stub(object):
    """service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloWorld = channel.unary_unary(
                '/ex1.ex1/HelloWorld',
                request_serializer=ex1__pb2.HelloRequest.SerializeToString,
                response_deserializer=ex1__pb2.HelloResponse.FromString,
                )
        self.ClientStream = channel.stream_unary(
                '/ex1.ex1/ClientStream',
                request_serializer=ex1__pb2.HelloRequest.SerializeToString,
                response_deserializer=ex1__pb2.DelayResponse.FromString,
                )
        self.ServerStream = channel.unary_stream(
                '/ex1.ex1/ServerStream',
                request_serializer=ex1__pb2.HelloRequest.SerializeToString,
                response_deserializer=ex1__pb2.HelloResponse.FromString,
                )
        self.BidirectionalStream = channel.stream_stream(
                '/ex1.ex1/BidirectionalStream',
                request_serializer=ex1__pb2.HelloRequest.SerializeToString,
                response_deserializer=ex1__pb2.HelloResponse.FromString,
                )


class ex1Servicer(object):
    """service definition
    """

    def HelloWorld(self, request, context):
        """unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientStream(self, request_iterator, context):
        """client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServerStream(self, request, context):
        """server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BidirectionalStream(self, request_iterator, context):
        """bi
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ex1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloWorld': grpc.unary_unary_rpc_method_handler(
                    servicer.HelloWorld,
                    request_deserializer=ex1__pb2.HelloRequest.FromString,
                    response_serializer=ex1__pb2.HelloResponse.SerializeToString,
            ),
            'ClientStream': grpc.stream_unary_rpc_method_handler(
                    servicer.ClientStream,
                    request_deserializer=ex1__pb2.HelloRequest.FromString,
                    response_serializer=ex1__pb2.DelayResponse.SerializeToString,
            ),
            'ServerStream': grpc.unary_stream_rpc_method_handler(
                    servicer.ServerStream,
                    request_deserializer=ex1__pb2.HelloRequest.FromString,
                    response_serializer=ex1__pb2.HelloResponse.SerializeToString,
            ),
            'BidirectionalStream': grpc.stream_stream_rpc_method_handler(
                    servicer.BidirectionalStream,
                    request_deserializer=ex1__pb2.HelloRequest.FromString,
                    response_serializer=ex1__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ex1.ex1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ex1(object):
    """service definition
    """

    @staticmethod
    def HelloWorld(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ex1.ex1/HelloWorld',
            ex1__pb2.HelloRequest.SerializeToString,
            ex1__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClientStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ex1.ex1/ClientStream',
            ex1__pb2.HelloRequest.SerializeToString,
            ex1__pb2.DelayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ServerStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ex1.ex1/ServerStream',
            ex1__pb2.HelloRequest.SerializeToString,
            ex1__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BidirectionalStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ex1.ex1/BidirectionalStream',
            ex1__pb2.HelloRequest.SerializeToString,
            ex1__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
