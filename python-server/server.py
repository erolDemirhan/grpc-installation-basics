import grpc
from concurrent import futures
import greeter_pb2
import greeter_pb2_grpc

class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f"Gelen istek: {request.name}")
        return greeter_pb2.HelloReply(message=f"Merhaba {request.name}! gRPC sunucusundan selamlar.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("🚀 gRPC Python Server çalışıyor... Port: 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
