import configparser

class ImportSettings:
    def __init__(self, config_file='settings.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, section, key):
        return self.config.get(section, key)

    def get_int(self, section, key):
        return self.config.getint(section, key)

    def get_float(self, section, key):
        return self.config.getfloat(section, key)

    def get_boolean(self, section, key):
        return self.config.getboolean(section, key)

class GetSettings: 
    settings = ImportSettings()
    
    def __init__(self):
        self.SETUP_APP_NAME             = self.settings.get('SETUP', 'APP-NAME')
        self.SETUP_COM_PORT             = self.settings.get('SETUP', 'COM-PORT')
        self.SETTINGS_TOGGLE_KEY        = self.settings.get('SETTINGS', 'TOGGLE-KEY')
        self.SETTINGS_TARGET_BONE       = self.settings.get('SETTINGS', 'TARGET-BONE')
        self.SETTINGS_X_FOV             = self.settings.get_int('SETTINGS', 'X-FOV')
        self.SETTINGS_Y_POV             = self.settings.get_int('SETTINGS', 'Y-FOV')
        self.SETTINGS_INGAME_SENS       = self.settings.get_float('SETTINGS', 'INGAME-SENS')
        self.AIMBOT_ENABLED             = self.settings.get_boolean('AIMBOT', 'ENABLED') 
        self.AIMBOT_KEY_BIND            = int(self.settings.get('AIMBOT', 'KEY-BIND'), 16)
        self.AIMBOT_Y_SPEED             = self.settings.get_float('AIMBOT', 'Y-SPEED')
        self.AIMBOT_X_SPEED             = self.settings.get_float('AIMBOT', 'X-SPEED')
        self.TRIGGERBOT_ENABLED         = self.settings.get_boolean('TRIGGERBOT', 'ENABLED') 
        self.TRIGGERBOT_KEY_BIND        = int(self.settings.get('TRIGGERBOT', 'KEY-BIND'), 16)
        self.TRIGGERBOT_X_THRESHOLD     = self.settings.get_int('TRIGGERBOT', 'X-THRESHOLD')
        self.TRIGGERBOT_Y_THRESHOLD     = self.settings.get_int('TRIGGERBOT', 'Y-THRESHOLD')
        self.TRIGGERBOT_DELAY_BEFORE    = self.settings.get_float('TRIGGERBOT', 'DELAY-BEFORE-SHOOT')
        self.TRIGGERBOT_DELAY_AFTER     = self.settings.get_float('TRIGGERBOT', 'DELAY-AFTER-SHOOT') 
        self.SILENTBOT_ENABLED          = self.settings.get_boolean('SILENTBOT', 'ENABLED')
        self.SILENTBOT_KEY_BIND         = int(self.settings.get('SILENTBOT', 'KEY-BIND'), 16)
        self.SILENTBOT_ONLY_FLICK       = self.settings.get_boolean('SILENTBOT', 'ONLY-FLICK')
        self.FLICKSPEED                 = 1.07437623 * self.SETTINGS_INGAME_SENS ** (-0.9936827126)
    
    def GetSetupAppName(self):
        return self.SETUP_APP_NAME
    
    def GetSetupComPort(self):
        return self.SETUP_COM_PORT
    
    def GetSettingsToggleKey(self):
        return self.SETTINGS_TOGGLE_KEY
    
    def GetSettingsTargetBone(self):
        return self.SETTINGS_TARGET_BONE
    
    def GetSettingsXFov(self):
        return self.SETTINGS_X_FOV
    
    def GetSettingsYFov(self):
        return self.SETTINGS_Y_POV
    
    def GetSettingsIngameSens(self):
        return self.SETTINGS_INGAME_SENS
    
    def GetAimbotEnabled(self):
        return self.AIMBOT_ENABLED
    
    def GetAimbotKeyBind(self):
        return self.AIMBOT_KEY_BIND
    
    def GetAimbotYSpeed(self):
        return self.AIMBOT_Y_SPEED
    
    def GetAimbotXSpeed(self):
        return self.AIMBOT_X_SPEED
    
    def GetTriggerbotEnabled(self):
        return self.TRIGGERBOT_ENABLED
    
    def GetTriggerbotKeyBind(self):
        return self.TRIGGERBOT_KEY_BIND
    
    def GetTriggerbotXThreshold(self):
        return self.TRIGGERBOT_X_THRESHOLD

    def GetTriggerbotYThreshold(self):
        return self.TRIGGERBOT_Y_THRESHOLD

    def GetTriggerbotDelayBefore(self):
        return self.TRIGGERBOT_DELAY_BEFORE

    def GetTriggerbotDelayAfter(self):
        return self.TRIGGERBOT_DELAY_AFTER

    def GetSilentbotEnabled(self):
        return self.SILENTBOT_ENABLED

    def GetSilentbotKeyBind(self):
        return self.SILENTBOT_KEY_BIND

    def GetSilentbotOnlyFlick(self):
        return self.SILENTBOT_ONLY_FLICK

    def GetFlickSpeed(self):
        return self.FLICKSPEED