import grpc
import quorum_pb2
import quorum_pb2_grpc

class QuorumClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = quorum_pb2_grpc.QuorumStub(self.channel)

    def init_quorum(self, N, Nr, Nw):
        request = quorum_pb2.QuorumConfig(N=N, Nr=Nr, Nw=Nw)
        response = self.stub.InitQuorum(request)
        return response.success, response.message
    
    def write(self, key, value):
        request = quorum_pb2.Request(key=key, value=value)
        response = self.stub.Write(request)
        return response.success, response.message, response.timestamp
    
    def read(self, key):
        request = quorum_pb2.Request(key=key, value="")
        response = self.stub.Read(request)
        return response.success, response.message, response.value, response.timestamp

def run_client():
    client = QuorumClient()

    # Initialize quorum configuration
    success, message = client.init_quorum(N=6, Nr=2, Nw=4)
    print("Quorum initialization:", message)

    # Write and read operations
    success, message, timestamp = client.write("key1", "value1")
    print("Write operation:", message, "Timestamp:", timestamp)

    success, message, value, timestamp = client.read("key1")
    print("Read operation:", message, "Value:", value, "Timestamp:", timestamp)

    success, message, value, timestamp = client.read("key2")
    print("Read operation:", message, "Value:", value, "Timestamp:", timestamp)

if __name__ == '__main__':
    run_client()