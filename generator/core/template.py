from config import TEMPLATE_NAME
from core.uuid_util import make_uuid


class Template:
    """
    Центральный объект генератора.

    Хранит все элементы шаблона до момента экспорта в YAML.
    """

    def __init__(self):

        self.uuid = make_uuid("template", TEMPLATE_NAME)

        self.name = TEMPLATE_NAME

        self.items = []
        self.macros = []
        self.valuemaps = []
        self.triggers = []
        self.discovery_rules = []
        self.tags = []
        self.graphs = []

    # -------------------------
    # Add methods
    # -------------------------

    def add_item(self, item):
        self.items.append(item)

    def add_macro(self, macro):
        self.macros.append(macro)

    def add_valuemap(self, valuemap):
        self.valuemaps.append(valuemap)

    def add_trigger(self, trigger):
        self.triggers.append(trigger)

    def add_discovery_rule(self, rule):
        self.discovery_rules.append(rule)

    def add_tag(self, tag):
        self.tags.append(tag)

    def add_graph(self, graph):
        self.graphs.append(graph)

    # -------------------------
    # Helpers
    # -------------------------

    @property
    def statistics(self):

        return {
            "items": len(self.items),
            "macros": len(self.macros),
            "valuemaps": len(self.valuemaps),
            "triggers": len(self.triggers),
            "discovery_rules": len(self.discovery_rules),
            "graphs": len(self.graphs),
        }