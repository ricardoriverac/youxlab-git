import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/aclk?sa=L&ai=DChsSEwj7z6fOnKaQAxWEXEgAHQaeGrgYACICCAEQABoCY2U&co=1&ase=2&gclid=Cj0KCQjwjL3HBhCgARIsAPUg7a77pPzFXAsoidGKCIUpowToBVLYgj-iVgs2GZahVvi7_4eHwF0V9c8aAklmEALw_wcB&cid=CAASWeRoSYvsShPKn7OAfzWdTTovG1u6KrQOPI6WA6NHlOpZHqpD8Zp8yr39rRt4YVzOqW9N6ih5LNNdKPRRLxGxe242bQlEcTnpbjKdTndBMwgniQDeW_vZXEb3&cce=2&category=acrcp_v1_32&sig=AOD64_1Lb0xUEBg3XIggLqU6duGn1OmkKQ&q&nis=4&adurl&ved=2ahUKEwjzkaPOnKaQAxVlHrkGHVegIioQ0Qx6BAgMEAE')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site iFood com sucesso!')
