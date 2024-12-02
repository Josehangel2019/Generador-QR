from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    print("Página cargada")  # Confirmar que se entra a esta función
    qr_image = None
    if request.method == "POST":
        texto = request.form.get("texto")
        if texto:
            img = qrcode.make(texto)
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            qr_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return render_template("index.html", qr_image=qr_image)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

