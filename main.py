from custom_codec import CustomCodec

if __name__ == "__main__":
    # Hello World! 123
    # I101mm111 X111sme! 123
    # m111I101m smeX111! 123
    # m111M101u sngA111! 123
    # m11#1M1#01u# sn#gX1#11!# 12#3
    # m11#1M1#01u# sn#gX1#11!# 63#9

    test_string = "Hello World! 123"
    # test_string = "Hello, Wonderful Z! 123"
    # test_string = "Happy New Year 2025"

    print(f"Original string: {test_string}")

    # Create a custom encoding and decoding object
    codec = CustomCodec()

    # Encode a string
    encoded_string = codec.encode(test_string)
    print(f"Encoded string: {encoded_string}")

    # Decode a string
    decoded_string = codec.decode(encoded_string)
    print(f"Decoded string: {decoded_string}")