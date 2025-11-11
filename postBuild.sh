#!/bin/bash

# Disable Jupyter token authentication
mkdir -p ~/.jupyter
cat >> ~/.jupyter/jupyter_notebook_config.py << EOF
c.NotebookApp.token = ''
c.NotebookApp.password = ''
c.NotebookApp.allow_origin = '*'
EOF