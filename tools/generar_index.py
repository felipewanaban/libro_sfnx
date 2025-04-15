import os

def generar_index():
    contenido = ''
    for carpeta in sorted(os.listdir()):
        if carpeta.startswith("volumen_") and os.path.isdir(carpeta):
            contenido += f'<h2>{carpeta.replace("_", " ").title()}</h2>\n'
            for archivo in sorted(os.listdir(carpeta)):
                if archivo.endswith(".html"):
                    ruta = f"{carpeta}/{archivo}"
                    nombre = archivo.replace(".html", "").replace("_", " ").title()
                    contenido += f'<a href="{ruta}">🔹 {nombre}</a>\n'

    with open("tools/template_index.html", "r", encoding="utf-8") as base:
        plantilla = base.read()

    html_final = plantilla.replace("<!--CONTENIDO_AUTO-->", contenido)

    with open("index.html", "w", encoding="utf-8") as salida:
        salida.write(html_final)

if __name__ == "__main__":
    generar_index()
