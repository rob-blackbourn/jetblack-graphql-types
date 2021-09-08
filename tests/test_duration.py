"""A test for GraphQLDuration type"""

from datetime import timedelta

from jetblack_graphql_types import GraphQLDuration


def test_parse_value():
    """Parse a duration"""
    assert GraphQLDuration.parse_value(
        timedelta(seconds=1)
    ) == timedelta(seconds=1)


def test_serialize():
    """Test the serializtion of durations"""
    assert GraphQLDuration.serialize(
        timedelta(seconds=1)
    ) == timedelta(seconds=1)
    assert GraphQLDuration.serialize("PT1S") == timedelta(seconds=1)
