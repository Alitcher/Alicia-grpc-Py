import time
import grpc
import speedtest_pb2
import speedtest_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = speedtest_pb2_grpc.SpeedTestStub(channel)
        start_time = time.time()
        responses = stub.Test(generate_messages())
        for response in responses:
            print(f'Received message: {response.message}')
        latency = time.time() - start_time
        print(f'Latency: {latency} seconds')

def generate_messages():
    for i in range(20):
        yield speedtest_pb2.SpeedRequest(message=f'{i}-Hello')

if __name__ == '__main__':
    run()
