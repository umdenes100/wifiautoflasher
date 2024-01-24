import os

import RPi.GPIO as GPIO

GPIO_BUTTON = 17


def write_to_screen(text: str):
    print(text)

def fetch_from_github():
    write_to_screen("Fetching from github")
    os.makedirs("firmware", exist_ok=True)
    files = ["firmware.ino", "helpers.h", "vs_stuff.ino"]
    files = [os.path.join("firmware", file) for file in files]
    checksums = [int(os.system(f"md5sum {file}")) for file in files]
    # fetch the files from GitHub into temp
    root_url = 'https://github.com/umdenes100/WifiFirmware/blob/master/'
    for file in files:
        os.system(f"wget {root_url}{file} -O {file}")
    new_checksums = [int(os.system(f"md5sum {file}")) for file in files]
    print('old: ', checksums, 'new: ', new_checksums)
    return checksums != new_checksums

def compile_for_esp8266():
    write_to_screen("Compiling for esp8266")
    # todo get correct fdqm
    os.system("arduino-cli compile -b esp8266:esp8266:generic firmware")


def upload_to_esp8266():
    write_to_screen("Uploading to esp8266")
    # todo get correct fdqm
    os.system("arduino-cli upload -p /dev/ttyUSB0 -b esp8266:esp8266:generic firmware")


def main():
    while True:
        GPIO.wait_for_edge(GPIO_BUTTON, GPIO.FALLING)
        print("Button pressed, lets get this going.")
        was_changes = fetch_from_github()
        if was_changes:
            compile_for_esp8266()

        upload_to_esp8266()


if __name__ == "__main__":
    main()