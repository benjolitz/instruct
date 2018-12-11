from instruct import parse_typedef
from typing import List, Union, AnyStr, Any
from instruct import make_custom_typecheck


def test_parse_typedef():

    custom_type = make_custom_typecheck(lambda val: val == 3)
    assert isinstance(3, custom_type)

    assert parse_typedef(Union[int, AnyStr]) == (int, str, bytes,)

    ListOfInts = parse_typedef(List[int])
    assert isinstance([1, 2, 3], ListOfInts)
    assert not isinstance([1, 2, 3.1], ListOfInts)
    ListOfIntsOrStrs = parse_typedef(List[Union[int, str]])
    assert isinstance(['a', 1, 2], ListOfIntsOrStrs)
    assert not isinstance(['a', 1, 2, {}], ListOfIntsOrStrs)
    ListOfIntsOrAnyStr = parse_typedef(List[Union[int, AnyStr]])
    assert isinstance(['a', b'b', 1], ListOfIntsOrAnyStr)
    assert not isinstance(['a', b'b', 1, [1]], ListOfIntsOrAnyStr)
    Anything = parse_typedef(Union[Any, AnyStr])
    assert isinstance({}, Anything)
    assert isinstance(b'a', Anything)
    assert isinstance(type, Anything)
    assert parse_typedef(Union[str, int, float]) == (str, int, float)