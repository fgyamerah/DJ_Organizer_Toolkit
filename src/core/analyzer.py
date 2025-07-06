import librosa
import numpy as np
from typing import Dict

CAMELOT_WHEEL = {
    'C': '8B', 'C#': '3B', 'D': '10B', 'D#': '5B', 'E': '12B',
    'F': '7B', 'F#': '2B', 'G': '9B', 'G#': '4B', 'A': '11B', 'A#': '6B', 'B': '1B',
    'Cm': '5A', 'C#m': '12A', 'Dm': '7A', 'D#m': '2A', 'Em': '9A',
    'Fm': '4A', 'F#m': '11A', 'Gm': '6A', 'G#m': '1A', 'Am': '8A', 'A#m': '3A', 'Bm': '10A'
}

def analyze_track(filepath: str) -> Dict[str, str]:
    """Extract BPM, key, energy, and mood from audio."""
    y, sr = librosa.load(filepath, duration=90.0)
    
    # BPM Detection
    tempo = float(librosa.beat.tempo(y=y, sr=sr)[0])
    
    # Key Detection
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    key_idx = np.argmax(np.mean(chroma, axis=1))
    keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    key = keys[key_idx]
    
    # Energy/Mood
    brightness = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)) / sr
    energy = "High" if tempo >= 128 and brightness >= 0.5 else "Low" if tempo < 100 else "Medium"
    
    return {
        "bpm": round(tempo),
        "key": key,
        "camelot": CAMELOT_WHEEL.get(key, "Unknown"),
        "energy": energy,
        "mood": "Uplifting" if not key.endswith("m") else "Dark"
    }