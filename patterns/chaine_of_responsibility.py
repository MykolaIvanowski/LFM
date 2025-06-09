class Handler:
    """Base handler class."""
    def __init__(self, successor=None):
        self.successor = successor  # Next handler in the chain

    def handle_request(self, request):
        if self.successor:
            return self.successor.handle_request(request)
        return None


class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            return "Handler A processed the request."
        return super().handle_request(request)


class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            return "Handler B processed the request."
        return super().handle_request(request)


class DefaultHandler(Handler):
    def handle_request(self, request):
        return f"Request '{request}' was not processed."


# Setting up the chain
handler_chain = ConcreteHandlerA(ConcreteHandlerB(DefaultHandler()))

# Making requests
print(handler_chain.handle_request("A"))  # Output: Handler A processed the request.
print(handler_chain.handle_request("B"))  # Output: Handler B processed the request.
print(handler_chain.handle_request("C"))  # Output: Request 'C' was not processed.