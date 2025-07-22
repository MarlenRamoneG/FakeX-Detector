# FakeX-Detector

Este repositorio contiene un ejemplo de aplicaci\u00f3n de prevenci\u00f3n de riesgos laborales.

La carpeta incluye un peque\u00f1o servidor web en `app.py` que permite al operario rellenar un checklist de EPIs, escribir una descripci\u00f3n de riesgos y seleccionar el tipo de accidente. Al enviar el formulario, se genera un PDF con la informaci\u00f3n recopilada y se intenta enviar por correo electr\u00f3nico a `marlenwow@icloud.com` (es necesario tener un servidor SMTP en `localhost`).

Para ejecutar la aplicaci\u00f3n en macOS (o cualquier sistema que disponga de Python), instale las dependencias y ejecute `app.py`:

```bash
pip install -r requirements.txt
python app.py
```

El servidor quedar\u00e1 accesible en `http://localhost:5000`. Puede abrir esta direcci\u00f3n tanto desde el Mac como desde un iPhone conectado a la misma red.

La funcionalidad de plan de emergencia se basa en un listado sencillo que asigna una salida de evacuaci\u00f3n seg\u00fan el accidente seleccionado.
