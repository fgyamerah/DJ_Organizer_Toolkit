import pytest
from src.core.analyzer import analyze_track
from pathlib import Path

SAMPLE_MP3 = Path(__file__).parent / "test_data" / "test.mp3"

def test_bpm_detection():
    result = analyze_track(SAMPLE_MP3)
    assert 100 <= result["bpm"] <= 200

def test_key_detection():
    result = analyze_track(SAMPLE_MP3)
    assert result["key"] in ["C", "C#", "D", ..., "B"]  # Complete key list