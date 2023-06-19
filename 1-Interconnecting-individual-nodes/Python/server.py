from concurrent import futures
import time
import grpc
import ex1_pb2
import ex1_pb2_grpc

class ex1(ex1_pb2_grpc.ex1):
    def HelloWorld(self, request,context):
        print("hello unary made: ")
        print(request)
        response = ex1_pb2.HelloResponse(status = True)
        return response

    def ClientStream(self, request_iterator,context):
        delayed_reply = ex1_pb2.DelayResponse()
        for request in request_iterator:
            print("client stream made:")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"Client sends {len(delayed_reply.request)} messages. Please expect a delayed response."
        return delayed_reply
    
    def ServerStream(self, request, context):
       print("server stream made: ")
       print(request)
       for i in range(3):
           response = ex1_pb2.HelloResponse(status = True)
           yield response
           time.sleep(3)
    
    def BidirectionalStream(self, request_iterator, context):
        for request in request_iterator:
            print("bi-direction stream made:")
            print(request)

            hello_reply = ex1_pb2.HelloResponse()
            hello_reply.message = f"{request.name}"

            yield hello_reply


def serve():
    port = 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ex1_pb2_grpc.add_ex1Servicer_to_server(ex1(),server)
    server.add_insecure_port(f"localhost: {port}")
    print(f'Starting server. Listening on port {port}.')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()