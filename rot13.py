def rot13(str_in):
    str_out = ""
    for char_in in str_in:
        if 'A' <= char_in <= 'Z':
            str_out += chr(ord('A') + (ord(char_in) - ord('A') + 13) % 26) 
        elif 'a' <= char_in <= 'z':
            str_out += chr(ord('a') + (ord(char_in) - ord('a') + 13) % 26)
        else:
            str_out += char_in

    return str_out
