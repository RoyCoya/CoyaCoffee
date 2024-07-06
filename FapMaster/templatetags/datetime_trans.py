from django import template

register = template.Library()

@register.filter
def duration(duration):
    result = ''
    total_seconds = int(duration.total_seconds())
    month, total_seconds = divmod(total_seconds, 30*24*60*60)
    if month > 0: result += str(month) + '月'
    days, total_seconds = divmod(total_seconds, 24*60*60)
    if days > 0: result += str(days) + '天'
    hours, total_seconds = divmod(total_seconds, 60*60)
    if hours > 0: result += str(hours) + '小时'
    minutes, seconds = divmod(total_seconds, 60)
    if minutes > 0: result += str(minutes) + '分钟'
    if seconds > 0: result += str(seconds) + '秒'
    return result