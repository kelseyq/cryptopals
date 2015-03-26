__author__ = 'Kelsey Gilmore-Innis'

def convert_to_base64(input):
    import base64
    bytes = bytearray.fromhex(input)
    return base64.b64encode(bytes)