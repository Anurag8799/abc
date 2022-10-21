from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START_MESSAGE = '''**Hello, {}
I Am tnlinks.in Bot , Bulk Link Converter. I Can Convert Links Directly From Your tnlinks.in Account,
    
1. Go To 👉 https://tnlinks.in/member/tools/api 

2. Than Copy API Key

3. Than Type /set_api than give a single space and than paste your API Key (see example to understand more...)

/set_api(space)API Key 
(See Example.👇)
Example:** `/set_api cbd63775f798fe0e58c67a56e6ce8b70c495cda4`

**💁‍♀️ Hit 👉 /help To Get Help.

➕ Hit 👉 /footer To Get Help About Adding your Custom Footer to bot.

➕ Hit 👉 /header To Get Help About Adding your Custom Footer to bot.**
'''




HELP_MESSAGE = '''
**Hey! My name is {firstname}. I am a Tnlinks Pro Shortener Bot.**

Features 

- [Hyperlink](https://t.me/{username})
- Buttons convert support
- Header and Footer Text support
- Replace Username
- Banner Image

Helpful commands:

- /start: Starts me! You've probably already used this.
- /help: Sends this message; I'll tell you more about myself!
If You Have Any Problem Then Contact - @TN92FF

Available commands:

- /set_api
- /header
- /footer
- /username
- /banner_image
- /me

Use the commands to know more about the same
Below are some features I provide'''


ABOUT_TEXT = """
**My Details:**
`🤖 Name:` ** {} **
    
`📝 Language:` [Python 3](https://www.python.org/)

`🧰 Framework:` [Pyrogram](https://github.com/pyrogram/pyrogram)

`👨‍💻 Developer:` [Anonymous](t.me/TN92FF)

`📢 Support:` [DK BOTZ SUPPORT](https://t.me/TnlinksUrlShortener)

`🌐 Source Code:` **[Click Here](https://t.me/TN92FF)**
"""




CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""




HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf'),
        InlineKeyboardButton('Admins', callback_data=f'admins_list'),    
    ],

    [
        
        #InlineKeyboardButton('Channels', callback_data=f'channels_list'),
        InlineKeyboardButton('Home', callback_data='start_command')
        
    ],


])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Home', callback_data=f'start_command'),
        InlineKeyboardButton('Help', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('Close', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Help', callback_data=f'help_command'),
        InlineKeyboardButton('About', callback_data='about_command')
    ],
    [
        InlineKeyboardButton('Close', callback_data='delete')
    ]
])

METHOD_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Mdisk + Shortener', callback_data=f'change_method#TnlinksWithMdisk'),
        InlineKeyboardButton('Shortener', callback_data='change_method#Tnlinks')
    ],
        [
        InlineKeyboardButton('Back', callback_data=f'help_command'),
        InlineKeyboardButton('Close', callback_data='delete')
    ],

])

BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """
- Website: [{base_site}](https://tnlinks.in/ref/Greymatter658)

- {base_site} API: {shortener_api}

- Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/set_api [api]`
            
Ex: `/set_api cbd63775f798fe0e58c67a56e6ce8b70c495cda4`

Get API From [{base_site}](https://tnlinks.in/ref/Greymatter658)

Current {base_site} API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \n
To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """Reply to the Footer Text You Want

This Text will be added to the bottom of every message caption or text

For adding line break use \n
To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """Current Username: {username}

Usage: `/username your_username` (without @)

This username will be automatically replaced with other usernames in the post

To remove this username, `/username remove`"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
