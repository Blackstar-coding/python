
class Television:
    """
    A class that contains details and methods for a television object.
    """
    
    """
    Class Variables
    :param min_volume: Minimum possible volume value
    :param max_volume: Maximum possible volume value
    :param min_channel: Minimum possible channel value
    :param max_channel: Maximum possible channel value
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self) -> None:
        """
        Method to set instance variables to default for the television object
        :param status: Whether the television is on or off
        :param muted: Whether the television is muted or not
        :param volume: Television's volume
        :param channel: Television's channel
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        
    def power(self) -> None:
        """
        Method to turn the power on and off
        :param power: Stores the status variable
        """
        
        power = self.__status
        if power == False:
            self.__status = True
        elif power == True:
            self.__status = False
            
    def mute(self) -> None:
        """
        Method to mute and unmute the television
        :param mute: Stores the muted variable
        """
        
        mute = self.__muted
        if mute == False:
            self.__muted = True
        elif mute == True:
            self.__muted = False
            
    def channel_up(self) -> None:
        """
        Method to increase the channel
        Loops back to minimum channel when attempting to increase passed maximum channel
        :param channel: Stores the channel variable
        """
        
        channel = self.__channel
        if self.__status == True:
            if channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
        
    def channel_down(self) -> None:
        """
        Method to decrease the channel
        Loops to the maximum channel when attempting to decreased passed the minimum channel
        :param channel: Stores the channel variable
        """
        
        channel = self.__channel
        if self.__status == True:
            if channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
        
    def volume_up(self) -> None:
        """
        Method to increase the volume
        Unmutes the television if it was muted
        Doesn't increase volume if the volume is at the max
        """ 
        
        if self.__status == True:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
        
    def volume_down(self) -> None:
        """
        Method to decrease the volume
        Unmutes the television if it was muted
        Doesn't decrease volume if the volume is at the minimum
        """
        if self.__status == True:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
        
    def __str__(self) -> str:
        """
        Method to return the television's power, channel, and volume
        Volume is returned as zero if the television is muted and on
        :param power: Stores the status variable
        :param channel: Stores the channel variable
        :param volume: Stores the volume variable
        """
        power = self.__status
        channel = self.__channel
        if self.__muted == True and self.__status == True:
            volume = 0
        else:
            volume = self.__volume
        return f'Power = {power}, Channel = {channel}, Volume = {volume}'
    
