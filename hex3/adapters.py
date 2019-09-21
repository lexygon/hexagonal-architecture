from .domain import ReadablePort, WriteablePort, ControllerUnit


class LightDetector(ReadablePort):
    def get_light_amplitude(self):
        return 1

    def read(self):
        return self.get_light_amplitude()


class Buzzer(WriteablePort):
    def make_noise(self):
        print('BUZZ!!')

    def write(self, value):
        if value > 0:
            self.make_noise()


class Dial(ReadablePort):
    current_value = 1

    def read(self):
        return self.current_value


class Light(WriteablePort):
    on = False

    def write(self, value):
        if value > 0:
            self.on = True
        else:
            self.on = False


class ThresholdDetectionCircuit(ControllerUnit):
    arbitrary_threshold = 4

    def input_to_output(self):
        next_value = self.input.read()
        if next_value > self.arbitrary_threshold:
            self.output.write(next_value)
