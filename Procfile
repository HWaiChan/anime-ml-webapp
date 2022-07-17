web: gunicorn --bind 0.0.0.0:$PORT app:app
release: dvc config core.no_scm true && dvc pull && rm -r .dvc .apt/usr/lib/dvc
