plantilla_html = '''
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>SFNX – Enciclopedia Interactiva</title>
  <style>
    body {{
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 2em;
      background: radial-gradient(ellipse at center, #111 0%, #000 100%);
      color: #e0e0ff;
      background-image: url('https://raw.githubusercontent.com/felipewanaban/libro_sfnx/main/assets/img/stars_bg.jpg');
      background-size: cover;
      background-attachment: fixed;
    }}
    h1 {{
      color: #a7f;
      text-shadow: 0 0 12px #6cf;
      text-align: center;
    }}
    h2 {{
      color: #fa7;
      margin-top: 40px;
      border-bottom: 1px solid #555;
    }}
    a {{
      color: #9cf;
      display: block;
      margin: 10px 0;
      font-weight: bold;
      text-decoration: none;
      font-size: 1.2em;
      transition: 0.3s;
    }}
    a:hover {{
      color: #fff;
      text-shadow: 0 0 8px #0ff;
    }}
    .wrapper {{
      background-color: rgba(0,0,0,0.6);
      padding: 2em;
      border-radius: 12px;
      max-width: 800px;
      margin: auto;
      box-shadow: 0 0 20px #000;
    }}
  </style>
</head>
<body>
  <div class="wrapper">
    <h1>📚 Sistema Formal Núcleo X – Atlas Interactivo</h1>
    <!--CONTENIDO_AUTO-->
  </div>
</body>
</html>
'''
