class Message:
    # Message objects contain an unique ID, message content,
    # the time it was sent and who sent it.
    def __init__(self, msgid, msg, time, user):
        self.msgid = msgid
        self.msg = msg
        self.time = time
        self.user = user

    def __str__(self):
        return self.msgid
