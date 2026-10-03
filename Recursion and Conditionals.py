def is_valid_part(part):
    if not part.isdigit():
        return False
    number = int(part)
    if number < 0 or number > 255:
        return False
    if len(part) > 1 and part[0] == "0":
        return False
    return True


def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not is_valid_part(p):
            return False
    return True


def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)


def binary_to_decimal(b):
    if b == "":
        return 0
    first_bit = int(b[0])
    place_value = 2 ** (len(b) - 1)
    return first_bit * place_value + binary_to_decimal(b[1:])


def pad_to_8(b):
    while len(b) < 8:
        b = "0" + b
    return b


def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return "Invalid IP address"
    result = ""
    for p in ip.split("."):
        if result != "":
            result = result + "."
        result = result + pad_to_8(decimal_to_binary(int(p)))
    return result

def is_binary_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if len(p) != 8:
            return False
        for ch in p:
            if ch != "0" and ch != "1":
                return False
    return True


def binary_to_ip(ip):
    if not is_binary_ip(ip):
        return "Invalid IP address"
    result = ""
    for p in ip.split("."):
        if result != "":
            result = result + "."
        result = result + str(binary_to_decimal(p))
    return result


def ip_convert(ip):
    if is_binary_ip(ip):
        return binary_to_ip(ip)
    elif is_valid_ip(ip):
        return ip_to_binary(ip)
    else:
        return "Invalid IP address"


print(is_valid_part("255"))  # True
print(is_valid_part("256"))  # False
print(is_valid_part("01"))  # False
print(is_valid_part("0"))  # True

print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("192.168.256.1"))  # False
print(is_valid_ip("192.168.1"))  # False
print(is_valid_ip("192.168.01.1"))  # False

print(decimal_to_binary(10))  # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))  # "1"

print(binary_to_decimal("1010"))  # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))  # 1

print(ip_to_binary("192.168.1.1"))  # "11000000.10101000.00000001.00000001"
print(ip_to_binary("255.255.255.0"))  # "11111111.11111111.11111111.00000000"
print(ip_to_binary("256.1.1.1"))  # "Invalid IP address"

print(ip_convert("192.168.1.1"))  # binary version
print(ip_convert("11000000.10101000.00000001.00000001"))  # "192.168.1.1"
print(ip_convert("999.1.1.1"))  # "Invalid IP address"