import pathlib

from ruamel.yaml import YAML

from config import (
    TEMPLATE_GROUP,
    TEMPLATE_NAME,
    ZABBIX_VERSION,
)


class Zabbix74Writer:

    def __init__(self):

        self.yaml = YAML()

        self.yaml.default_flow_style = False

        self.yaml.indent(
            mapping=2,
            sequence=4,
            offset=2
        )

    def write(self, template):

        data = {
            "zabbix_export": {
                "version": ZABBIX_VERSION,
                "templates": [
                    {
                        "uuid": template.uuid,
                        "template": TEMPLATE_NAME,
                        "name": TEMPLATE_NAME,
                        "groups": [
                            {
                                "name": TEMPLATE_GROUP
                            }
                        ],
                        "macros": [],
                        "valuemaps": [],
                        "items": []
                    }
                ]
            }
        }

        output = (
            pathlib.Path(__file__).resolve().parents[2]
            / "template"
            / "Template_Dell_EMC_SC_Series.yaml"
        )

        output.parent.mkdir(exist_ok=True)

        with output.open(
            "w",
            encoding="utf-8"
        ) as f:

            self.yaml.dump(data, f)

        print(f"Generated {output}")