# see https://stackoverflow.com/questions/11815503/whats-the-best-way-to-write-python-code-into-a-python-file
class CodeBlock():
    def __init__(self, head, block):
        self.head = head
        self.block = block
    def __str__(self, indent=""):
        result = indent + self.head + ":\n"
        indent += "    "
        for block in self.block:
            if isinstance(block, CodeBlock):
                result += block.__str__(indent)
            else:
                result += indent + block + "\n"
        return result