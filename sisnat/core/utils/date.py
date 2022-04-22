from datetime import datetime


def format_datetime_to_brt(dt: datetime):
    # TODO: need to translate to pt-br
    return dt.strftime('%d/%m/%Y %H:%M:%S')


def format_datetime_to_brt_extend(dt: datetime):
    # TODO: need to translate to pt-br
    return dt.strftime('%A %d de %B de %Y, %H:%M:%S')
