class Record:
    filename = "record.txt"
    maxOpened = 0

    def load(self):
        try:
            file = open(self.filename, 'r')
            content = file.read()
            if content:
                self.maxOpened = int(content)
        except FileNotFoundError:
            self.save(0)

    def save(self, currentOpened):
        self.load()
        if currentOpened > self.maxOpened:
            self.maxOpened = currentOpened
            with open(self.filename, 'w') as file:
                file.write(str(self.maxOpened))
