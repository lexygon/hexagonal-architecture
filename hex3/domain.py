class ReadablePort:
    def read(self):
        raise NotImplementedError


class WriteablePort:
    def write(self, value):
        raise NotImplementedError


class ControllerUnit:
    def __init__(self, input: ReadablePort, output: WriteablePort):
        self.input = input
        self.output = output

    def input_to_output(self):
        return self.output.write(self.input.read())
