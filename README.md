appblue-master/
│
├── app/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── routes.py
│   │
│   ├── admin/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       └── admin/
│   │           └── panel.html
│   │
│   ├── auth/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       └── login.html
│   │
│   ├── blog/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       └── blog/
│   │           └── entrada.html
│   │
│   ├── productos/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       └── index.html
│   │
│   └── templates/
│       └── base.html
│
├── usuarios/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── lista.html
│
├── venv/
├── .gitignore
├── requirements.txt
├── routes.py
└── run.py



---

##  Puntos clave de tu estructura:
-  `app/templates/base.html` → Plantilla base compartida
-  `app/admin/templates/admin/panel.html` → Panel de administración
-  `app/blog/templates/blog/entrada.html` → Entrada dinámica del blog
-  Carpetas adicionales: `auth`, `productos`, `usuarios` → listas para ampliar el proyecto
-  `venv/` → Entorno virtual (no se sube a GitHub por `.gitignore`)

---
