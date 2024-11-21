from datalink import datareceiver, datalinker
from speaker import spk


class Transport:
    def __init__(self, crc_value = "00", crc = False, segment = []):
        self.crc = crc
        self.segment = segment
        self.crc_value = crc_value
        pass
    
    def reciver_flowcontrol(self, segment):
        result = datareceiver.robot_receiver(segment)
        if result is None:
            return False, None


        entire_frame, crc_value, data = result
        data_hex = hex(int(data))[2:]
        print(f"crc_value: {crc_value}. data: {data_hex}")
        calc_crc = datalinker.CRC8(data_hex).upper()
        print(f"calc_crc: {calc_crc}")

        # Receiver side
        if(crc_value == calc_crc):
            print("CRC check passed")
            # Send ACK
            #spk.play_dtmf_tone("A")
            #spk.play_dtmf_tone("0")
            #spk.play_dtmf_tone("1")
            #spk.play_dtmf_tone("F")
            #spk.play_dtmf_tone("A")
            # We need to tell session layer that we have a correct CRC value

            crc_value = ""
            data = ""
            return True
        
flowcontrol = Transport()
    #def transmitter_flowcontrol(self,)
        