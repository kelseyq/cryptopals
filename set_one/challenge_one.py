__author__ = 'Kelsey Gilmore-Innis'

def convert_to_base64(input):
    import base64
    bytes = bytearray.fromhex(input)
    return base64.b64encode(bytes)

if __name__ == "__main__":
    import sys
    input_string = sys.argv[1]
    print(convert_to_base64(input_string))