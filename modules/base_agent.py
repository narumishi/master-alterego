import threading

import pyautogui

from util.addon import check_sys_setting
from util.base import is_interactive_mode
from util.config import *
from util.log import logger
from .server import app


class BaseAgent:
    _server_thread: threading.Thread = None

    def pre_process(self, conf):
        config.load(conf)
        check_sys_setting(config.need_admin)
        if config.www_host_port is not None:
            self.run_sever(*config.www_host_port)

    def post_process(self):
        # server thread should be daemon, make it possible to be terminated by Ctrl-C
        # in terminal: keep app running until ctrl-C pressed => call thread.join() in post processing
        # in interactive: main thread is always alive, join() is not needed, we can terminate it manually.
        if config.hide_when_finish:
            pyautogui.hotkey('alt', 'z')  # hide window for mumu emulator
        if not is_interactive_mode() and self._server_thread.is_alive():
            logger.info('keep running server...')
            self._server_thread.join()

    @classmethod
    def terminate_server(cls):
        from util.addon import kill_thread
        kill_thread(cls._server_thread)
        app.logger.info(f'server stopped: {cls._server_thread}')

    @classmethod
    def run_sever(cls, host='0.0.0.0', port=8080):
        if cls._server_thread is not None and cls._server_thread.is_alive():
            app.logger.info(f'server is already running: {cls._server_thread}')
            return
        cls._server_thread = threading.Thread(target=app.run, name='flask_app_server', args=[host, port], daemon=True)
        cls._server_thread.start()
        app.logger.info(f'server started: {cls._server_thread}')
