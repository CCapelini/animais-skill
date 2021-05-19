from mycroft import MycroftSkill, intent_file_handler


class Animais(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('animais.intent')
    def handle_animais(self, message):
        self.speak_dialog('animais')


def create_skill():
    return Animais()

