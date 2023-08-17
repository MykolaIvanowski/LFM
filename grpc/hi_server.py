import hi_pb2_grpc
import hi_pb2


class HiServicer(hi_pb2_grpc.HiServicer):
    def SayHi(self, request, context):
        print('request message hi')
        print(request)
        hi_reply = hi_pb2.HiReply()
        hi_reply.message = f'{request.message_hello} and {request.greeting_number}'

        return super().SayHi(request=request, context=context)

    def SayHello(self, request, context):
        print('request message hello')
        print(request)
        hello_reply = hi_pb2.HelloReply()
        hello_reply.message_hello = request.message_hello
        hello_reply.greeting_number = request.greeting_number
        hello_reply.result_per_hi = request.result_per_hi

        return super().SayHello(context=context, request=request)

    def AnotherSayHi(self, request, context):
        pass