import serial
import time
import json

ser = serial.Serial('COM4', 115200, timeout=1)


def main():
    ser.isOpen()

    print('Enter your commands below.\r\nInsert "exit" to leave the application.')

    while True:
        # get keyboard input
        string = input(">> ")
        # Python 3 users
        # input = input(">> ")
        if string == 'exit':
            ser.close()
            exit()
        else:
            # send the character to the device
            # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
            #s = json.loads(string)
            ser.write((string + '\n').encode('utf-8'))
            out = ''
            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(1)
            while ser.inWaiting() > 0:
                output = ser.read(1)
                out += output.decode("utf-8")

            if out != '':
                print(">>" + out)


if __name__ == "__main__":
    main()
