from flask import Flask, render_template_string, request, send_file
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import io
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

CHECK_ITEMS = ['Casco', 'Botas', 'Gafas', 'Guantes', 'Ropa de trabajo',
               'Arnes', 'Media mascara con filtros de gases',
               'Filtros de particulas o vapores']

EMERGENCY_EXITS = {
    'Incendio': 'Salida Norte',
    'Derrumbe': 'Salida Sur',
    'Quimicos': 'Salida Este'
}

HTML_FORM = '''
<!doctype html>
<title>Checklist de EPIs</title>
<h1>Checklist de EPIs</h1>
<form method="post" action="/submit">
  {% for item in items %}
    <label><input type="checkbox" name="epi" value="{{item}}"> {{item}}</label><br>
  {% endfor %}
  <h2>Descripcion de riesgos</h2>
  <textarea name="riesgos" rows="4" cols="50"></textarea><br>
  <h2>Tipo de accidente</h2>
  <select name="accidente">
    {% for key in exits.keys() %}
      <option value="{{key}}">{{key}}</option>
    {% endfor %}
  </select><br><br>
  <input type="submit" value="Enviar">
</form>
{% if exit %}
<h2>Salida recomendada: {{exit}}</h2>
{% endif %}
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_FORM, items=CHECK_ITEMS, exits=EMERGENCY_EXITS, exit=None)

@app.route('/submit', methods=['POST'])
def submit():
    selected = request.form.getlist('epi')
    riesgos = request.form.get('riesgos', '')
    accidente = request.form.get('accidente', '')
    salida = EMERGENCY_EXITS.get(accidente, 'Consultar plan de emergencia')

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=LETTER)
    p.drawString(100, 750, "Checklist de EPIs")
    y = 730
    for item in selected:
        p.drawString(100, y, f"- {item}")
        y -= 15
    p.drawString(100, y - 10, f"Riesgos: {riesgos}")
    p.drawString(100, y - 30, f"Accidente: {accidente}")
    p.drawString(100, y - 50, f"Salida recomendada: {salida}")
    p.showPage()
    p.save()
    buffer.seek(0)

    pdf_data = buffer.getvalue()
    send_email(pdf_data)

    return render_template_string(HTML_FORM, items=CHECK_ITEMS,
                                  exits=EMERGENCY_EXITS, exit=salida)

def send_email(pdf_bytes):
    msg = EmailMessage()
    msg['Subject'] = 'Reporte de EPIs'
    msg['From'] = 'noreply@example.com'
    msg['To'] = 'marlenwow@icloud.com'
    msg.set_content('Se adjunta reporte en PDF.')
    msg.add_attachment(pdf_bytes, maintype='application', subtype='pdf', filename='reporte.pdf')

    try:
        with smtplib.SMTP('localhost') as s:
            s.send_message(msg)
    except Exception as e:
        print('Error enviando correo:', e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
