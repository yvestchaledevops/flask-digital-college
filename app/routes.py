from flask import Blueprint, jsonify,request, redirect, url_for, flash,render_template
from sqlalchemy.sql import text
from werkzeug.utils import secure_filename
from .models import RetourFormation
from . import db
import os


# Define a test blueprint or use an existing one
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
test_bp = Blueprint('test', __name__,url_prefix='/test')
main_bp = Blueprint('main', __name__)
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}


@test_bp.route('/test-db-connection')
def test_db_connection():
    try:
        # Execute a simple query to test the connection
        result = db.session.execute(text('SELECT 1')).scalar()
        return jsonify({'success': True, 'message': 'Database connection is successful!', 'result': result}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': 'Database connection failed!', 'error': str(e)}), 500

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Query all feedback from the database
    retours = RetourFormation.query.all()

    # Render the 'index.html' template in the 'templates' folder
    return render_template('index.html', retours=retours)

@main_bp.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        # Get form data
        formation = request.form['formation']
        priorite_retour = request.form['prioriteRetour']
        type_retour = request.form['typeRetour']
        date_retour = request.form['date']
        evaluation = int(request.form['rating'])
        commentaires = request.form['comments']
        consentement = 'consentement' in request.form

        # Handle file upload
        attached_file = request.files['attachedfiles']
        fichier_joint = None
        if attached_file and attached_file.filename != '':
            filename = secure_filename(attached_file.filename)
            attached_file.save(os.path.join(UPLOAD_FOLDER, filename))
            fichier_joint = filename

        # Save to database
        retour = RetourFormation(
            nom_bootcamp=formation,
            formation=formation,
            priorite_retour=priorite_retour,
            type_retour=type_retour,
            date_retour=date_retour,
            evaluation=evaluation,
            commentaires=commentaires,
            fichier_joint=fichier_joint,
            donnees_acceptees=consentement
        )
        db.session.add(retour)
        db.session.commit()
        print(f"Received form data: {request.form}")


        flash('Votre retour a été enregistré avec succès!', 'success')
        return redirect(url_for('main.index'))
    except Exception as e:
        flash(f"Erreur lors de l'enregistrement: {str(e)}", 'danger')
        return redirect(url_for('main.index'))
    
@admin_bp.route('/')
def admin_dashboard():
    # Obtenir tous les retours non supprimés
    retours = RetourFormation.query.filter_by(delete_status=False).all()
    return render_template('admin_dashboard.html', retours=retours) 

@admin_bp.route('/delete/<int:retour_id>')
def delete_retour(retour_id):
    retour = RetourFormation.query.get_or_404(retour_id)
    retour.delete_status = True  # Marquer comme supprimé
    db.session.commit()
    flash("Retour marqué comme supprimé.", "success")
    return redirect(url_for('admin.admin_dashboard'))

@admin_bp.route('/edit/<int:retour_id>', methods=['GET', 'POST'])
def edit_retour(retour_id):
    retour = RetourFormation.query.get_or_404(retour_id)

    if request.method == 'POST':
        retour.nom_bootcamp = request.form['nom_bootcamp']
        retour.formation = request.form['formation']
        retour.priorite_retour = request.form['priorite_retour']
        retour.type_retour = request.form['type_retour']
        retour.date_retour = request.form['date_retour']
        retour.evaluation = request.form['evaluation']
        retour.commentaires = request.form['commentaires']
        db.session.commit()
        flash("Retour mis à jour avec succès.", "success")
        return redirect(url_for('admin.admin_dashboard'))

    return render_template('edit_retour.html', retour=retour)