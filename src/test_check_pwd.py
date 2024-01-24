import pytest

from . import check_pwd

def test_is_valid_pwd():
    assert check_pwd.is_valid_pwd('aF145#<')
    assert check_pwd.is_valid_pwd('asAqwr1234@1')

def test_invalid_pwd():
    assert not check_pwd.is_valid_pwd('abc')
    assert not check_pwd.is_valid_pwd('123456')

def test_is_valid_pwd_empty():
    assert not check_pwd.is_valid_pwd('')

def test_is_valid_pwd_incorrect_length():
    assert not check_pwd.is_valid_pwd('')
    assert not check_pwd.is_valid_pwd('1aF#')
    assert not check_pwd.is_valid_pwd('@Favb#dsf29dsafsa1aF#')

def test_check_pwd():
    assert check_pwd.get_passwords('asAqwr1234@1,aF145#,2w3E*,@Favb#,9zMX*') == ['asAqwr1234@1','aF145#']
    assert check_pwd.get_passwords('abc,123') == []

def test_print_pwd(capsys: pytest.CaptureFixture[str]):
    check_pwd.print_pwds('asAqwr1234@1,aF145#,2w3E*,@Favb#,9zMX*')
    captured = capsys.readouterr()
    assert captured.out == 'asAqwr1234@1,aF145#\n'