# FakeX-Detector

Este proyecto incluye un script en Python para detectar posibles cuentas falsas en la plataforma **X**. El detector se basa en heurísticas simples como la cantidad de seguidores, la imagen de perfil y la actividad reciente.

## Uso rápido

1. Coloca los datos del usuario en un archivo JSON. Se incluye un ejemplo para `@MantecaAlba84024` en `sample_data/MantecaAlba84024.json`.
2. Ejecuta el detector indicando la ruta del archivo de datos:

```bash
python fake_x_detector.py sample_data/MantecaAlba84024.json
```

El script imprime un puntaje y las razones que llevaron a clasificar la cuenta como falsa o legítima.

## Formato del archivo JSON

El archivo debe contener campos como:

```json
{
  "username": "nombreDeUsuario",
  "default_image": true,
  "followers": 100,
  "following": 50,
  "posts": 10,
  "last_post_days_ago": 30
}
```

Puedes modificar los valores según la información que tengas del usuario para analizar su perfil.
