class Template:

    def __init__(self):

        self.macros = []

        self.items = []

        self.valuemaps = []

    def add_macro(self, macro):

        self.macros.append(macro)

    def add_item(self, item):

        self.items.append(item)

    def add_valuemap(self, vm):

        self.valuemaps.append(vm)