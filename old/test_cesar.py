from cesar.decrpt import decrypt
from cesar.encript import encript


def test_encrypt():
    result = encript(text="abcd", step=1)
    assert result == "bcde"


def test_decrypt():
    result = decrypt(encripted_text="bcde", step=1)
    assert  result == "abcd"


if __name__ == "__main__":
    #test_decrypt()
    test_encrypt()