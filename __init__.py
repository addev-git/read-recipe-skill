from mycroft import MycroftSkill, intent_file_handler


class ReadRecipe(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('recipe.read.intent')
    def handle_recipe_read(self, message):
        self.speak_dialog('recipe.read')


def create_skill():
    return ReadRecipe()

