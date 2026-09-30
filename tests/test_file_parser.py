from core.file_parser import chunk_text


def test_short_text_returns_one_chunk():
    text = "This is a short sentence."
    result = chunk_text(text, max_chars=1000)
    assert len(result) == 1
    assert result[0] == text


def test_long_text_splits_into_multiple_chunks():
    text = "\n".join([f"This is line number {i}." for i in range(50)])
    result = chunk_text(text, max_chars=200)
    assert len(result) > 1


def test_every_chunk_respects_max_chars():
    text = "\n".join([f"This is line number {i}." for i in range(50)])
    max_chars = 200
    result = chunk_text(text, max_chars=max_chars)
    for chunk in result:
        assert len(chunk) <= max_chars   # <-- changed on purpose, too strict


def test_no_text_is_lost_between_chunks():
    text = "\n".join([f"Line {i}" for i in range(20)])
    result = chunk_text(text, max_chars=50)
    combined = "\n".join(result)
    for i in range(20):
        assert f"Line {i}" in combined