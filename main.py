import os

import gi
import webview
from webview.window import Window

from app import settings
from app.api import Api
from app.menu import menu_items

gi.require_version('Soup', '2.4')


settings.not_exist_create()
config = settings.load()
api = Api()

# 设置代理环境变量
if config.http_proxy:
    os.environ['http_proxy'] = config.http_proxy
if config.https_proxy:
    os.environ['https_proxy'] = config.https_proxy

window = webview.create_window(
    title='ChatAI',
    url=config.current_url,
    resizable=True,
    text_select=True,
    zoomable=True,
    draggable=True,
    confirm_close=True,
    on_top=True,
    js_api=api
)


def get_current_url(window: Window):
    print(window.real_url)


webview.start(get_current_url, window, private_mode=False, menu=menu_items, debug=False, user_agent=config.bing_ua)
