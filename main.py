from config import token_v2, url
from notion.client import NotionClient
from notion.block import CodeBlock

from discord_webhook import DiscordWebhook


client = NotionClient(token_v2=token_v2)
page = client.get_block(url)

#create checkboxes for assignment names
#possibly create labels for subjects (?)

# page.children.add_new(CodeBlock, title = "something", language = "python")

print (page.blocks)

#purges all blocks from a given notion
# def Purge():
#   for block in page.blocks:
#     page.remove()

# Purge()