import pytest

from src.orchestrator import _current_report_date


def test_report_date_uses_valid_override(monkeypatch):
    monkeypatch.setenv("HORIZON_REPORT_DATE", "2026-08-06")

    assert _current_report_date() == "2026-08-06"


@pytest.mark.parametrize(
    "value",
    ["2026-8-6", "06-08-2026", "2026-02-30", "../../outside"],
)
def test_report_date_rejects_invalid_override(monkeypatch, value):
    monkeypatch.setenv("HORIZON_REPORT_DATE", value)

    with pytest.raises(ValueError, match="YYYY-MM-DD"):
        _current_report_date()
