# from config import token_v2, url
# from notion.client import NotionClient
# from notion.block import CodeBlock,TodoBlock

# client = NotionClient(token_v2=token_v2)
# page = client.get_block(url)

# #syntax for adding codeblocks

# page.children.add_new(CodeBlock, title = "test codeblock", language = "python")

# page.children.add_new(TodoBlock, title = "test todo block")


class CheckBox:
    def __init__(self, title):
        self.title = title


c = CheckBox("something")

print(c.title)
