from utils import read_json
# global variables
user_info = read_json('users.json')
admins = [user_info["vin"]['id'], user_info["kwok"]['id']]
bot_channel = '710106340865081355'
metal_channel = '694379147065163806'
