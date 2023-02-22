import os
import platform
from typing import Any
from pydantic import BaseModel, Field

import yaml


class Config(BaseModel):
    http_proxy: str = Field('')
    https_proxy: str = Field('')
    url_gpt: str = Field('')
    url_bing: str = Field('')
    current_url: str = Field('')
    gpt_ua: str = Field('')
    bing_ua: str = Field('')


config = Config()
config.http_proxy = 'http://127.0.0.1:7890'
config.https_proxy = 'http://127.0.0.1:7890'
config.current_url = 'https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx&fbg=0'
config.url_gpt = 'https://chat.openai.com/chat'
config.url_bing = 'https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx&fbg=0'
config.gpt_ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
config.bing_ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0'


def load(filename: str = 'settings.yaml') -> Config:
    path = get_storage_path()
    settings_path = os.path.join(path, filename)
    with open(settings_path) as f:
        c = yaml.load(f, Loader=yaml.FullLoader)
        return Config(**c)


def dump(data: Any, filename: str = 'settings.yaml'):
    path = get_storage_path()
    settings_path = os.path.join(path, filename)
    with open(settings_path, 'w') as f:
        yaml.dump(data, f)


def not_exist_create(filename: str = 'settings.yaml'):
    path = get_storage_path()
    if not os.path.exists(path):
        os.makedirs(path)
    settings_path = os.path.join(path, filename)
    if not os.path.isfile(settings_path):
        dump(config.dict(), filename)


def get_storage_path(folder: str = 'ChatGPT'):
    os_name = platform.system()
    if os_name == 'Windows':
        # do something for Windows
        home = os.path.expanduser('~')
        storage_path = os.path.join(home, '.config', folder)
    elif os_name == 'Linux':
        # do something for Linux
        home = os.path.expanduser('~')
        storage_path = os.path.join(home, '.config', folder)
    elif os_name == 'Darwin':
        # do something for Mac OS X
        home = os.path.expanduser('~')
        storage_path = os.path.join(home, '.config', folder)
    else:
        # do something for other OS
        home = os.path.expanduser('~')
        storage_path = os.path.join(home, folder)
    return storage_path
