from concurrent import futures
import time
import grpc
import speedtest_pb2
import speedtest_pb2_grpc

class SpeedTestServicer(speedtest_pb2_grpc.SpeedTestServicer):
    def Test(self, request_iterator, context):
        for request in request_iterator:
            print(f'Received message: {request.message}')
            yield speedtest_pb2.SpeedResponse(message='Received')

def serve():
    port = 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    speedtest_pb2_grpc.add_SpeedTestServicer_to_server(SpeedTestServicer(), server)
    server.add_insecure_port(f'[::]:{port}')
    print(f'Starting server. Listening on port {port}.')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
