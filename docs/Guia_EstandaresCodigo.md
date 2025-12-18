# Guia_EstandaresCodigo

Actividades 

Según el stack seleccionado, crear archivo Guia_EstandaresCodigo.md con: 

Reglas de nombres (variables, clases, métodos). 

Comentarios y documentación interna. 

Identación y estilo de código. 

Ejemplos aceptados y no aceptados. 

Instalar linters y formateadores: 

ESLint para JS/TS (frontend) 

Black para Python (backend) 

isort y ruff para Python (backend) 

Prettier para JS/TS (opcional, frontend) 

 

## 📦 Stack Seleccionado 

Frontend: React + TypeScript 

Backend: FastAPI + Python 

 

### 1. Reglas de Nombres 

Frontend (React/TypeScript) 

Componentes: PascalCase 

Ejemplo: InicioSesion.tsx, Navbar.tsx 

Variables y funciones: camelCase 

Ejemplo: userName, handleSubmit 

Clases CSS: kebab-case 

Ejemplo: .login-container, .main-header 

Backend (Python/FastAPI) 

Clases: PascalCase 

Ejemplo: UsuarioController, ProductoModel 

Variables y funciones: snake_case 

Ejemplo: usuario_origen, get_productos 

Archivos: snake_case 

Ejemplo: usuario_controller.py, producto_dto.py 

 

### 2. Comentarios y Documentación Interna 

Frontend 

Usa comentarios // para explicar lógica compleja. 

Documenta componentes y funciones con JSDoc:/** 
 * Componente de inicio de sesión 
 * @returns JSX.Element 
 */ 
  

Backend 

Usa docstrings para funciones y clases:def get_productos(): 
    """ 
    Retorna la lista de productos disponibles. 
    """ 
    ... 
  

Usa # para comentarios en línea. 

 

### 3. Identación y Estilo de Código 

Frontend 

Usa 2 espacios por nivel de indentación. 

Llaves abiertas en la misma línea. 

Usa prettier y eslint para formateo automático. 

Backend 

Usa 4 espacios por nivel de indentación. 

Sigue PEP8 para Python. 

Usa black, isort y ruff para formateo y linting. 

 

### 4. Ejemplos Aceptados y No Aceptados 

Frontend 

Aceptado: 

function handleLogin() { 
  // Lógica de login 
} 
  

No aceptado: 

function Handlelogin(){ 
    //logica 
} 
  

Backend 

Aceptado: 

def obtener_usuario_por_id(usuario_id: int) -> Usuario: 
    """Obtiene un usuario por su ID.""" 
    pass 
  

No aceptado: 

def ObtenerUsuarioPorID(ID): 
    pass 
  

 

### 5. Linters y Formateadores 

Frontend 

Instala ESLint:npm install eslint --save-dev 
npx eslint --init 
  

Instala Prettier (opcional):npm install prettier --save-dev 
  

Backend 

Instala Black, isort y ruff:pip install black isort ruff 
  
