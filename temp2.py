com = " ABGR: Wnpx - grzcbenel olcnff: hfr urnqre K-Qri-Npprff: lrf "
def rot13(s):
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            rotated = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result.append(rotated)
        elif 'A' <= char <= 'Z':
            rotated = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(rotated)
        else:
            result.append(char)
    return ''.join(result)

com_rot13 = rot13(com)
print(com_rot13)