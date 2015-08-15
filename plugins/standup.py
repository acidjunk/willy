from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings

class StandupPlugin(WillPlugin):

    @periodic(hour='9', minute='30', day_of_week="mon-fri")
    def standup(self):
        self.say("@all Standup!")
