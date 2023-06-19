# README.md

## GRPC with Python - Learning Project

This project is a part of [Distributed Systems (LTAT.06.007)](https://courses.cs.ut.ee/2023/ds/spring/Main/Guide0) which is designed to guide students to get to know GRPC with Python and its capabilities. The program includes four types of RPC calls: Unary, Client Streaming, Server Streaming, and Bidirectional Streaming. 

### Prerequisites

You need to have the following installed:

- Python 3.8 or newer.
- GRPC Python package (`grpcio` and `grpcio-tools`), you can install it using pip:
  ```
  pip install grpcio grpcio-tools
  ```

### Clone the Repository

First, clone the repository using the following command:

```bash
git clone https://github.com/Alitcher/Alicia-grpc-Py.git
```
Navigate to the project folder:

```bash
cd 1-Interconnecting-individual-nodes
```

### Generate Protocol Buffers

This step is only necessary if you have made changes to the `ex1.proto` file. 

To generate the Python files (`ex1_pb2.py` and `ex1_pb2_grpc.py`) needed for GRPC, use the following command:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ex1.proto
```

This will create the necessary Python files based on your protobuf definition.

### Running the Server

To start the GRPC server, run the following command:

```bash
python server.py
```

The server will start and listen on `localhost` port `50051`.

### Running the Client

Open a new terminal window (don't close the one running the server) and run the client using:

```bash
python client.py
```

The client will connect to the server and provide you with options to make RPC calls. 

### Making RPC Calls

After starting the client, it will print out the options to make RPC calls. Enter the corresponding number for the type of RPC call you wish to make and follow the instructions.

```text
1 - Unary
2 - Client streaming
3 - Server streaming
4 - Bidirectional streaming
```

Enter `exit` to stop the client.

### Conclusion

I hope this guide was useful in understanding and running this GRPC Python learning project. I'd be happy to receive any suggestions or improvements. Enjoy exploring GRPC!


### References

[Python gRPC Tutorial by MissCoding](https://www.youtube.com/watch?v=WB37L7PjI5k&t=188s)
[Distributed Systems (LTAT.06.007)](https://courses.cs.ut.ee/2023/ds/spring/Main/Guide0)
