import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()  #自定义filter时必须加上


@register.filter(is_safe=True)  #注册template filter
@stringfilter  #希望字符串作为参数
def custom_md_truncate(value, max_length):
    maxl=int(max_length)
    if len(value) > maxl:
        truncd_val = value[:maxl]
        n = truncd_val.find("```")
        find_num = 0
        while n != -1:
            n = truncd_val.find("```", n + 3)
            find_num += 1
        if find_num % 2 != 0:
            truncd_val += "......\n```\n"
        else:
            truncd_val += "......"
    else:
        truncd_val = value

    return mark_safe(markdown.markdown(truncd_val,
                                       extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False))

