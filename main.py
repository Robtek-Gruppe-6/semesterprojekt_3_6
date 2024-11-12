from control import *
from decoding import decoder
from filter import fil
from speaker import spk
from microphone import micro
from plotting import plot
from UI import ui
from datalink import datalinker
from dataframer import framer

def main():
    
    try:
       for audio_chunk in micro.capture_audio():
           filtered_chunk = fil.butter_bandpass(audio_chunk)
           frequencies, magnitude = fil.analyze_frequency(filtered_chunk)
           
           binary_val = decoder.process_chunk(frequencies, magnitude)
           framer.input_binary()
           
           if binary_val is not None:
               result = datalinker.receive_data(binary_val)
               if result:
                    
                    collected_data, data_length = result
                    print("Collected Data:", [bin(int(b, 2))[2:].zfill(4) for b in collected_data])
                    print("Data Length:", data_length)
           
           
           
    finally:
        micro.close()
        
        


if __name__ == "__main__":
    #ui.run_example() #UI example code
    #ui.run_protocol() #Runs the movementProtocol but it needs to display that into the UI SO NOT DONE!
    main()
    




