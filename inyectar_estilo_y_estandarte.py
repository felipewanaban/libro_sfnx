from pathlib import Path

# Ruta base del proyecto
base_path = Path(__file__).resolve().parent
css_link = '<link rel="stylesheet" href="/estilo_sfnx.css">\n'
img_block = '''
<div style="text-align: center; margin-bottom: 20px;">
  <img src="/assets/img/ChatGPT Image 15 abr 2025, 02_48_10.png" alt="SFNX Estandarte" style="max-width: 250px; box-shadow: 0 0 30px #0ff; border-radius: 10px;">
</div>
'''

# Buscar todos los HTMLs en volumenes
html_files = list(base_path.glob("volumen_*/**/*.html"))

for html_file in html_files:
    content = html_file.read_text(encoding="utf-8")
    if css_link.strip() not in content:
        content = content.replace("<head>", f"<head>\n  {css_link.strip()}")
        content = content.replace("<body>", f"<body>\n{img_block.strip()}")
        html_file.write_text(content, encoding="utf-8")
