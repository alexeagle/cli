# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.devtools.build.v1 import publish_build_event_pb2 as google_dot_devtools_dot_build_dot_v1_dot_publish__build__event__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class PublishBuildEventStub(object):
    """A service for publishing BuildEvents. BuildEvents are generated by Build
    Systems to record actions taken during a Build. Events occur in streams,
    are identified by a StreamId, and ordered by sequence number in a stream.

    A Build may contain several streams of BuildEvents, depending on the systems
    that are involved in the Build. Some BuildEvents are used to declare the
    beginning and end of major portions of a Build; these are called
    LifecycleEvents, and are used (for example) to indicate the beginning or end
    of a Build, and the beginning or end of an Invocation attempt (there can be
    more than 1 Invocation in a Build if, for example, a failure occurs somewhere
    and it needs to be retried).

    Other, build-tool events represent actions taken by the Build tool, such as
    target objects produced via compilation, tests run, et cetera. There could be
    more than one build tool stream for an invocation attempt of a build.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PublishLifecycleEvent = channel.unary_unary(
                '/google.devtools.build.v1.PublishBuildEvent/PublishLifecycleEvent',
                request_serializer=google_dot_devtools_dot_build_dot_v1_dot_publish__build__event__pb2.PublishLifecycleEventRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.PublishBuildToolEventStream = channel.stream_stream(
                '/google.devtools.build.v1.PublishBuildEvent/PublishBuildToolEventStream',
                request_serializer=google_dot_devtools_dot_build_dot_v1_dot_publish__build__event__pb2.PublishBuildToolEventStreamRequest.SerializeToString,
                response_deserializer=google_dot_devtools_dot_build_dot_v1_dot_publish__build__event__pb2.PublishBuildToolEventStreamResponse.FromString,
                )


class PublishBuildEventServicer(object):
    """A service for publishing BuildEvents. BuildEvents are generated by Build
    Systems to record actions taken during a Build. Events occur in streams,
    are identified by a StreamId, and ordered by sequence number in a stream.

    A Build may contain several streams of BuildEvents, depending on the systems
    that are involved in the Build. Some BuildEvents are used to declare the
    beginning and end of major portions of a Build; these are called
    LifecycleEvents, and are used (for example) to indicate the beginning or end
    of a Build, and the beginning or end of an Invocation attempt (there can be
    more than 1 Invocation in a Build if, for example, a failure occurs somewhere
    and it needs to be retried).

    Other, build-tool events represent actions taken by the Build tool, such as
    target objects produced via compilation, tests run, et cetera. There could be
    more than one build tool stream for an invocation attempt of a build.
    """

    def PublishLifecycleEvent(self, request, context):
        """Publish a build event stating the new state of a build (typically from the
        build queue). The BuildEnqueued event must be publishd before all other
        events for the same build ID.

        The backend will persist the event and deliver it to registered frontend
        jobs immediately without batching.

        The commit status of the request is reported by the RPC's util_status()
        function. The error code is the canoncial error code defined in
        //util/task/codes.proto.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishBuildToolEventStream(self, request_iterator, context):
        """Publish build tool events belonging to the same stream to a backend job
        using bidirectional streaming.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PublishBuildEventServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PublishLifecycleEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishLifecycleEvent,
                    request_deserializer=google_dot_devtools_dot_build_dot_v1_dot_publish__build__event__pb2.PublishLifecycleEventRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'PublishBuildToolEventStream': grpc.stream_stream_rpc_method_handler(
                    servicer.PublishBuildToolEventStream,
                    request_deserializer=google_dot_devtools_dot_build_dot_v1_dot_publish__build__event__pb2.PublishBuildToolEventStreamRequest.FromString,
                    response_serializer=google_dot_devtools_dot_build_dot_v1_dot_publish__build__event__pb2.PublishBuildToolEventStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.devtools.build.v1.PublishBuildEvent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PublishBuildEvent(object):
    """A service for publishing BuildEvents. BuildEvents are generated by Build
    Systems to record actions taken during a Build. Events occur in streams,
    are identified by a StreamId, and ordered by sequence number in a stream.

    A Build may contain several streams of BuildEvents, depending on the systems
    that are involved in the Build. Some BuildEvents are used to declare the
    beginning and end of major portions of a Build; these are called
    LifecycleEvents, and are used (for example) to indicate the beginning or end
    of a Build, and the beginning or end of an Invocation attempt (there can be
    more than 1 Invocation in a Build if, for example, a failure occurs somewhere
    and it needs to be retried).

    Other, build-tool events represent actions taken by the Build tool, such as
    target objects produced via compilation, tests run, et cetera. There could be
    more than one build tool stream for an invocation attempt of a build.
    """

    @staticmethod
    def PublishLifecycleEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.build.v1.PublishBuildEvent/PublishLifecycleEvent',
            google_dot_devtools_dot_build_dot_v1_dot_publish__build__event__pb2.PublishLifecycleEventRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishBuildToolEventStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/google.devtools.build.v1.PublishBuildEvent/PublishBuildToolEventStream',
            google_dot_devtools_dot_build_dot_v1_dot_publish__build__event__pb2.PublishBuildToolEventStreamRequest.SerializeToString,
            google_dot_devtools_dot_build_dot_v1_dot_publish__build__event__pb2.PublishBuildToolEventStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
