
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        
    def power(self):
        power = self.__status
        if power == False:
            self.__status = True
        elif power == True:
            self.__status = False
            
    def mute(self):
        mute = self.__muted
        if mute == False:
            self.__muted = True
        elif mute == True:
            self.__muted = False
            
    def channel_up(self):
        channel = self.__channel
        if self.__status == True:
            if channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
        
    def channel_down(self):
        channel = self.__channel
        if self.__status == True:
            if channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
        
    def volume_up(self):
        if self.__status == True:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
        
    def volume_down(self):
        if self.__status == True:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
        
    def __str__(self):
        power = self.__status
        channel = self.__channel
        if self.__muted == True and self.__status == True:
            volume = 0
        else:
            volume = self.__volume
        return f'Power = {power}, Channel = {channel}, Volume = {volume}'
    
