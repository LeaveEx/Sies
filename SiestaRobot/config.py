# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/SiestaRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 3330416  # integer value, dont use ""
    API_HASH = "551d747d492ad11a10054fbf672d16e3"
    ARQ_API_KEY = "FKIRFQ-IYWRKE-SEBYHE-CZRMBD-ARQ"
    TOKEN = "5262608425:AAEbUDcE2inIrSqmzdSTTJUDlVHeZF5pJw8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1680004937  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "itsmeleave"
    BOT_USERNAME = "senzuxbot"
    STRING_SESSION = "1BVtsOJIBuyAC0ni7ku6EM2HM8h2qJ5xzAqe2DdtcySA1s4iHs1ckGG2bXrFq9BOe7zHQvcnq74d8Quc8MDmySLxQMfp1XddHaHBoHWtDmnoYFHeT_n-2Ta9TPRbf5_fESDJp7u052RXpvhJrz0GWggI05gacGFud52KKUwZPKqB8JiWxeU_KR8SFz_9BjkjtoeciOWxSrdb8-4ORZFDAK7raO9gDKFKZ_s7N-sX0T9Bqao_0SkNl7IzVnI2t3WOX9-eQskDYjJr7oaYxwurGAupBs9ZyOrTrAHLcLx8_jnlTw1b6HhHLzLisig7PLbpIj7gyx5sKjU9HZwT9_kstw_PQGLyc-N0="
    SESSION_STRING = "1BVtsOJIBuyAC0ni7ku6EM2HM8h2qJ5xzAqe2DdtcySA1s4iHs1ckGG2bXrFq9BOe7zHQvcnq74d8Quc8MDmySLxQMfp1XddHaHBoHWtDmnoYFHeT_n-2Ta9TPRbf5_fESDJp7u052RXpvhJrz0GWggI05gacGFud52KKUwZPKqB8JiWxeU_KR8SFz_9BjkjtoeciOWxSrdb8-4ORZFDAK7raO9gDKFKZ_s7N-sX0T9Bqao_0SkNl7IzVnI2t3WOX9-eQskDYjJr7oaYxwurGAupBs9ZyOrTrAHLcLx8_jnlTw1b6HhHLzLisig7PLbpIj7gyx5sKjU9HZwT9_kstw_PQGLyc-N0="
    SUPPORT_CHAT = "senzusupp"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001600598969
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001561812932
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ERROR_LOGS = (
        -1001561812932
    )  # Prints information Error

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://doadmin:AVNS_fQskw1ybQeSVBnKpo13@db-postgresql-nyc1-31108-do-user-14162283-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require"  # needed for any database modules
    LOAD = []
    MONGO_DB_URI = "mongodb+srv://newsenzu:newsenzu@cluster0.m1mw8vk.mongodb.net/?retryWrites=true&w=majority"
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = "xYCR1ZyK3ZsofjH7Y6hPcyzC"
    OPENWEATHERMAP_ID = "887da2c60d9f13fe78b0f9d0c5cbaade"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
