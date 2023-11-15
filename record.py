class Record:
    def __init__(self, filename="record.txt"):
        self.filename = filename
        self.maxOpened = 0

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                if content:
                    self.maxOpened = int(content)
        except FileNotFoundError:
            self.save(0)

    def save(self, currentOpened):
        if currentOpened > self.maxOpened:
            self.maxOpened = currentOpened
            with open(self.filename, 'w') as file:
                file.write(str(self.maxOpened))

    def update_max_opened(self, currentOpened):
        self.load()
        self.save(currentOpened)