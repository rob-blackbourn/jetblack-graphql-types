"""Tests for GraphQLJson type"""

from pytest import raises
from graphql.error import GraphQLError

from jetblack_graphql_types import GraphQLJson


def test_parse_value():
    assert GraphQLJson.parse_value({'one': 1}) == {'one': 1}
    assert GraphQLJson.parse_value(['one', 1]) == ['one', 1]
    assert GraphQLJson.parse_value(1) == 1
    assert GraphQLJson.parse_value(1.0) == 1.0
    assert GraphQLJson.parse_value(True)
    assert not GraphQLJson.parse_value(False)
    assert GraphQLJson.parse_value(None) is None

    with raises(GraphQLError) as exc_info:
        GraphQLJson.parse_value(set())
    assert (
        str(exc_info.value) == "JSON cannot represent value: set()"
    )


def test_serialize():
    assert GraphQLJson.serialize({'one': 1}) == {'one': 1}
    assert GraphQLJson.serialize('{"one": 1}') == {'one': 1}
    assert GraphQLJson.serialize(['one', 1]) == ['one', 1]
    assert GraphQLJson.serialize('["one", 1]') == ['one', 1]
    assert GraphQLJson.serialize(1) == 1
    assert GraphQLJson.serialize("1") == 1
    assert GraphQLJson.serialize(1.0) == 1.0
    assert GraphQLJson.serialize("1.0") == 1.0
    assert GraphQLJson.serialize(True)
    assert GraphQLJson.serialize("true")
    assert not GraphQLJson.serialize(False)
    assert not GraphQLJson.serialize("false")
    assert GraphQLJson.serialize(None) is None
    assert GraphQLJson.serialize("null") is None

    with raises(GraphQLError) as exc_info:
        GraphQLJson.serialize("Hello, World!")
    assert (
        str(exc_info.value) == "JSON cannot represent value: 'Hello, World!'"
    )
