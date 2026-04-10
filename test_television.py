import pytest
from television import *

class Test:
    def setup_method(self):
        self.t1 = Television()
        
    def teardown_method(self):
        del self.t1
        
    def test_init(self):
        assert self.t1._Television__status == False
        assert self.t1._Television__muted == False
        assert self.t1._Television__volume == 0
        assert self.t1._Television__channel == 0
        
    def test_power(self):
        self.t1.power()
        assert self.t1._Television__status == True
        self.t1.power()
        assert self.t1._Television__status == False
        
    def test_mute(self):
        self.t1.power()
        assert self.t1._Television__muted == False
        self.t1.mute()
        assert self.t1._Television__muted == True
        self.t1.mute()
        assert self.t1._Television__muted == False
        
    def test_channel_up(self):
        self.t1.power()
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
        self.t1.power()
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
        self.t1.power()
        assert self.t1._Television__volume == 0
        self.t1.volume_up()
        assert self.t1._Television__volume == 1
        self.t1.volume_up()
        assert self.t1._Television__volume == 2
        self.t1.volume_up()
        assert self.t1._Television__volume == 2
        
    def test_volume_down(self):
        self.t1.power()
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