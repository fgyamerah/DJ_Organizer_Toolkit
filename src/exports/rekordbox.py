import os
import xml.etree.ElementTree as ET
from typing import List, Dict

def export_rekordbox_xml(tracks: List[Dict], output_path: str) -> None:
    """Generate Rekordbox-compatible XML with proper URL encoding."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    root = ET.Element("DJ_PLAYLISTS", Version="1.0.0")
    collection = ET.SubElement(root, "COLLECTION", Entries=str(len(tracks)))
    
    for idx, track in enumerate(tracks, 1):
        location = _encode_location(track['path'])
        ET.SubElement(
            collection, "TRACK",
            TrackID=str(idx),
            Name=track.get("title", ""),
            Artist=track.get("artist", ""),
            BPM=str(track.get("bpm", "")),
            Key=track.get("camelot", ""),
            Location=location
        )
    
    ET.ElementTree(root).write(output_path, encoding="utf-8", xml_declaration=True)

def _encode_location(path: str) -> str:
    """Convert Windows paths to Rekordbox URL format."""
    return "file://localhost/" + path.replace("\\", "/").replace(":", "%3A").replace(" ", "%20")