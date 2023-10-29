from characterai import PyCAI

auth_token_file = open('auth_token.txt')
AUTH_TOKEN = auth_token_file.readline()
auth_token_file.close()
# sm64 mario, will change later
CHARACTER = 'OYYf4iM6fjt9eZ72oXRsY3UGPeXd9Y-uJwfAjF5JAwk'

class CommentaryAgent:
    def __init__(self):
        self.client = PyCAI(AUTH_TOKEN)
        self.chat = client.chat.get_chat(char)
        participants = self.chat['participants']

        if not participants[0]['is_human']:
            self.tgt = participants[0]['user']['username']
        else:
            self.tgt = participants[1]['user']['username']

    def render_system_message(self):
        pass

    def fetch_commentary(self, reasoning: str, task: str):
        pass
    