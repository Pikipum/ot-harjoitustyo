#from user import User

class Message:
    # Message objects contain an unique ID, message content,
    # the time it was sent and who sent it.
    def __init__(self, id, msg, time, user):
        self.id = id
        self.msg = msg
        self.time = time
        self.user = user

    def __str__(self):
        return self.msg
