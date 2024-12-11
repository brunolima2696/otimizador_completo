class InvalidExpression(Exception):
    def __init__(self, message="Expressao invalida"):
        self.message = message
        super().__init__(self.message)