# -*- coding: UTF-8 -*-
"""
@author: MaLj 
@contact: malj@163.com
@site: www.e-law.com
@version: 1.0
@file: game_stats.py.py
@time: 2017/12/8 15:22

这一行开始写关于本文件的说明与解释
"""
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于活动状态
        self.game_active = False
        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化随游戏运行可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
