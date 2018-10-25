from django.conf import settings
import hmac
from hashlib import sha1

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
import requests
from ipaddress import ip_address, ip_network
from django.utils.encoding import force_bytes
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import git
import os

@require_POST
@csrf_exempt
def hookendpoint(request):
    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')

    # Verification complete, now we are good to go
    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')
    if event == 'ping':
        return HttpResponse('pong', status=200)
    elif event == 'push':
        g = git.cmd.Git(os.getcwd())
        g.pull()
        return HttpResponse(status = 202)

    return HttpResponse('OK')
