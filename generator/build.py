from core.template import Template
from writer.zabbix74 import Zabbix74Writer


def main():

    template = Template()

    writer = Zabbix74Writer()

    writer.write(template)


if __name__ == "__main__":
    main()