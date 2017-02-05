from django import template
from django.templatetags.static import StaticNode

register = template.Library()


class PushedStaticNode(StaticNode):
    def render(self, context):
        rendered = url = super(PushedStaticNode, self).render(context)
        if not url:
            url = self.url(context)
        if url:
            request = context.get('request')
            if request:
                if not hasattr(request, '_h2_push_store'):
                    request._h2_push_store = set()
                request._h2_push_store.add(url)
        return rendered


@register.tag('pushed_static')
def do_pushed_static(parser, token):
    return PushedStaticNode.handle_token(parser, token)
