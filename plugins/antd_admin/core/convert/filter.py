def django_convert_typescript(value):
    """
    django转typescript数据类型
    :param value:
    :return:
    """
    if value == 'BigAutoField':
        return 'number'
    if value == 'BigIntegerField':
        return 'number'
    if value == 'BooleanField':
        return 'boolean'
    if value == 'CharField':
        return 'string'
    if value == 'DateField':
        return 'string'
    if value == 'DateTimeField':
        return 'string'
    if value == 'DecimalField':
        return 'number'
    if value == 'EmailField':
        return 'string'
    if value == 'FloatField':
        return 'number'
    if value == 'IntegerField':
        return 'number'
    if value == 'PositiveBigIntegerField':
        return 'number'
    if value == 'PositiveIntegerField':
        return 'number'
    if value == 'PositiveSmallIntegerField':
        return 'number'
    if value == 'SmallIntegerField':
        return 'number'
    if value == 'TextField':
        return 'string'
    if value == 'timefield':
        return 'string'
    if value == 'ForeignKey':
        return 'number'
    if value == 'ManyToManyField':
        return 'Array<number>'
    return 'string'


def enable_filter(value, fields):
    """
    筛选允许筛选的项
        1.字段类型包含choices
        2.字段类型为many2many
    """
    if not value or not fields:
        return False
    cur_field = [item for item in fields if value == item['name']]
    if not cur_field:
        return False
    cur_field = cur_field[0]
    if cur_field.get('choices'):
        return True
    if cur_field.get('type') == 'ManyToManyField':
        return True
    return False


def django_to_protable(value):
    """
    django转pro table列类型
    :param value:
    :return:
    """

    if value == 'BigAutoField':
        return 'digit'
    if value == 'BigIntegerField':
        return 'digit'
    if value == 'BooleanField':
        return 'radio'
    if value == 'CharField':
        return 'text'
    if value == 'DateField':
        return 'date'
    if value == 'DateTimeField':
        return 'dateTime'
    if value == 'DecimalField':
        return 'digit'
    if value == 'EmailField':
        return 'text'
    if value == 'FloatField':
        return 'digit'
    if value == 'IntegerField':
        return 'digit'
    if value == 'PositiveBigIntegerField':
        return 'digit'
    if value == 'PositiveIntegerField':
        return 'digit'
    if value == 'PositiveSmallIntegerField':
        return 'digit'
    if value == 'SmallIntegerField':
        return 'digit'
    if value == 'TextField':
        return 'textarea'
    if value == 'timefield':
        return 'time'
    if value == 'ForeignKey':
        return 'number'
    if value == 'ManyToManyField':
        return 'Array<number>'


def capitalize(value):
    """
    首字母大写
    :param value:
    :return:
    """
    return value.capitalize()



