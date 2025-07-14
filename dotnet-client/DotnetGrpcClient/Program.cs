using System;
using System.Threading.Tasks;
using Grpc.Net.Client;
using Greeter; // Proto'dan gelen namespace

class Program
{
    static async Task Main(string[] args)
    {
        // Python gRPC server'ına bağlan
        var channel = Grpc.Net.Client.GrpcChannel.ForAddress("http://localhost:50051");
        var client = new Greeter.Greeter.GreeterClient(channel);

        Console.Write("İsmini gir kaptanım: ");
        var name = Console.ReadLine();

        var reply = await client.SayHelloAsync(new HelloRequest { Name = name });
        Console.WriteLine("🚀 Python sunucusundan cevap: " + reply.Message);
    }
}
