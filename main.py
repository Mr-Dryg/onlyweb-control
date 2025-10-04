import webbrowser
import os

username_login = os.getlogin()
yandex_path=f"C:/Users/{username_login}/AppData/Local/Yandex/YandexBrowser/Application/browser.exe"
webbrowser.register('yandex', None, webbrowser.BackgroundBrowser(yandex_path))
webbrowser.get('yandex').open('ya.ru')
