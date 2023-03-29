import grpc
from concurrent import futures
import random
import time

import quorum_pb2
import quorum_pb2_grpc

class Replica(quorum_pb2_grpc.QuorumServicer):
    def __init__(self, id):
        self.id = id
        self.data = {}
        self.quorum_config = None

    def InitQuorum(self, request, context):
        N = request.N
        Nr = request.Nr
        Nw = request.Nw

        is_valid = (Nw + Nr > N) and (Nw > N // 2)
        if is_valid:
            self.quorum_config = request
            message = "Quorum configuration is valid and initialized."
        else:
            message = "Invalid quorum configuration."

        return quorum_pb2.InitQuorumResponse(success=is_valid, message=message)
    
    def Read(self, request, context):
        if request.key in self.data:
            timestamp = int(time.time())
            return quorum_pb2.Response(success=True, message="Read succeeded", value=self.data[request.key], timestamp=timestamp)
        else:
            return quorum_pb2.Response(success=False, message="Read failed", value="", timestamp=0)
        
    def Write(self, request, context):
        self.data[request.key] = request.value
        timestamp = int(time.time())
        return quorum_pb2.Response(success=True, message="Write succeeded", value="", timestamp=timestamp)

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    replicas = [Replica(i) for i in range(1, 6)]
    for replica in replicas:
        quorum_pb2_grpc.add_QuorumServicer_to_server(replica, server)
    server.add_insecure_port('[::]:50051')
    server.start()

    print('Starting server. Ready for Quorum check!.')

    server.wait_for_termination()

if __name__ == '__main__':
    run_server()