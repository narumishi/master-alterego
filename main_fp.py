# %%
from modules.fp_gacha import FpGacha
from util.autogui import config, screenshot, is_interactive_mode, ArgParser  # noqas


def start(cfg=None):
    parser = ArgParser()
    cfg = cfg or parser.config
    fp_gacha = globals()['fp_gacha'] = FpGacha()
    fp_gacha.start(supervise=parser.supervise, cfg=cfg)


# %%
if __name__ == '__main__':
    start()
# %%
if __name__ == '__main__' and is_interactive_mode():
    start('data/config-jp.json')
