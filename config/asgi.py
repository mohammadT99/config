"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django

from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
application =ProtocolTypeRouter({
    "http":AsgiHandler(),

  # We will add WebSocket protocol later, but for now it's just HTTP.

})
