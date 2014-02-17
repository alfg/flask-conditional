flask-conditional
=================

Conditional decorators for Flask routes.

```python
from flask import Flask
from flask.ext.conditional import conditional

app = Flask(__name__)

ENABLED = True

@conditional(app.route('/'), ENABLED)
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```


Example for disabling authentication when debugging:
```python
AUTH_ENABLED = False # Disable auth for debugging

@app.route("/settings")
@conditional(login_required, AUTH_ENABLED)
def settings():
    pass
```

## Installation
Preferred method of installation is via pip::

    $ pip install flask-conditional
    
    
## License

The MIT License (MIT)

Copyright (c) 2014 Alfred Gutierrez

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
