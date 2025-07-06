import eyed3
from typing import Dict

def tag_file(filepath: str, metadata: Dict) -> bool:
    """Comprehensive audio tagging with energy/mood support."""
    try:
        audio = eyed3.load(filepath)
        if not audio or not audio.tag:
            audio.initTag()
        
        # Required Tags
        audio.tag.artist = metadata.get("artist", "Unknown Artist")
        audio.tag.title = metadata.get("title", "Unknown Title")
        
        # Standard ID3 Frames
        if (bpm := metadata.get("bpm")):
            audio.tag.bpm = int(bpm)
        
        if (key := metadata.get("key")):
            audio.tag.key = key
            audio.tag.user_text_frames.set("initialkey", key)
        
        # Custom Fields
        for field in ["energy", "mood"]:
            if value := metadata.get(field):
                audio.tag.user_text_frames.set(field, str(value))
        
        audio.tag.save()
        return True
    
    except Exception as e:
        print(f"⚠️ Tagging error in {filepath}: {str(e)}")
        return False