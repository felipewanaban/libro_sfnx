import os
from pathlib import Path

# Ruta base del proyecto (raíz del repo)
base = Path(__file__).resolve().parent.parent

# Volúmenes (subcarpetas dentro del repo)
volumenes = sorted([d for d in base.iterdir() if d.is_dir() and d.name.startswith("volumen_")])

# Diccionario por volumen
estructura = {}

for volumen in volumenes:
    capis = sorted([f for f in volumen.glob("*.html")])
    estructura[volumen.name] = capis

# Estructura visual y cósmica
with open(base / "index.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>SFNX – Enciclopedia Interactiva</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 2em;
      background: radial-gradient(ellipse at center, #111 0%, #000 100%);
      color: #e0e0ff;
      background-image: url('https://raw.githubusercontent.com/felipewanaban/libro_sfnx/main/assets/img/stars_bg.jpg');
      background-size: cover;
      background-attachment: fixed;
    }
    h1 {
      color: #6cf;
      text-shadow: 0 0 10px #6cf;
    }
    h2 {
      color: #fa7;
      margin-top: 40px;
      border-bottom: 1px solid #555;
    }
    a {
      color: #0ff;
      display: block;
      margin: 8px 0;
      font-weight: bold;
      text-decoration: none;
      transition: 0.3s;
    }
    a:hover {
      color: #fff;
      text-shadow: 0 0 10px #0ff;
    }
    .wrapper {
      background-color: rgba(0,0,0,0.6);
      padding: 2em;
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <div class="wrapper">
    <h1>📚 Sistema Formal Núcleo X – SFNX</h1>
""")

    for nombre_vol, archivos in estructura.items():
        titulo = nombre_vol.replace("_", " ").title()
        f.write(f"    <h2>{titulo}</h2>\n    <ul>\n")
        for cap in archivos:
            cap_name = cap.stem.replace("_", " ").capitalize()
            ruta = f"{nombre_vol}/{cap.name}"
            f.write(f'      <li><a href="{ruta}">{cap_name}</a></li>\n')
        f.write("    </ul>\n")

    f.write("""
  </div>
</body>
</html>""")
