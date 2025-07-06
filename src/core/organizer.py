import os
import sys
import json
from src.core.analyzer import analyze_track
from src.utils.file_io import organize_file_by_artist
from src.utils.metadata import tag_mp3
from src.exports.rekordbox import export_rekordbox_xml
from src.exports.m3u import export_m3u_playlists

def load_config() -> dict:
    """Load config from JSON file."""
    config_path = os.path.join(os.path.dirname(__file__), "../../config/config.json")
    with open(config_path) as f:
        return json.load(f)

def process_tracks(source: str, dest: str) -> list:
    """Main processing pipeline."""
    tracks = []
    for filename in os.listdir(source):
        if not filename.lower().endswith(".mp3"):
            continue
        
        src_path = os.path.join(source, filename)
        try:
            metadata = analyze_track(src_path)
            dest_path = organize_file_by_artist(src_path, dest, metadata)
            tag_mp3(dest_path, metadata)
            tracks.append({
                "path": dest_path,
                **metadata
            })
        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")
    return tracks

def main():
    config = load_config()
    source = sys.argv[1] if len(sys.argv) > 1 else config["source_folder"]
    dest = sys.argv[2] if len(sys.argv) > 2 else config["destination_folder"]
    
    tracks = process_tracks(source, dest)
    export_rekordbox_xml(tracks, os.path.join(dest, "_REKORDBOX_XML_EXPORTS/rekordbox.xml"))
    export_m3u_playlists(tracks, os.path.join(dest, "_PLAYLISTS_M3U_EXPORT"))

if __name__ == "__main__":
    main()