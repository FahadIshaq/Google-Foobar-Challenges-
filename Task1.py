# import re


# def Solution(s):
#     result = ""
#     special_char = re.compile('[@_!$%^&*()<>?/\|}{~:]#')
#     a = "abcdefghijklmnopqrstuvwxyz"
#     for i in range(len(s)):
#         k = 0
#         while (k != 26):
#             if (s[i] == a[k]):
#                 result += a[26-k-1]
#                 break
#             elif (s[i].isupper()):
#                 result += s[i]
#                 break
#             elif (s[i] == special_char):
#                 print("here")
#                 result += s[i]
#                 break

#             k += 1
#     return result


# print(Solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))

def solution(s):
    result = ""

    # only small case letters are switched
    for i in range(len(s)):
        # iterate over every character in s:
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            # this character is encrypted
            result += chr(122 - ord(s[i]) + 97)
        else:
            result += s[i]
    return result


solution(s)