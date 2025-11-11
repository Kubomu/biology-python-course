# Jupyter Notebook Configuration for Binder
# Disables token authentication for educational use

c = get_config()

# Disable token authentication
c.NotebookApp.token = ''
c.NotebookApp.password = ''

# Allow access from any IP (needed for Binder)
c.NotebookApp.allow_origin = '*'

# Disable authentication entirely
c.NotebookApp.disable_check_xsrf = True

# Open browser automatically
c.NotebookApp.open_browser = True