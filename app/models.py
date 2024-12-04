from . import db
from datetime import datetime

class RetourFormation(db.Model):
    __tablename__ = 'retour_formation'

    id = db.Column(db.Integer, primary_key=True)  # ID unique
    nom_bootcamp = db.Column(db.String(150), nullable=False)  # Nom du bootcamp
    formation = db.Column(db.String(150), nullable=False)  # Nom de la formation
    priorite_retour = db.Column(db.String(50), nullable=False)  # Priorité de retour (e.g., Faible)
    type_retour = db.Column(db.String(150), nullable=False)  # Type de retour
    date_retour = db.Column(db.Date, nullable=False, default=datetime.utcnow)  # Date du retour
    evaluation = db.Column(db.Integer, nullable=False)  # Évaluation
    commentaires = db.Column(db.Text, nullable=True)  # Commentaires
    fichier_joint = db.Column(db.String(250), nullable=True)  # Chemin vers les fichiers joints
    donnees_acceptees = db.Column(db.Boolean, nullable=False, default=False)  # Consentement
    delete_status = db.Column(db.Boolean, nullable=False,default=False)
    def __repr__(self):
        return f"<RetourFormation {self.nom_bootcamp}, {self.formation}>"
