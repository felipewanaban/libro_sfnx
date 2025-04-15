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

# Escribir index.html con estilo cósmico universal
with open(base / "index.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>SFNX – Enciclopedia Interactiva</title>
  <style>
    body {
      margin: 0;
      padding: 2em;
      font-family: 'Segoe UI', sans-serif;
      background: url('https://raw.githubusercontent.com/felipewanaban/libro_sfnx/main/assets/img/stars_bg.jpg') no-repeat center center fixed;
      background-size: cover;
      color: #00ffff;
    }
    h1 {
      text-align: center;
      color: #66ccff;
      text-shadow: 0 0 18px #66ccff;
      font-size: 2em;
    }
    h2 {
      color: #ffa77b;
      margin-top: 40px;
      border-bottom: 1px solid #777;
      font-size: 1.4em;
    }
    a {
      color: #00ffff;
      display: block;
      margin: 8px 0;
      font-weight: bold;
      font-size: 1.2em;
      text-decoration: none;
      transition: 0.3s;
    }
    a:hover {
      color: #ffffff;
      text-shadow: 0 0 12px #00ffff;
    }
    .wrapper {
      background-color: rgba(0, 0, 0, 0.7);
      padding: 2em;
      border-radius: 18px;
      max-width: 850px;
      margin: auto;
      box-shadow: 0 0 40px #000;
    }
  </style>
</head>
<body>
  <div class="wrapper">
    <h1>📘 Sistema Formal Núcleo X – SFNX</h1>
""")

    # Agregar capítulos por volumen
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
</html>
""")
