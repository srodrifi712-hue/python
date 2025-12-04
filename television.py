class Television:
    """Creates the class with default settings with a max and min for volume and channel"""
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Starts it with the default settings"""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Changes status to the opposite of the current boolean"""
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """Changes the mute to the opposite of the current boolean"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """If the tv is on, the channel goes up 1, but if it is at the maximum, it goes to the start."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """If the tv is on, the channel goes down 1, but if it is at the minimum, it goes to the end."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """If the tv is on, the volume goes up 1 unless it is at the maximum. Automatically unmutes."""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """If the tv is on, the volume goes down 1 unless it is at the minimum. Automatically unmutes."""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """If muted, then volume is 0. Returns the info of the television"""
        display_volume: int = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}"
