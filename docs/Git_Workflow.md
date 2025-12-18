# Git Workflow

Este documento define las prácticas estándar para trabajar con Git en este proyecto, con el fin de mantener un flujo de trabajo limpio, colaborativo y eficiente.

---

**Tipos comunes:**
- `feat`: Nueva funcionalidad
- `fix`: Corrección de errores
- `docs`: Cambios en documentación
- `style`: Formato (espacios, indentación, etc.)
- `refactor`: Refactorización sin cambio de funcionalidad
- `test`: Añadir o modificar pruebas
- `chore`: Tareas menores (actualización de dependencias, etc.)

**Ejemplos:**
- `feat(inventario): agregar actualización en tiempo real`
- `fix(login): corregir validación de credenciales`
- `docs: actualizar README con instrucciones de despliegue`

---

## ✅ Convención de Commits

Utilizamos una convención basada en [Conventional Commits](https://www.conventionalcommits.org/) para mantener un historial claro y automatizar procesos como generación de changelogs.

**Formato:**


## 🔁 Frecuencia de Push/Pull

**Pull (actualizar local desde remoto):**
- Antes de comenzar a trabajar cada día
- Antes de crear una nueva rama
- Antes de hacer push, para evitar conflictos

**Push (subir cambios al remoto):**
- Al finalizar una tarea o sub-tarea significativa
- Nunca dejar cambios locales sin subir por más de 24 horas
- Siempre desde una rama distinta a `main`

---

## 🚀 Política de Pull Requests

- Todo cambio debe ser propuesto mediante un Pull Request (PR)
- Los PR deben ir desde una rama descriptiva (`feat/inventario`, `fix/login`, etc.)
- Cada PR debe incluir:
  - Descripción clara del cambio
  - Referencia al issue (si aplica)
  - Capturas o pruebas si el cambio es visual o funcional

**Revisión:**
- Al menos una aprobación de otro miembro del equipo
- No se permite hacer merge sin revisión
- Se recomienda usar `Squash and merge` para mantener el historial limpio

**Merge a `main`:**
- Solo después de pasar pruebas automáticas (CI/CD)
- Solo si el PR está aprobado
