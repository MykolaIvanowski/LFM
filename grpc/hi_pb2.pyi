from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloReply(_message.Message):
    __slots__ = ["greeting_number", "message_hello", "result_per_hi"]
    GREETING_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_HELLO_FIELD_NUMBER: _ClassVar[int]
    RESULT_PER_HI_FIELD_NUMBER: _ClassVar[int]
    greeting_number: int
    message_hello: str
    result_per_hi: int
    def __init__(self, message_hello: _Optional[str] = ..., greeting_number: _Optional[int] = ..., result_per_hi: _Optional[int] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ["greeting_number", "hello_request", "result_per_hi"]
    GREETING_NUMBER_FIELD_NUMBER: _ClassVar[int]
    HELLO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESULT_PER_HI_FIELD_NUMBER: _ClassVar[int]
    greeting_number: int
    hello_request: str
    result_per_hi: int
    def __init__(self, hello_request: _Optional[str] = ..., greeting_number: _Optional[int] = ..., result_per_hi: _Optional[int] = ...) -> None: ...

class HiReply(_message.Message):
    __slots__ = ["greeting_number", "reply", "result_per_hi"]
    GREETING_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    RESULT_PER_HI_FIELD_NUMBER: _ClassVar[int]
    greeting_number: int
    reply: str
    result_per_hi: int
    def __init__(self, reply: _Optional[str] = ..., greeting_number: _Optional[int] = ..., result_per_hi: _Optional[int] = ...) -> None: ...

class HiRequest(_message.Message):
    __slots__ = ["greeting_number", "message_hi", "result_per_hi"]
    GREETING_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_HI_FIELD_NUMBER: _ClassVar[int]
    RESULT_PER_HI_FIELD_NUMBER: _ClassVar[int]
    greeting_number: int
    message_hi: str
    result_per_hi: int
    def __init__(self, message_hi: _Optional[str] = ..., greeting_number: _Optional[int] = ..., result_per_hi: _Optional[int] = ...) -> None: ...
