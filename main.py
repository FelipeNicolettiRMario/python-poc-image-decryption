import os


def encrypt(content: bytes, key: int) -> bytearray:
    image = bytearray(content)

    for index, values in enumerate(image):
        image[index] = values ^ key

    return image


def decrypt(key: int, encrypted_content: bytearray) -> bytearray:

    for index, values in enumerate(encrypted_content):
        encrypted_content[index] = values ^ key

    return encrypted_content


def encrypt_image(path_to_image: str, key: int):
    if os.path.exists(path_to_image):
        with open(path_to_image, "rb") as image:
            image_bytes = image.read()

        encrypted_content = encrypt(image_bytes, key)

        output_path = f"{os.getcwd()}/encrypted/{path_to_image.split('/')[-1]}"

        with open(output_path, "wb") as image_encrypted:
            image_encrypted.write(encrypted_content)

        return output_path, key
    else:
        raise FileExistsError


def decrypt_image(file_path: str, key: int):

    with open(file_path, "rb") as image:
        image_bytes = image.read()

    decrypted_image = decrypt(key, bytearray(image_bytes))

    with open(f"{os.getcwd()}/decrypted/{file_path.split('/')[-1]}", "wb") as output_file:
        output_file.write(decrypted_image)


if __name__ == "__main__":
    path = "/media/felipenicolettireismario/58449FBC449F9AF8/Imagens/Wallpapers/godfather.jpg"
    path, key = encrypt_image(path, 22)

    decrypt_image(path, key)
