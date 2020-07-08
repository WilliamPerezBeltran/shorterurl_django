from django.db import models
import hashlib
import pdb
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class Url(models.Model):
    url_text = models.CharField(max_length=200)
    url_base62 = models.CharField(max_length=200)

    def decode_url_string_to_base62(self, url):
        validate = URLValidator()
        try:
            validate(url)
        except ValidationError as e:
            return e

        _alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # convert string to md5
        md5 = hashlib.md5()
        md5.update(url.encode("utf-8"))
        # convert md5 to exadecimal
        hexa = md5.hexdigest()
        # convet hexadecimal to decimal
        decimal = int(hexa, 16)

        # convert decimal to base62
        array_base62 = []

        base62 = ""

        while decimal > 0:
            array_base62.append(int(decimal % 62))
            decimal = decimal // 62

        for posicion in reversed(array_base62):
            base62 += _alphabet[posicion]

        # return base62 number
        return base62

    def __str__(self):
        return self.url_text
