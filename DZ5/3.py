# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode_rle (data):
    encode = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encode += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encode += str(count) + prev_char
        return encode

def decode_rle (data):
    decode = ""
    count = ""
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ""
    return decode

with open('ДЗ5/text.txt', 'r') as file:
    text = file.read()

with open('ДЗ5/rle_text.txt', 'w') as file:
    rle_text = encode_rle(text)
    file.write(rle_text)

with open('ДЗ5/rle_text.txt', 'r') as file:
    decoding = file.read()

print(f'{decode_rle(decoding)}')
