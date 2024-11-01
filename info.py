import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
API_ID = environ.get('API_ID', "27705761")
API_HASH = environ.get('API_HASH', "822cb334ca4527a134aae97f9fe44fd6")
BOT_TOKEN = environ.get('BOT_TOKEN', "7859871122:AAFyR-dibB_2_SQFSSaJ3z75CLwL-FLwESc")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', "6987158459").split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS',).split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP', "")
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
SUPPORT_CHANNEL = environ.get('CHANNEL_USERNAME')
SUPPORT_GROUP = environ.get('GROUP_USERNAME')
INDEX_USER = [int(environ.get('INDEX_USER', '6987158459'))]
INDEX_USER.extend(ADMINS)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://akashrabha2005:781120@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'TgFiles')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1002125006518"))
FORCESUB_CHANNEL = int(environ.get('FORCESUB_CHANNEL', "-1002177725676"))
SLOW_MODE_DELAY = int(environ.get('SLOW_MODE_DELAY', 60))
WAIT_TIME = int(environ.get('AUTO_DELETE_WAIT_TIME', 1800))
FORWARD_CHANNEL = int(environ.get('FORWARD_CHANNEL', "-1002353224172"))

# other
ACCESS_KEY = environ.get("LICENSE_ACCESS_KEY")
BIN_CHANNEL = environ.get("BIN_CHANNEL")
URL = environ.get("STREAM_URL")
SHORTNER_SITE = environ.get("SHORTNER_SITE")
SHORTNER_API = environ.get("SHORTNER_API")
