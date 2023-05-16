#Alexza Jean R. Catanoy
#BSCPE 1-4
#TV and a Test Driver Program named TestTV

#Title
print("\033[0;36m*" * 90)
print("\033[1;97mClass named TV and a Test Driver program named TestTV".center(97))
print("\033[0;36m*" * 90)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4")
print("-" * 90)

class TV:

    #Constructor
    def __init__(self):

        #channel: int (The current channel (1 to 120) of this TV.)
        self.channel = 1

        #volumelevel: int (The current volume (1 to 7) of this TV.)
        self.volumelevel = 1

        #on: bool (Indicates whether this TV is on/off)
        self.on = False
        

    #Methods of this UML Class Diagram
       
    #turnON(): None (Turns on this TV.)
    def turn_on(self):
        self.on = True

    #turnOFF(): None (Turns off this TV.)
    def turn_off(self):
        self.on = False

    #getChannel(): int (Returns the channel for this TV.)
    def get_channel(self):
        return self.channel
        
    #setChannel(channel: int): None (Sets a new channel for this TV.)
    def set_channel(self, channel):
         if self.on and 1 <= channel <= 120:
            self.channel = channel

    #getVolume(): int (Gets the volume for this TV.)
    def get_volume_level(self):
        return self.volume_level
        
    #setVolume(volume_level: int):  None (Sets a new volume level for this TV.)
    def set_volume_level(self, volume_level):
        if self.on and 1 <= volume_level <= 7:
            self.volume_level = volume_level

    #channelUp(): None (Increases the channel number by 1.)
    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1

    #channelDown(): None (Decreases the channel number by 1.)
    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    #volumeUp(): None (Increases the volume level by 1.)
    def volume_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1

    #volumeDown(): None (Decreases the volume level by 1.)
    def volume_down(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1

    
    
    

