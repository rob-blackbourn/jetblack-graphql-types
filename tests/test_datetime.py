"""A test for GraphQLDuration type"""

from datetime import datetime, timezone

from jetblack_iso8601 import datetime_to_iso8601

from jetblack_graphql_types import GraphQLDateTime


def test_parse_value():
    """Parse a datetime"""
    timestamp = datetime(2000, 1, 31, 12, 15, 32).astimezone(timezone.utc)
    assert GraphQLDateTime.parse_value(timestamp) == timestamp


def test_serialize():
    """Test the serializtion of datetimes"""
    timestamp = datetime(2000, 1, 31, 12, 15, 32).astimezone(timezone.utc)
    assert GraphQLDateTime.serialize(timestamp) == timestamp
    text = datetime_to_iso8601(timestamp)
    assert GraphQLDateTime.serialize(text) == timestamp
