from flask import render_template, request
from config import db
from models import Message, Checkin, Diario


def init_routes(app):

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/dashboard")
    def dashboard():

        total_mensagens = Message.query.count()

        total_checkins = Checkin.query.count()

        dicas = [
            "Pratique respiração profunda",
            "Faça pausas durante os estudos",
            "Durma pelo menos 7 horas",
            "Converse com alguém de confiança"
        ]

        return render_template(
            "dashboard.html",
            total=total_mensagens,
            checkins=total_checkins,
            dicas=dicas
        )

    @app.route("/teste", methods=["GET", "POST"])
    def teste():

        resultado = None

        if request.method == "POST":

            r1 = int(request.form.get("resposta1", 0))
            r2 = int(request.form.get("resposta2", 0))
            r3 = int(request.form.get("resposta3", 0))

            score = r1 + r2 + r3

            if score <= 2:
                resultado = """
                Você aparenta estar emocionalmente bem 😊
                Continue cuidando da sua saúde mental.
                """

            elif score <= 4:
                resultado = """
                Você demonstra alguns sinais de estresse 😐
                Procure reservar momentos para descanso e lazer.
                """

            else:
                resultado = """
                Atenção ao seu bem-estar emocional ❤️
                Considere buscar apoio emocional e conversar com pessoas de confiança.
                """

        return render_template(
            "teste.html",
            resultado=resultado
        )

    @app.route("/comunidade", methods=["GET", "POST"])
    def comunidade():

        if request.method == "POST":

            texto = request.form["mensagem"]

            if texto != "":

                msg = Message(texto=texto)

                db.session.add(msg)
                db.session.commit()

        mensagens = Message.query.all()

        return render_template(
            "comunidade.html",
            mensagens=mensagens
        )

    @app.route("/checkin", methods=["GET", "POST"])
    def checkin():

        if request.method == "POST":

            humor = request.form["humor"]

            novo_checkin = Checkin(humor=humor)

            db.session.add(novo_checkin)

            db.session.commit()

        historico = Checkin.query.all()

        return render_template(
            "checkin.html",
            historico=historico
        )
    
    @app.route("/diario", methods=["GET", "POST"])
    def diario():

        if request.method == "POST":

            texto = request.form["texto"]

            if texto != "":
                novo = Diario(texto=texto)

                db.session.add(novo)
                db.session.commit()

        registros = Diario.query.all()

        return render_template(
            "diario.html",
             registros=registros
    )