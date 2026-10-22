# # # k = {2:3,9:5}
# # # for s,v in enumerate(k.items()):
# # #     print(s,v)

# # def countdown_with_skip(start: int) -> list:
# #     """
# #     Using a while loop, count down from `start` to 1 (inclusive),
# #     appending each number to a list, but skip appending any
# #     number that is exactly 3 (use continue for this).
# #     Do not use break here.
# #     Return the resulting list.
# #     """
# #     k = []
# #     while start > 0:
# #         if start == 3:
# #             start -= 1  
# #         k.append(start)
# #         start -= 1      
# #     return k

# # print(countdown_with_skip(5))


# # def find_first_negative(numbers: list) -> int | None:
# #     """
# #     Using a while loop with an index variable, find and return
# #     the first negative number in `numbers`. Use break once found.
# #     If no negative number exists, use the loop's else clause to
# #     return None after the loop completes normally.
# #     """
# #     index = 0
# #     negative_num = None
    
# #     while index < len(numbers):
# #         if numbers[index] < 0:
# #             negative_num = numbers[index]
# #             break  
# #         index += 1
# #     else:
# #         return None
        
# #     return negative_num

# # print(find_first_negative([2,3,4,5,6,-1,9,-84]))

# # iterator = iter([9,345,32])

# # print(iterator)

# def first_and_last(s: str) -> str:
#     """
#     Return a new string made of the first character of `s`
#     followed by the last character of `s`.

#     - If `s` is empty, return "".
#     - If `s` has exactly one character, return that character twice.

#     Example: first_and_last("python") -> "pn"
#     """
#     if s=="":
#         return ""
#     elif len(s) == 1:
#         return s
#     else:
#         return f"{s[0],s[-1]}"


# def reverse_string(s: str) -> str:
#     """
#     Return a new string containing the characters of `s` in
#     reverse order. Use a slice with a negative step.

#     Example: reverse_string("python") -> "nohtyp"
#     """
#     return s[::-1]


# def every_kth_from(s: str, start: int, k: int):
#     """
#     Return the characters of `s` at positions start, start + k,
#     start + 2k, ... continuing to the end of the string.
#     `start` may be negative (counted from the end). `k` is
#     always >= 1. If `start` is out of range, return "".

#     Example: every_kth_from("abcdefgh", 1, 3) -> "beh"
#     """
# #     for i in range(len(s)):
# #         if start+i*k<len(s):
# #             print(s[start+i*k])

# # every_kth_from("erenYeager",0,10)


# # print(first_and_last("mikasa"))

