def is_power(number,base):
    if number<base:
        if number!=1:
            return 0
        return 1
    return is_power(number/base,base)

print(is_power(8,2)) # as 2^3 = 8 return 1
print(is_power(16,2)) # 2^4 = 16 return 1
print(is_power(64,3)) # as there is no number which 3^ = 64 return 0 false

