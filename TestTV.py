#Import file TV Program.py
from TV import TV

#Methods of TestTV
def main():

    #tv1's channel is 30 and volume level is 3

    #Object 1 of the TV class
    tv1 = TV()

    #Turn on TV 1
    tv1.turn_on()

    #Set TV 1's channel 
    tv1.set_channel(30)

    #Set TV 1's volume level
    tv1.set_volume_level(3)

    #Print the channel and volume level that is set for TV 1
    print("\033[0;33m\ntv1's channel", tv1.get_channel(), "and volume level is", tv1.get_volume_level())


    #tv2's channel is 3 and volume level is 2

    #Object 2 of the TV class
    tv2 = TV()

    #Turn on TV 2
    tv2.turn_on()

    #Set TV 2's channel
    tv2.set_channel(3)

    #Set TV 2's volume level
    tv2.set_volume_level(2)

    #Print the chennel and volume level that is set for TV 2
    print("\033[0;31m\ntv2's channel is",tv2.get_channel(), "and volume level is", tv2.get_volume_level())
    print("\033[1;37m~" * 90)

if __name__ == "__main__":
        main()

