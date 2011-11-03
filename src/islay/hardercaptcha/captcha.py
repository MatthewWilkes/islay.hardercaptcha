import urllib

from lxml import html
from lxml.etree import XMLSyntaxError, Element
from webob import Request, Response

def CaptchaFactory(global_config, **local_conf):
    return CaptchaMiddleware

class CaptchaMiddleware(object):
    """An endpoint"""
    
    def __init__(self, app):
        self.app = app
        self.valid_captchas = set()
    
    def __call__(self, environ, start_response):
        
        # Before we go any further, gzip is hard to parse, don't ask for it
        del environ['HTTP_ACCEPT_ENCODING']
        
        request = Request(environ)

        if request.method == "POST":
            NotImplemented
            valid = captcha in self.valid_captchas
            params = urllib.urlencode(request.POST)
            post = request.POST.copy()
            post['isHuman'] = valid
            request.body = urllib.urlencode(post)
        
        response = request.get_response(self.app)
        
        # We don't want to deal with images and the like
        if response.content_type == 'text/html':
            try:
                parsed = html.fromstring(response.body)
            except (XMLSyntaxError, TypeError):
                return response(environ, start_response)
            response.body = html.tostring(parsed)
        
        NotImplemented
        
        return response(environ, start_response)
    
