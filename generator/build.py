from core.template import Template

from writer.zabbix74 import write


template = Template()

writer = Zabbix74Writer()

writer.write(template)