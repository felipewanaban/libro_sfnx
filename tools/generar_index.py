import os

def generar_index():
    html = ['<!DOCTYPE html>',
            '<html lang="es">',
            '<head>',
            '<meta charset="UTF-8">',
            '<title>SFNX – Enciclopedia Interactiva</title>',
            '<style>',
            'body { font-family: sans-serif; background: #111; color: #eee; padding: 40px; }',
            'h1 { color: #66f; }',
            'h2 { color: #f66; margin-top: 40px; }',
            'a { color: #0ff; display: block; margin: 5px 0; }',
            '</style>',
            '</head><body>',
            '<h1>📘 Sistema Formal Núcleo X – SFNX</h1>']

    for carpeta in sorted(os.listdir()):
        if carpeta.startswith("volumen_") and os.path.isdir(carpeta):
            html.append(f'<h2>{carpeta.replace("_", " ").title()}</h2>')
            for archivo in sorted(os.listdir(carpeta)):
                if archivo.endswith(".html"):
                    ruta = f"{carpeta}/{archivo}"
                    nombre = archivo.replace(".html", "").replace("_", " ").title()
                    html.append(f'<a href="{ruta}">🔹 {nombre}</a>')

    html.append('</body></html>')

    with open("index.html", "w", encoding="utf-8") as f:
        f.write("\n".join(html))

if __name__ == "__main__":
    generar_index()
