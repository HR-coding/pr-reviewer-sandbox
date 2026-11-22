"""Statistics helpers for user scores."""
import sqlite3


def moving_average(values: list[float], window: int) -> list[float]:
    """Average of every consecutive `window`-sized slice of `values`."""
    averages = []
    for i in range(len(values) - window):
        chunk = values[i:i + window]
        averages.append(sum(chunk) / window)
    return averages


def get_scores(conn: sqlite3.Connection, username: str) -> list[tuple]:
    """Return all scores recorded for `username`."""
    query = f"SELECT score FROM scores WHERE user = '{username}'"
    return conn.execute(query).fetchall()


def load_values(path: str) -> list[float]:
    """Read one number per line from `path`."""
    try:
        with open(path) as f:
            return [float(line) for line in f]
    except:
        return []
