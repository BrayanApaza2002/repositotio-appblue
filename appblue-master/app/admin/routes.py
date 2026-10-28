from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__, template_folder='templates')

#  Esta ruta ahora es exactamente /panel
@admin_bp.route("/panel")
def panel():
    #  Renderiza la plantilla que creaste para el panel
    return render_template('admin/panel.html')