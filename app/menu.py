import webview
import webview.menu as wm
from webview import Window

from app import settings
from html.settings import get_config_html


def on_refresh():
    active_window: Window = webview.active_window()
    if active_window:
        config = settings.load()
        active_window.load_url(config.current_url)


def on_bing_ai():
    active_window: Window = webview.active_window()
    if active_window:
        config = settings.load()
        config.current_url = config.url_bing
        settings.dump(config.dict())
        active_window.load_url(config.current_url)


def on_chat_gpt():
    active_window: Window = webview.active_window()
    if active_window:
        config = settings.load()
        config.current_url = config.url_gpt
        settings.dump(config.dict())
        active_window.load_url(config.current_url)


def on_config():
    active_window: Window = webview.active_window()
    if active_window:
        active_window.load_html(get_config_html())


menu_items = [
    wm.Menu(
        'ChatAI',
        [
            wm.MenuAction('Refresh', on_refresh),
            wm.MenuAction('BingAI', on_bing_ai),
            wm.MenuAction('ChatGPT', on_chat_gpt),
        ]
    ),
    wm.Menu(
        'Setting',
        [
            wm.MenuAction('config', on_config)
        ]
    )
]
