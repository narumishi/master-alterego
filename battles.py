"""Store battle_func for different battles"""
from modules.battle_base import *


# noinspection DuplicatedCode
class AFree(BattleBase):
    @with_goto
    def a_charlotte(self, pre_process=False):
        """
        旧剑(75NP>=60NP)-豆爸50NP-孔明support-X-X-X
        """
        master = self.master
        T = master.T
        LOC = master.LOC

        master.quest_name = 'A-Charlotte'
        names = master.members = ['旧剑', '豆爸', '孔明']
        master.set_card_weight(dict(zip(names, [3, 1, 1.09])))

        # pre-processing: e.g. set templates, only once
        if pre_process:
            logger.debug(f'pre-process for {master.quest_name}...')
            T.read_templates('img/battles/a-charlotte/')

            # LOC.relocate((0, 0, 1920 - 1, 1080 - 1))

            # -----------------------    NP    Quick    Arts   Buster -----------
            master.set_cards(names[0], (3, 6), (3, 2), (2, 4), (3, 1))
            master.set_cards(names[1], (1, 7), (1, 4), (1, 2), (2, 2))
            master.set_cards_from_json(names[2], 'img/cards/android/cards-android.json', '孔明')

            def _handler():
                # mainly for jp, re-login handler at 3am(UTC+8)
                wait_targets(T.get('login_page'), LOC.menu_button)
                wait_targets(T.get('login1'), (1000, 480, 1350, 600), at=0, clicking=LOC.safe_area)
                # ....
                wait_targets(T.quest, LOC.quest)

            config.battle.login_handler = None if True else _handler
            return

        # battle part
        if config.battle.jump_battle:
            config.battle.jump_battle = False
            logger.warning('goto label.h')
            goto.h  # noqas

        # label.h  # noqas  # make sure master.set_waves(a,b) is called
        # master.set_waves(T.waveXa, T.waveXb)
        label.h  # noqas

        wait_targets(T.support, LOC.support_refresh)
        master.choose_support(match_svt=True, match_ce=True, match_ce_max=True, match_skills=True,
                              switch_classes=(5, 0), friend_only=False)

        # wave 1
        wait_targets(T.wave1a, LOC.loc_wave, 0.7)
        logger.debug(f'Quest {master.quest_name} started...')
        logger.debug('wave 1...')
        with master.set_waves(T.wave1a, T.wave1b):
            master.svt_skill(3, 2)
            master.svt_skill(3, 3)
            master.svt_skill(3, 1, 2)
            master.svt_skill(2, 2)
            master.auto_attack(nps=7)

        # wave 2
        wait_targets(T.wave2a, LOC.loc_wave, 0.7)
        logger.debug('wave 2...')
        with master.set_waves(T.wave2a, T.wave2b):
            master.svt_skill(2, 1)
            master.master_skill(2, 2)
            master.auto_attack(nps=7)
            # chosen_cards = master.auto_attack(nps=6, no_play_card=True)
            # master.play_cards([chosen_cards[i] for i in (2, 0, 1)])

        # wave 3
        wait_targets(T.wave3a, LOC.loc_wave, 0.7)
        logger.debug('wave 3...')
        with master.set_waves(T.wave3a, T.wave3b):
            master.svt_skill(1, 3)
            master.svt_skill(1, 1)
            master.svt_skill(1, 2)
            master.auto_attack(nps=6, mode='alter')

        master.xjbd(T.kizuna, LOC.kizuna, mode='alter', allow_unknown=True)
        return


# noinspection DuplicatedCode
class JFree(BattleBase):
    @with_goto
    def j_charlotte(self, pre_process=False):
        """
        lily(80NP)-黑C(80NP)-孔明support-X-X-X
        """
        master = self.master
        T = master.T
        LOC = master.LOC

        master.quest_name = 'J-Charlotte'
        names = master.members = ['Lily', '黑C', '孔明']
        master.set_card_weight(dict(zip(names, [3, 1, 1.1])))

        # pre-processing: e.g. set templates, only once
        if pre_process:
            logger.debug(f'pre-process for {master.quest_name}...')
            T.read_templates('img/battles/free/j-charlotte/')

            # LOC.relocate((0, 0, 1920 - 1, 1080 - 1))

            # -----------------------    NP    Quick    Arts   Buster -----------
            master.set_cards(names[0], (1, 6), (1, 3), (2, 1), (2, 4))
            master.set_cards(names[1], (1, 7), (2, 5), (1, 1), (2, 3))
            master.set_cards_from_json(names[2], 'img/cards/jp/cards-jp.json', '孔明')

            def _handler():
                # mainly for jp, re-login handler at 3am(UTC+8)
                wait_targets(T.get('login_page'), LOC.menu_button)
                wait_targets(T.get('login1'), (1000, 480, 1350, 600), at=0, clicking=LOC.safe_area)
                # ....
                wait_targets(T.quest, LOC.quest)

            config.battle.login_handler = None if True else _handler
            return

        # battle part
        if config.battle.jump_battle:
            config.battle.jump_battle = False
            logger.warning('goto label.h')
            goto.h  # noqas

        # label.h  # noqas  # make sure master.set_waves(a,b) is called
        # master.set_waves(T.waveXa, T.waveXb)
        label.h  # noqas

        wait_targets(T.support, LOC.support_refresh)
        master.choose_support(match_svt=True, match_ce=True, match_ce_max=True, match_skills=True,
                              switch_classes=(5, 0), friend_only=False)

        # wave 1
        wait_targets(T.wave1a, LOC.loc_wave, 0.7)
        logger.debug(f'Quest {master.quest_name} started...')
        logger.debug('wave 1...')
        with master.set_waves(T.wave1a, T.wave1b):
            master.svt_skill(3, 2)
            master.svt_skill(3, 3)
            master.svt_skill(2, 1)
            master.auto_attack(nps=7, mode='alter')

        # wave 2
        wait_targets(T.wave2a, LOC.loc_wave, 0.7)
        logger.debug('wave 2...')
        with master.set_waves(T.wave2a, T.wave2b):
            master.svt_skill(3, 1, 2)
            master.svt_skill(2, 2)
            master.master_skill(1, 2)
            master.auto_attack(nps=7)

        # wave 3
        wait_targets(T.wave3a, LOC.loc_wave, 0.7)
        logger.debug('wave 3...')
        with master.set_waves(T.wave3a, T.wave3b):
            master.svt_skill(1, 2)
            master.svt_skill(1, 1)
            master.auto_attack(nps=6, mode='alter')

        master.xjbd(T.kizuna, LOC.kizuna, mode='alter', allow_unknown=True)
        return

    @with_goto
    def j_charlotte2(self, pre_process=False):
        """
        宇宙凛(80NP)-伊阿宋(80NP)-孔明support-X-X-X
        """
        master = self.master
        T = master.T
        LOC = master.LOC

        master.quest_name = 'J-Charlotte'
        names = master.members = ['宇宙凛', '伊阿宋', '孔明']
        master.set_card_weight(dict(zip(names, [3, 2, 1.1])))

        # pre-processing: e.g. set templates, only once
        if pre_process:
            logger.debug(f'pre-process for {master.quest_name}...')
            T.read_templates('img/battles/free/j-charlotte2/')

            # LOC.relocate((0, 0, 1920 - 1, 1080 - 1))

            # -----------------------    NP    Quick    Arts   Buster -----------
            master.set_cards(names[0], (1, 6), (2, 3), (1, 2), (2, 5))
            master.set_cards(names[1], (1, 7), (3, 2), (1, 4), (1, 3))
            master.set_cards_from_json(names[2], 'img/cards/jp/cards-jp.json', '孔明')

            def _handler():
                # mainly for jp, re-login handler at 3am(UTC+8)
                wait_targets(T.get('login_page'), LOC.menu_button)
                wait_targets(T.get('login1'), (1000, 480, 1350, 600), at=0, clicking=LOC.safe_area)
                # ....
                wait_targets(T.quest, LOC.quest)

            config.battle.login_handler = None if True else _handler
            return

        # battle part
        if config.battle.jump_battle:
            config.battle.jump_battle = False
            logger.warning('goto label.h')
            goto.h  # noqas

        # label.h  # noqas  # make sure master.set_waves(a,b) is called
        # master.set_waves(T.waveXa, T.waveXb)
        label.h  # noqas

        wait_targets(T.support, LOC.support_refresh)
        master.choose_support(match_svt=True, match_ce=True, match_ce_max=True, match_skills=True,
                              switch_classes=(5, 0), friend_only=False)

        # wave 1
        wait_targets(T.wave1a, LOC.loc_wave, 0.7)
        logger.debug(f'Quest {master.quest_name} started...')
        logger.debug('wave 1...')
        with master.set_waves(T.wave1a, T.wave1b):
            master.svt_skill(3, 2)
            master.svt_skill(3, 3)
            master.svt_skill(1, 1)
            master.auto_attack(nps=6, mode='alter')

        # wave 2
        wait_targets(T.wave2a, LOC.loc_wave, 0.7)
        logger.debug('wave 2...')
        with master.set_waves(T.wave2a, T.wave2b):
            master.svt_skill(2, 3)
            master.auto_attack(nps=7, mode='alter')

        # wave 3
        wait_targets(T.wave3a, LOC.loc_wave, 0.7)
        logger.debug('wave 3...')
        with master.set_waves(T.wave3a, T.wave3b):
            master.svt_skill(3, 1, 1)
            master.svt_skill(1, 3)
            master.svt_skill(1, 2, 1)
            master.master_skill(1, 1)
            master.auto_attack(nps=6, mode='dmg')

        master.xjbd(T.kizuna, LOC.kizuna, mode='alter', allow_unknown=True)
        return

    @with_goto
    def j_riverside(self, pre_process=False):
        """
        A(>10NP to all)-陈宫(80NP)-弓凛-孔明support-X-X
        """
        master = self.master
        T = master.T
        LOC = master.LOC

        master.quest_name = 'J-Riverside'
        names = master.members = ['海妈', '陈宫', '弓凛', '孔明', 'CBA']
        master.set_card_weight(dict(zip(names, [0, 1, 3, 1.09, 1.09])))

        # pre-processing: e.g. set templates, only once
        if pre_process:
            logger.debug(f'pre-process for {master.quest_name}...')
            T.read_templates('img/battles/free/j-riverside/')

            # LOC.relocate((0, 0, 1920 - 1, 1080 - 1))

            # -----------------------    NP    Quick    Arts   Buster -----------
            # master.set_cards(names[0], (), (), (), ())
            master.set_cards(names[1], (4, 7), (2, 1), (1, 2), (3, 1))
            master.set_cards(names[2], (1, 8), (2, 5), (1, 5), (1, 1))
            master.set_cards_from_json('孔明', 'img/cards/jp/cards-jp.json')
            master.set_cards_from_json('CBA', 'img/cards/jp/cards-jp.json')

            def _handler():
                # mainly for jp, re-login handler at 3am(UTC+8)
                wait_targets(T.get('login_page'), LOC.menu_button)
                wait_targets(T.get('login1'), (1000, 480, 1350, 600), at=0, clicking=LOC.safe_area)
                # ....
                wait_targets(T.quest, LOC.quest)

            config.battle.login_handler = None if True else _handler
            return

        # battle part
        if config.battle.jump_battle:
            config.battle.jump_battle = False
            logger.warning('goto label.h')
            goto.h  # noqas

        wait_targets(T.support, LOC.support_refresh)
        support = master.choose_support(match_svt=True, match_ce=True, match_ce_max=True, match_skills=True,
                                        switch_classes=(5, 0), friend_only=False,
                                        images=[master.T.support, master.T.support2])
        # logger.debug('please choose support manually!')
        if support == 0:
            names.pop(-1)
        else:
            names.pop(-2)

        # label.h  # noqas  # make sure master.set_waves(a,b) is called
        # master.set_waves(T.waveXa, T.waveXb)
        label.h  # noqas

        # wave 1
        wait_targets(T.wave1a, LOC.loc_wave, 0.7)
        logger.debug(f'Quest {master.quest_name} started...')
        logger.debug('wave 1...')
        with master.set_waves(T.wave1a, T.wave1b):
            master.svt_skill(1, 1)
            # master.auto_attack(nps=7, mode='alter')
            master.attack([7, 1, 2])
        master.members = [names[3], names[1], names[2]]  # A sacrifice

        # wave 2
        wait_targets(T.wave2a, LOC.loc_wave, 0.7, clicking=LOC.safe_area)
        logger.debug('wave 2...')
        with master.set_waves(T.wave2a, T.wave2b):
            master.svt_skill(3, 1)
            master.svt_skill(3, 3)
            master.auto_attack(nps=8, mode='alter')

        # wave 3
        wait_targets(T.wave3a, LOC.loc_wave, 0.7)
        logger.debug('wave 3...')
        if support == 0:
            with master.set_waves(T.wave3a, T.wave3b):
                master.svt_skill(1, 2)
                master.svt_skill(1, 3)
                master.svt_skill(1, 1, 3)
        else:
            with master.set_waves(T.wave3a2, T.wave3b2):
                master.svt_skill(1, 2)
                master.svt_skill(1, 3, 3)

        with master.set_waves(T.wave3a, T.wave3b):
            master.svt_skill(3, 2)
            master.svt_skill(2, 3, 3)
            # master.master_skill(2, 3)
            master.auto_attack(nps=8, mode='dmg')

        master.xjbd(T.kizuna, LOC.kizuna, mode='dmg', allow_unknown=True)
        return


# noinspection DuplicatedCode
class SFree(BattleBase):
    pass


# noinspection PyPep8Naming,DuplicatedCode
class Battle(JFree, AFree, SFree):
    """
    - it's better to load card templates from json if friend's support(need to parse card) has 3/4 sets of dress,
      e.g. Kongming, Merlin(3+1 dress), Skadi
    - ensure the same app version: e.g. command card might differ.
    """
    pass
