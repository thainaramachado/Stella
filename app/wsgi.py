"""
WSGI config for stella project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings') #Correção estava 'stella.wsgi.application' / apesar do seu projeto se chamar Stella, o diretório onde vc está construindo sua aplicação se chama 'app' então as configurações tem que se refenciar a ele.

application = get_wsgi_application()
