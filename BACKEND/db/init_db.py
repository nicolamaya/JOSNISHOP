import sys
import os
import bcrypt # Necesario para hashear contraseñas
from sqlalchemy.exc import IntegrityError

# Agrega la raíz del proyecto al path para asegurar que las importaciones funcionen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importa el motor, la clase Base, la sesión y el modelo Usuario.
# Asegúrate de que tu __init__.py exporte SessionLocal y Usuario
from BACKEND.db import engine, Base, SessionLocal, Usuario 


def create_initial_user():
    """Inserta el usuario de prueba con ID 54 para que las pruebas unitarias funcionen."""
    
    # ⚠️ ASEGÚRATE DE USAR EL HASH CORRECTO para la verificación en tu prueba.
    # Usaremos una contraseña simple para el usuario de prueba.
    password_text = 'testpassword123' 
    password_hash = bcrypt.hashpw(password_text.encode('utf-8'), bcrypt.gensalt(rounds=12)).decode('utf-8')
    
    db = SessionLocal()
    
    try:
        existing_user = db.query(Usuario).filter(Usuario.id_usuario == 54).first()
        
        if existing_user is None:
            # Crear el objeto Usuario con el ID que la prueba espera (54)
            new_user = Usuario(
                id_usuario=54,
                nombre="UsuarioCI",
                correo="ci@test.com",
                contraseña=password_hash,
                rol_id=1,
                estado=True,
                tipo_documento='CC',
                numero_documento='999999999',
                fecha_nacimiento='2000-01-01',
                seguridad_pregunta='test_q',
                seguridad_respuesta='test_a'
            )
            db.add(new_user)
            db.commit()
            print("✅ Usuario de prueba (ID 54) insertado exitosamente.")
        else:
            print("Usuario de prueba (ID 54) ya existe.")
            
    except Exception as e:
        db.rollback()
        # Si falla por un error de programación o de BD, se mostrará aquí
        print(f"❌ Ocurrió un error al insertar el usuario: {e}")
    finally:
        db.close()


def init_db():
    print("Intentando crear todas las tablas en la BD...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas exitosamente.")
    
    # LLAMAR A LA FUNCIÓN DE INSERCIÓN
    create_initial_user()


if __name__ == '__main__':
    init_db()