class Input:
    def __init__(self, up_action, down_action, left_action, right_action, escape_action):
        self.up = up_action
        self.down = down_action
        self.left = left_action
        self.right = right_action
        self.escape = escape_action

    def handle_events(self):
        pass
