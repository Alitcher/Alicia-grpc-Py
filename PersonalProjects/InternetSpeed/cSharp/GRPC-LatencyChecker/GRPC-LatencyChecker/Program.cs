using Grpc.Net.Client;
using System.Collections.Generic;

internal class Program
{
    private static async void Main(string[] args)
    {
        using var channel = GrpcChannel.ForAddress("https://localhost:50051");
        //var client = new Gree
    }
}