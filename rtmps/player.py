class Player:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.process = None
        self.current_msg = None
        self.current_file = None
        self.next_msg = None
        self.next_file = None
        self.queue = []
        self.loop = 0

PLAYERS = {}

def get_player(chat_id):
    if chat_id not in PLAYERS:
        PLAYERS[chat_id] = Player(chat_id)
    return PLAYERS[chat_id]
