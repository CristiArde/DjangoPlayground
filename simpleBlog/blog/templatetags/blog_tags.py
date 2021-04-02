from django import template
from ..models import Post

register = template.Library()

#@register.simple_tag(name='my_tag') to give it a diffrent name
@register.simple_tag
def total_posts():
    return Post.published.count()