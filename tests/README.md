# Tests

Before running any tests, make sure you have `uv` installed (and ideally run `make sync` after).

## Running tests

```
make tests
```

## Snapshots

We use [inline-snapshots](https://15r10nk.github.io/inline-snapshot/latest/) for some tests. If your code adds new snapshot tests or breaks existing ones, you can fix/create them. After fixing/creating snapshots, run `make tests` again to verify the tests pass.

### How snapshots work

Snapshot tests capture the output of your code at a specific point in time. When you run the tests, the actual output is compared against the saved snapshot. If they don't match, the test fails.

**Example scenario:** Your tests will break if you change your code. Maybe that is correct and you should fix your code, or your code is correct and you want to update your test results.

For example, if you have this code:

```python
from inline_snapshot import snapshot

def something():
    return (1548 * 18489) // 18

def test_something():
    assert something() == snapshot(1590054)
```

And you change the calculation by adding `// 18`:

```python
def something():
    return (1548 * 18489) // 18  # changed code
```

The test will fail because the output changed. If the new output is correct, update the snapshot using `make snapshots-fix`.

### Fixing snapshots

```
make snapshots-fix
```

### Creating snapshots

```
make snapshots-update
```
