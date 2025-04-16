import os
from pathlib import Path

base = Path(__file__).resolve().parent

volumenes = sorted([d for d in base.iterdir() if d.is_dir() and d.name.startswith("volumen_")])
estructura = {}
for volumen in volumenes:
    capis = sorted([f for f in volumen.glob("*.html")])
    estructura[volumen.name] = capis

with open(base / "index.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>SFNX – Enciclopedia Interactiva</title>
  <link rel="stylesheet" href="/estilo_sfnx.css">
</head>
<body>
  <div style="text-align:center;margin-bottom:20px;">
    <img src="/assets/img/ChatGPT Image 15 abr 2025, 02_48_10.png" alt="SFNX Estandarte" style="max-width:240px;border-radius:10px;box-shadow:0 0 30px #0ff;">
  </div>
  <div class="wrapper">
    <h1>📚 Sistema Formal Núcleo X – Atlas Interactivo</h1>
""")
    for nombre_vol, archivos in estructura.items():
        titulo = nombre_vol.replace("_", " ").title()
        f.write(f"    <h2>{titulo}</h2>\n    <ul>\n")
        for cap in archivos:
            cap_name = cap.stem.replace("_", " ").capitalize()
            ruta = f"{nombre_vol}/{cap.name}"
            f.write(f'      <li><a href="{ruta}">{cap_name}</a></li>\n')
        f.write("    </ul>\n")
    f.write("""  </div>
</body>
</html>
""")
