import grpc
import ex1_pb2
import ex1_pb2_grpc
import time


def get_client_stream_requests():
    while True:
        txt = input("Please type anything (or nothing to stop chatting): ")

        if txt == "":
            break

        hello_request = ex1_pb2.HelloRequest(name = txt)
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel("localhost: 50051") as channel:
        stub = ex1_pb2_grpc.ex1Stub(channel)
        print("1 - Unary")
        print("2 - Client streaming")
        print("3 - Server streaming")
        print("4 - Bidirectional streaming")
        exit = False
        while(not exit):
            rpc_call = input("Pick one RPC type to call, Unary = 1, client streaming = 2, server streaming = 3, bi stream = 4.")
            match rpc_call:
                #Only Unary runs smoothly
                case "1":
                    nameinput = input("please enter your name: ") 
                    unaryreq = stub.HelloWorld(ex1_pb2.HelloRequest(name=nameinput))
                    unaryresp = stub.HelloWorld(unaryreq)
                    print(f"Server response to {nameinput} = {unaryresp.status}")
                case "2":
                    delayed_reply = stub.ClientStream(get_client_stream_requests())

                    print("response:")
                    print(delayed_reply)
                case "3":
                    nameinput = input("please enter your name: ") 
                    sstreamres = stub.ServerStream(ex1_pb2.HelloRequest(name=nameinput))
                    for res in sstreamres:
                        print(f"Server response to {nameinput} = {res.status}")
                case "4":
                    responses = stub.BidirectionalStream(get_client_stream_requests())
                case "exit":
                    exit = True
                case _:
                    pass

if __name__ == "__main__":
    run()