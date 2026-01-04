import shutil
import sys

def ensure_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print(
            "\n❌ FFmpeg not found.\n\n"
            "RTMPS requires FFmpeg to stream audio.\n\n"
            "Install FFmpeg first:\n\n"
            "• Ubuntu / Debian:\n"
            "  sudo apt install ffmpeg\n\n"
            "• Termux:\n"
            "  pkg install ffmpeg\n\n"
            "• macOS (Homebrew):\n"
            "  brew install ffmpeg\n\n"
            "• Windows:\n"
            "  https://ffmpeg.org/download.html\n"
        )
        sys.exit(1)
