class tester:  # Oparcie na klasach
    def __init__(self, start):  # Przy tworzeniu obiektu stan jest
        self.state = start  # Jawna referencja do zmienej state
    def nested(self, label):
        print(label, self.state)
        self.state += 1  # Modyfikacja jest zawsze dozwolona
F = tester(0)  # Tworzenie instancji, wywołanie __init__
print(F.nested('mielonka'))  # F przekzywane jest do self
print(F.nested('szynka'))
