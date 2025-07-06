import os
from typing import List, Dict

def export_m3u_playlists(tracks: List[Dict], export_dir: str) -> None:
    """Generate M3U playlists organized by energy level and Camelot key."""
    os.makedirs(export_dir, exist_ok=True)
    
    # Group by energy and key
    playlists = {}
    for track in tracks:
        key = track.get("camelot", "Unknown")
        energy = track.get("energy", "Unknown")
        playlist_name = f"{key} - {energy}.m3u"
        playlists.setdefault(playlist_name, []).append(track['path'])
    
    # Write playlists
    for name, paths in playlists.items():
        with open(os.path.join(export_dir, name), "w", encoding="utf-8") as f:
            f.write("\n".join(paths))