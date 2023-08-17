import hi_pb2_grpc
import hi_pb2
import grpc


def run():
    while True:
        with grpc.insecure_chennel('localhost:50001') as channel:
            stub = hi_pb2_grpc.HiStub(channel=channel)
            print("run server hello!!!")
            print("1, rpc call say hello!!!")
            print("2 rpc call say hi!")
            rpc_call = input("Put rpc call would you like")

            if rpc_call == "1":
                hello_request = hi_pb2.HelloRequest(hello_request="hello message from rpc",
                                                    greeting_number=1000, result_per_hi=2
                                                    )
                stub.SayHello(hello_request)
            elif rpc_call == "2":
                hi_request = hi_pb2.HiRequest(message_hi="hi message from rpc",
                                              greeting_number=10000, result_per_hi=1
                                              )
                stub.SayHi(hi_request)
            elif rpc_call == "10":
                print("exit")
                break
            else:
                raise NotImplementedError()


if __name__ == "__main__":
    run()