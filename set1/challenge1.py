__author__ = 'Kelsey Gilmore-Innis'


def convert_to_base64(hex_input):
    import base64
    bytes = bytearray.fromhex(hex_input)
    return base64.b64encode(bytes)
