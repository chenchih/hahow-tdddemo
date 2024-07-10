import pytest
from login import login_by_username_and_password

@pytest.mark.parametrize(
    argnames="username, password, expected",
    argvalues=[
        ["cc", "test123456", "login success"],
                ["cc", "yyyyyy", ValueError]
    ], 
    ids=[1,2]
 

)
def test_login_by_username_and_password(username, password, expected):
    if isinstance(expected, str):
        result= login_by_username_and_password(
            
            username=username,
            password=password
        )
        print(result)
        assert result == expected
    else:
        with pytest.raises(expected) as exc:
            login_by_username_and_password(
                username=username,
                password=password
            )
        print(exc.value.__class__)
        assert exc.value.__class__== expected

