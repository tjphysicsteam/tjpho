live:
  sphinx-autobuild . _build/html/

html:
  sphinx-build -M html . _build/

build-strict:
  sphinx-build -M html . _build/ -n -W
