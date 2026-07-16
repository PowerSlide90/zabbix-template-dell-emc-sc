from pathlib import Path

from ruamel.yaml import YAML

from config import TEMPLATE_GROUP, TEMPLATE_NAME, ZABBIX_VERSION


def write(template):

    data = {
        "zabbix_export": {
            "version": ZABBIX_VERSION,
            "templates": [
                {
                    "uuid": "00000000000000000000000000000001",
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

    yaml = YAML()
    yaml.default_flow_style = False
    yaml.indent(mapping=2, sequence=4, offset=2)

    output = Path(__file__).resolve().parents[2] / "template" / "Template_Dell_EMC_SC_Series.yaml"

    output.parent.mkdir(exist_ok=True)

    with output.open("w", encoding="utf-8") as f:
        yaml.dump(data, f)

    print(f"Generated: {output}")