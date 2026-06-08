from flask import render_template, request
from config import db
from models import Message, Checkin, Diario, Persona


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
            "Procure uma rede de apoio",
            "Busque atividades que tragam prazer",
            "Mantenha uma rotina saudável",
            "Evite o isolamento social",
            "Limite o consumo de notícias negativas",
            "Faça exercícios físicos regularmente",
            "Durma pelo menos 7 horas por dia",
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

            r1 = int(request.form.get("pergunta1", 0))
            r2 = int(request.form.get("pergunta2", 0))
            r3 = int(request.form.get("pergunta3", 0))
            r4 = int(request.form.get("pergunta4", 0))

            score = r1 + r2 + r3 + r4

            if score <= 2:
                resultado = """
                Você aparenta estar emocionalmente bem 😊
                Continue mantendo hábitos saudáveis e sua rede de apoio.
                """

            elif score <= 5:
                resultado = """
                Você apresenta alguns sinais de desgaste emocional 😐
                Considere conversar com familiares, amigos ou buscar apoio profissional.
                """

            else:
                resultado = """
                Atenção ao seu bem-estar emocional ❤️
                Recomendamos procurar apoio psicológico e fortalecer sua rede de apoio.
                """

        return render_template(
            "teste.html",
            resultado=resultado
        )
    
    @app.route("/personas", methods=["GET", "POST"])
    def personas():

        if request.method == "POST":
            nome = request.form["nome"]
            perfil = request.form["perfil"]
            problema = request.form["problema"]

            nova_persona = Persona(
            nome=nome,
            perfil=perfil,
            problema=problema
            )

            db.session.add(nova_persona)
            db.session.commit()

        todas = Persona.query.all()

        return render_template(
            "personas.html",
            personas=todas
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