import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power - False, Channel - 0, Volume - 0"

def test_power():
    tv = Television()
    tv.power()
    assert tv._Television__status == True
    tv.power()
    assert tv._Television__status == False

def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv._Television__muted == True
    tv.mute()
    assert tv._Television__muted == False

def test_channel_up():
    tv = Television()
    tv.power()
    tv._Television__channel = Television.MIN_CHANNEL
    tv.channel_up()
    assert tv._Television__channel == 1
    tv.channel_up()
    assert tv._Television__channel == 2
    tv.channel_up()
    assert tv._Television__channel == 3
    tv.channel_up()
    assert tv._Television__channel == 0


def test_channel_down():
    tv = Television()
    tv.power()
    tv._Television__channel = Television.MAX_CHANNEL
    tv.channel_down()
    assert tv._Television__channel == 2
    tv.channel_down()
    assert tv._Television__channel == 1
    tv.channel_down()
    assert tv._Television__channel == 0
    tv.channel_down()
    assert tv._Television__channel == 3


def test_volume_up():
    tv = Television()
    tv.power()
    tv._Television__muted = True
    tv._Television__volume = 0
    tv.volume_up()
    assert tv._Television__muted == False
    assert tv._Television__volume == 1
    tv.volume_up()
    assert tv._Television__volume == 2
    tv.volume_up()
    assert tv._Television__volume == 2

def test_volume_down():
    tv = Television()
    tv.power()
    tv._Television__muted = True
    tv._Television__volume = 2
    tv.volume_down()
    assert tv._Television__muted == False
    assert tv._Television__volume == 1
    tv.volume_down()
    assert tv._Television__volume == 0
    tv.volume_down()
    assert tv._Television__volume == 0

