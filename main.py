from pathlib import Path
from generate_inst import generate

out_dir = Path("output")
out_dir.mkdir(exist_ok=True)

generate(str(out_dir / "instrumental.wav"))
