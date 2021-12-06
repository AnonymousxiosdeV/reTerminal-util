
# reTerminal user Keys module
# for python and  micropython

# struct input_event {
#     struct timeval time;
#     unsigned short type;
#     unsigned short code;
#     unsigned int value;
# };
import struct
EVENT_FORMAT = "llHHI"; # long, long, unsigned short, unsigned short, unsigned int
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)
    
def get_userkeys():
    infile_path = "/dev/input/by-path/platform-gpio_keys-event"
    with open(infile_path, "rb") as file:
        event = file.read(EVENT_SIZE)
        while event:
            (tv_sec, tv_usec, type, code, value) = struct.unpack(EVENT_FORMAT, event)
            #print(struct.unpack(EVENT_FORMAT, event))
            if code != 0:
                #print(f"code={code} value={value}")
                if value != 0:
                    return code
            event = file.read(EVENT_SIZE)


if __name__ == "__main__":
    infile_path = "/dev/input/by-path/platform-gpio_keys-event"

    while True:
        code=get_userkeys()
        print(code)