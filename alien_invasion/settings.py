class Settings:
    """存储游戏（外星人入侵）中所有的设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_with = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed = 1.5
