
class User:
    # Users have a name and a list of messages they have sent
    def __init__(self, name, msghistory, password):
        self.name = name
        self.msghistory = msghistory
        self.password = password

    def __str__(self):
        return self.name
