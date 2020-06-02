# Configuration file for jupyter-notebook.

## Whether to allow the user to run the notebook as root.
c.NotebookApp.allow_root = True

## Override URL shown to users.
#
#  Replace actual URL, including protocol, address, port and base URL, with the
#  given value when displaying URL to the users. Do not change the actual
#  connection URL. If authentication token is enabled, the token is added to the
#  custom URL automatically.
#
#  This option is intended to be used when the URL to display to the user cannot
#  be determined reliably by the Jupyter notebook server (proxified or
#  containerized setups for example).
c.NotebookApp.custom_display_url = 'http://127.0.0.1:8888'

## The IP address the notebook server will listen on.
c.NotebookApp.ip = '0.0.0.0'

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (NotebookApp.browser)
#  configuration option.
c.NotebookApp.open_browser = False

## The port the notebook server will listen on.
c.NotebookApp.port = 8888
