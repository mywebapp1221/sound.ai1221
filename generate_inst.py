import numpy as np
import soundfile as sf

def generate(output_path: str):
    sr = 48000
    bpm = 92
    bars = 8
    beats_per_bar = 4
    sec_per_beat = 60.0 / bpm
    total_sec = bars * beats_per_bar * sec_per_beat

    t = np.linspace(0, total_sec, int(sr * total_sec), endpoint=False)

    # 超シンプル：パッド + ベース（メロディ無し）
    pad = 0.18 * np.sin(2*np.pi*220*t) + 0.12 * np.sin(2*np.pi*277.18*t)  # A + C#
    bass = 0.16 * np.sin(2*np.pi*110*t)

    # ほんの少し揺らして“広がり感”を作る
    lfo = 0.5 + 0.5*np.sin(2*np.pi*0.25*t)
    audio = (pad * (0.7 + 0.3*lfo) + bass)

    # クリップ防止（安全に正規化）
    peak = np.max(np.abs(audio)) + 1e-9
    audio = audio / peak * 0.9  # -1dBFSより低め

    # ステレオ化（左右ほんの少し差）
    left = audio * 0.98
    right = audio * 1.02
    stereo = np.stack([left, right], axis=1).astype(np.float32)

    sf.write(output_path, stereo, sr)
    print(f"✅ wrote: {output_path}  (sr={sr})")
