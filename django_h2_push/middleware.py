from django.utils.deprecation import MiddlewareMixin


def _build_header(asset_names):
    asset_template = "<{asset_path}>; rel=preload"
    return ", ".join(
        asset_template.format(asset_name=asset_name)
        for asset_name in asset_names
    )


class H2PushMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        # not strictly necessary, but it helps spec out what we're
        # using
        request._h2_push_store = set()

    @staticmethod
    def process_response(request, response):
        if not getattr(request, '_h2_push_store', None):
            return response
        link_header = response.get('Link', '')
        if link_header:
            link_header += ', '
        link_header += _build_header(request._h2_push_store)
        response['Link'] = link_header
        return response
