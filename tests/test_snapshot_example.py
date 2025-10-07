"""
Example test demonstrating inline-snapshot usage.

This test shows how inline-snapshot works and how to update snapshots
when code changes.
"""

from inline_snapshot import snapshot


def something():
    """Calculate a value using integer division."""
    return (1548 * 18489) // 18


def test_something():
    """Test the something function with a snapshot assertion."""
    assert something() == snapshot(1590054)
