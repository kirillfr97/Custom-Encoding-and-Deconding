from custom_codec import CustomCodec

if __name__ == "__main__":

    test_string = "Hello, Wonderful Z! 123"
    # test_string = "Hello World! 123"

    print(f"Original string: {test_string}")

    # Create a custom encoding and decoding object
    codec = CustomCodec()

    # Encode a string
    encoded_string = codec.encode(test_string)
    print(f"Encoded string: {encoded_string}")

    # Decode a string
    decoded_string = codec.decode(encoded_string)
    print(f"Decoded string: {decoded_string}")