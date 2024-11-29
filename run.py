from app import create_app, db
from app.models import Category, Tag
import time


def initialize_database():
    """Inicializa las tablas y los datos básicos en la base de datos."""
    print("Waiting for MySQL to be ready...")
    time.sleep(10)

    with app.app_context():
        db.create_all()

        categories = ['Trabajo', 'Personal', 'Estudios', 'Salud', 'Proyectos', 'Finanzas', 'Compras', 'Viajes']
        for name in categories:
            if not Category.query.filter_by(name=name).first():
                category = Category(name=name)
                db.session.add(category)

        tags = ['Urgente', 'Importante', 'Baja Prioridad', 'Largo Plazo', 'Corto Plazo']
        for name in tags:
            if not Tag.query.filter_by(name=name).first():
                tag = Tag(name=name)
                db.session.add(tag)

        db.session.commit()
        print("Database initialized with categories and tags.")


app = create_app()

if __name__ == '__main__':
    initialize_database()
    app.run(host='0.0.0.0', port=5000, debug=True)
