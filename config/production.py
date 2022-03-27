from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x9e\xb3^\xf3\xc9\xab\xd0+\x0b\xf2\xb1\x80\\\x7f\x1d\x86'