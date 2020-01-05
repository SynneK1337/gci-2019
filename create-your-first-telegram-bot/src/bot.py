from github_wrapper import Github
from weather import Weather
import telegram.ext
import logging


class Telegram(telegram.ext.Updater):
    def __init__(self, token=None):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        telegram.ext.Updater.__init__(self, token, use_context=True)
        self.dispatcher.add_handler(telegram.ext.CommandHandler('forks', self._forks))
        self.dispatcher.add_handler(telegram.ext.CommandHandler('weather', self._weather))
        self.dispatcher.add_error_handler(self._error)
        self.start_polling()
        self.idle()

    def _forks(self, update, context):
        message = "Number of forks:\n"
        if context.args:
            for arg in context.args:
                try:
                    repos = Github().get_organization_repos(arg)
                except ValueError:
                    update.message.reply_text(f"Error: organization called {arg} not found.")
                else:
                    message += f'{arg} repositories:\n'
                    for repo in repos:
                        message += f"{repo['name']}:\t{repo['forks']} forks\n"
        else:
            repos = Github().get_organization_repos('fedora-infra')
            for repo in repos:
                message += f"{repo['name']}:\t{repo['forks']} forks\n"
        update.message.reply_text(message)

    def _weather(self, update, context):
        weather = Weather('9fa16bd5078ca8dffdf54339845e08e6')
        if not context.args:
            update.message.reply_text("Usage: /weather <CITYNAME>")
        else:
            response = weather.get_by_city_name(context.args[0], units='metric')
            if response['cod'] == '404':
                update.message.reply_text(f"Error: {context.args[0]} not found.")
            elif response['cod'] == 200:
                message = f"""Current weather in {context.args[0]}:
Description:\t{response['weather'][0]['description']}
Temperature:\t{response['main']['temp']} °C
Wind speed:\t{response['wind']['speed']} m/s
Humidity:\t{response['main']['humidity']} %
Pressure:\t{response['main']['pressure']} hPa
                           """
                update.message.reply_text(message)
            else:
                update.message.reply_text("Unknown error :(")

    def _error(self, update, context):
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)


if __name__ == "__main__":
    _TOKEN = '925626458:AAHDW4zHbwoan-AI7X_7EKTZe2nGAr37L8s'
    t = Telegram(_TOKEN)
