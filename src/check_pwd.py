"""
A library to check the validity of password input by users.
Following are the criteria for checking the password:
○ At least 1 letter between [a-z]
○ At least 1 number between [0-9]
○ At least 1 letter between [A-Z]
○ At least 1 character from [$#@]
○ Minimum length of transaction password: 6
○ Maximum length of transaction password: 12
The function accepts a sequence of comma separated passwords
and will check them according to the above criteria. Passwords that
match the criteria are to be printed, each separated by a comma
Example -
input_password =Asqwr1234@1,aF145#,2w3E*,2We3345
Output = Asqwr1234@1
"""
import re

from typing import List

def is_valid_pwd(st: str) -> bool:
    """ Return True if given string follows the criteria below:
        ○ At least 1 letter between [a-z]
        ○ At least 1 number between [0-9]
        ○ At least 1 letter between [A-Z]
        ○ At least 1 character from [$#@]
        ○ Minimum length of transaction password: 6
        ○ Maximum length of transaction password: 12"""
    # use lookahead regx to look for a-z 0-9 A-Z and S#@ in any order
    # pattern = r'^(?=.*[a-z]+?)(?=.*[A-Z]+?)(?=.*[0-9]+?)(?=.*[$#@]).{6,12}$'
    length = len(st)
    if (length < 6 or length > 12):
        return False
    return all(re.search(pattern, st) for pattern in ('[A-Z]+', '[a-z]+', r'\d+', r'[$#@]+'))

def get_passwords(pwd: str, separator: str=',') -> List[str]:
    res = []
    for pwd in pwd.split(separator):
        if is_valid_pwd(pwd):
            res.append(pwd)
    return res

def print_pwds(pwd: str, separator: str=',' ) -> None:
    pwd_list = get_passwords(pwd, separator)
    print(','.join(pwd_list))