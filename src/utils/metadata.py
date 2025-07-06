from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TKEY, TBPM
import os
from typing import Dict

def tag_mp3(file_path: str, metadata: Dict[str, str]) -> None:
    """Write ID3 tags with BPM/key support."""
    try:
        audio = EasyID3(file_path) if EasyID3(file_path) else ID3(file_path)
        
        # Standard tags
        audio["artist"] = metadata.get("artist", "")
        audio["title"] = metadata.get("title", "")
        
        # BPM (converted to integer)
        if bpm := metadata.get("bpm"):
            audio["bpm"] = str(int(bpm))
            audio.add(TBPM(encoding=3, text=str(int(bpm))))
        
        # Key (Camelot or musical)
        if key := metadata.get("key"):
            audio["initialkey"] = key
            audio.add(TKEY(encoding=3, text=key))
        
        audio.save()
    except Exception as e:
        raise RuntimeError(f"Tagging failed for {os.path.basename(file_path)}: {e}")