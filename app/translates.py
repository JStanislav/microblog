import json
import requests
from flask_babel import _
from flask import current_app


def translate(text, source_lang, dest_lang):
    if 'MS_TRANLATOR_KEY' not in current_app.config or \
                       not current_app.config['MS_TRANLATOR_KEY']:
        return _('Error: the tranlation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANLATOR_KEY']}
    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(
                        text, source_lang, dest_lang),
                        headers=auth)
    if r.status_code != 200:
        return _('Error: the tranlation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))