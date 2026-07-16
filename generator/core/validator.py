def validate(template):

    keys = set()

    for item in template.items:

        if item.key in keys:

            raise ValueError(item.key)

        keys.add(item.key)