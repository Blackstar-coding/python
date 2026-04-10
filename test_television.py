import pytest
from television import *

class Test:
    def setup_method(self):
        self.t1 = Television()
        self.t1.power()
        
    def test_init(self):
        # Since every other test needs the power on I have to manually turn it back off for the test
        self.t1.power()
        assert self.t1._Television__status == False
        assert self.t1._Television__muted == False
        assert self.t1._Television__volume == 0
        assert self.t1._Television__channel == 0
        
    def test_power(self):
        assert self.t1._Television__status == True
        self.t1.power()
        assert self.t1._Television__status == False
        
    def test_mute(self):
        assert self.t1._Television__muted == False
        self.t1.mute()
        assert self.t1._Television__muted == True
        self.t1.mute()
        assert self.t1._Television__muted == False
        
    def test_channel_up(self):
        assert self.t1._Television__channel == 0
        self.t1.channel_up()
        assert self.t1._Television__channel == 1
        self.t1.channel_up()
        assert self.t1._Television__channel == 2
        self.t1.channel_up()
        assert self.t1._Television__channel == 3
        self.t1.channel_up()
        assert self.t1._Television__channel == 0
        
    def test_channel_down(self):
        assert self.t1._Television__channel == 0
        self.t1.channel_down()
        assert self.t1._Television__channel == 3
        self.t1.channel_down()
        assert self.t1._Television__channel == 2
        self.t1.channel_down()
        assert self.t1._Television__channel == 1
        self.t1.channel_down()
        assert self.t1._Television__channel == 0
        
    def test_volume_up(self):
        assert self.t1._Television__volume == 0
        self.t1.volume_up()
        assert self.t1._Television__volume == 1
        self.t1.volume_up()
        assert self.t1._Television__volume == 2
        self.t1.volume_up()
        assert self.t1._Television__volume == 2
        
    def test_volume_down(self):
        assert self.t1._Television__volume == 0
        self.t1.volume_down()
        assert self.t1._Television__volume == 0
        self.t1.volume_up()
        self.t1.volume_up()
        assert self.t1._Television__volume == 2
        self.t1.volume_down()
        assert self.t1._Television__volume == 1
        self.t1.volume_down()
        assert self.t1._Television__volume == 0
        
    
if __name__ == "__main__":
    pytest.main()