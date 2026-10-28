from flask import Blueprint, render_template, abort


blog_bp = Blueprint('blog', __name__, template_folder='templates')

entradas = {
    '1': {'titulo': 'Mi primera entrada en el Blog'},
    '2': {'titulo': 'Aprendiendo Flask con Blueprints'}
}

@blog_bp.route('/entrada/<id>')
def entrada(id):
    post = entradas.get(id)
    if post is None:
        abort(404)
    return render_template('blog/entrada.html', titulo=post['titulo'])