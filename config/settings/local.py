from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='e@t_s8n1apnwn@)@^gjukjic^c88==qfx49!8n6+*=6jyojc$h')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
