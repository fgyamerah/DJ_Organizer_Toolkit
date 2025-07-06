import os
import shutil
import re
from typing import Dict

def clean_string(s: str) -> str:
    """Remove invalid filesystem characters."""
    return re.sub(r'[\\/*?:"<>|]', "", s).strip()

def copy_file(src: str, dst: str) -> None:
    """Copy files with parent directory creation."""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)

def organize_file_by_artist(
    src_path: str,
    dest_root: str,
    metadata: Dict[str, str]
) -> str:
    """Organize files into artist subfolders."""
    artist = clean_string(metadata.get("artist", "Unknown Artist"))
    title = clean_string(metadata.get("title", os.path.splitext(os.path.basename(src_path))[0]))
    
    dest_path = os.path.join(dest_root, "Artists", artist, f"{title}.mp3")
    copy_file(src_path, dest_path)
    
    return dest_path