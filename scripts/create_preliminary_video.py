from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import math


ROOT = Path(__file__).resolve().parents[1]
EPISODE = ROOT / "Episodes" / "01 - El caminante del cementerio Central"
ART = EPISODE / "03 Arte" / "Generado"
OUT_DIR = EPISODE / "05 Video" / "preliminar"
EXPORTS = EPISODE / "06 Exportaciones"

W, H = 360, 640
FPS = 6


SCENES = [
    {
        "file": "escena-01-cementerio-central-noche.png",
        "seconds": 7,
        "subtitle": "Dicen que en el Cementerio Central de Cali hay una tumba que no siempre esta ahi.",
        "zoom": (1.0, 1.08),
    },
    {
        "file": "escena-02-el-caminante-arcos.png",
        "seconds": 8,
        "subtitle": "Los martes, un hombre vestido de negro cruza la entrada sin saludar a nadie.",
        "zoom": (1.02, 1.10),
    },
    {
        "file": "escena-04-tumba-imposible-3pm.png",
        "seconds": 8,
        "subtitle": "La tumba que busca solo aparece los miercoles, exactamente a las tres de la tarde.",
        "zoom": (1.0, 1.12),
    },
    {
        "file": "escena-06-lamento-tumba.png",
        "seconds": 9,
        "subtitle": "El caminante se arrodilla frente a esa piedra y llora hasta que cae la tarde.",
        "zoom": (1.01, 1.09),
    },
    {
        "file": "escena-08-casa-madrugada.png",
        "seconds": 8,
        "subtitle": "El verdadero peligro no es verlo. Es escucharlo el domingo en la madrugada.",
        "zoom": (1.0, 1.08),
    },
    {
        "file": "escena-09-sombra-pasillo.png",
        "seconds": 8,
        "subtitle": "Quienes oyen sus lamentos despiertan sabiendo que algo los esta siguiendo.",
        "zoom": (1.0, 1.10),
    },
    {
        "file": "escena-11-plano-final-tumba.png",
        "seconds": 9,
        "subtitle": "\"Todavia no es tu turno.\" Y esos viven. De los otros... nadie ha podido contar.",
        "zoom": (1.0, 1.11),
    },
]


def font(size: int):
    candidates = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/calibri.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


FONT = font(28)
SMALL = font(18)


def cover_crop(img: Image.Image, scale: float) -> Image.Image:
    target_ratio = W / H
    src_ratio = img.width / img.height
    if src_ratio > target_ratio:
        new_h = H
        new_w = int(H * src_ratio)
    else:
        new_w = W
        new_h = int(W / src_ratio)
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    zw, zh = int(W * scale), int(H * scale)
    zoomed = resized.resize((max(zw, W), max(zh, H)), Image.Resampling.LANCZOS)
    left = (zoomed.width - W) // 2
    top = (zoomed.height - H) // 2
    return zoomed.crop((left, top, left + W, top + H))


def wrap_text(draw, text, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), test, font=FONT)[2] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def make_vignette() -> Image.Image:
    overlay = Image.new("L", (W, H), 0)
    px = overlay.load()
    cx, cy = W / 2, H / 2
    max_d = math.sqrt(cx * cx + cy * cy)
    for y in range(H):
        for x in range(W):
            d = math.sqrt((x - cx) ** 2 + (y - cy) ** 2) / max_d
            px[x, y] = int(max(0, min(180, (d - 0.35) * 260)))
    return overlay


VIGNETTE = make_vignette()


def add_vignette(frame: Image.Image) -> Image.Image:
    black = Image.new("RGB", (W, H), "black")
    return Image.composite(black, frame, VIGNETTE)


def add_subtitle(frame: Image.Image, text: str, scene_no: int) -> Image.Image:
    draw = ImageDraw.Draw(frame, "RGBA")
    lines = wrap_text(draw, text, W - 80)
    line_h = 36
    box_h = line_h * len(lines) + 42
    y0 = H - box_h - 46
    draw.rounded_rectangle((28, y0, W - 28, H - 34), radius=18, fill=(0, 0, 0, 145))
    y = y0 + 20
    for line in lines:
        tw = draw.textbbox((0, 0), line, font=FONT)[2]
        draw.text(((W - tw) / 2, y), line, font=FONT, fill=(245, 241, 226, 255))
        y += line_h
    label = f"LEYENDAS DE LA SULTANA  |  ESCENA {scene_no:02d}"
    draw.text((28, 24), label, font=SMALL, fill=(235, 220, 180, 210))
    return frame


def fade_factor(i, total):
    fade_frames = max(4, int(FPS * 0.75))
    if i < fade_frames:
        return i / fade_frames
    if i > total - fade_frames:
        return max(0, (total - i) / fade_frames)
    return 1


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    EXPORTS.mkdir(parents=True, exist_ok=True)
    frames = []
    for idx, scene in enumerate(SCENES, start=1):
        img = Image.open(ART / scene["file"]).convert("RGB")
        count = scene["seconds"] * FPS
        z0, z1 = scene["zoom"]
        for i in range(count):
            t = i / max(1, count - 1)
            scale = z0 + (z1 - z0) * t
            frame = cover_crop(img, scale)
            frame = ImageEnhance.Contrast(frame).enhance(1.08)
            frame = ImageEnhance.Color(frame).enhance(0.92)
            frame = add_vignette(frame)
            frame = add_subtitle(frame, scene["subtitle"], idx)
            alpha = fade_factor(i, count)
            if alpha < 1:
                black = Image.new("RGB", (W, H), "black")
                frame = Image.blend(black, frame, alpha)
            frames.append(frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))

    out = EXPORTS / "01-el-caminante-video-preliminar.gif"
    frames[0].save(
        out,
        save_all=True,
        append_images=frames[1:],
        duration=int(1000 / FPS),
        loop=0,
        optimize=True,
    )

    contact = OUT_DIR / "timeline-preliminar.txt"
    elapsed = 0
    lines = ["Timeline preliminar - 01 El caminante del Cementerio Central", ""]
    for idx, scene in enumerate(SCENES, start=1):
        start = elapsed
        elapsed += scene["seconds"]
        lines.append(f"Escena {idx:02d}: {start:02d}s-{elapsed:02d}s | {scene['file']}")
        lines.append(f"Texto: {scene['subtitle']}")
        lines.append("")
    contact.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
