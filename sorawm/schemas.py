from enum import Enum


class CleanerType(str, Enum):
    LAMA = "lama"
    E2FGVI_HQ = "e2fgvi_hq"
    OVERLAY = "overlay"  # Overlay a custom image on top of the watermark
