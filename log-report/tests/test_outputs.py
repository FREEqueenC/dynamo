import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), f"Expected report file at {REPORT_PATH} does not exist."
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_total_requests():
    """Verify success criterion 1: total_requests is the total number of requests in the log file (integer)."""
    data = load_report()
    assert "total_requests" in data, "Key 'total_requests' not found in report"
    assert data["total_requests"] == 6, f"Expected total_requests to be 6, got {data['total_requests']}"


def test_unique_ips():
    """Verify success criterion 2: unique_ips is the count of unique IP addresses making requests (integer)."""
    data = load_report()
    assert "unique_ips" in data, "Key 'unique_ips' not found in report"
    assert data["unique_ips"] == 3, f"Expected unique_ips to be 3, got {data['unique_ips']}"


def test_top_path():
    """Verify success criterion 3: top_path is the most frequently requested path (string)."""
    data = load_report()
    assert "top_path" in data, "Key 'top_path' not found in report"
    assert data["top_path"] == "/index.html", f"Expected top_path to be '/index.html', got {data['top_path']}"
