# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support', '_mountzlib.py'),
              os.path.join(HOMEPATH,'support', 'useUnicode.py'), 'logview.py'],
              pathex=[os.getcwd()])
pyz = PYZ(a.pure)
appname = 'logview'
if sys.platform == 'win32':
    exename = '%s.exe' % appname
else:
    exename = appname
exe_args = {
	'exclude_binaries': True,
    'name': os.path.join('build', 'pyi.%s' % sys.platform, appname, exename),
    'debug': False,
    'strip': False,
    'upx': True,
    'console': False
}
if sys.platform == 'win32':
	exe_args['icon']  = 'logview.ico'
exe = EXE(pyz, a.scripts, **exe_args)
coll = COLLECT(exe,
               a.binaries,
               (
               	('README', 'README', 'DATA'),
               	('LICENSE', 'LICENSE', 'DATA'),
               ),
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist', appname))
import shutil
if sys.platform.startswith('darwin'):
    app = BUNDLE(coll, name=os.path.join('dist', 'LogView.app'), version='0.1')
    if 'QtCore' in [t[0] for t in a.binaries]:
        src = '/Library/Frameworks/QtGui.framework/Versions/4/Resources/qt_menu.nib'
        dst = os.path.join('dist', 'LogView.app', 'Contents', 'Resources', 'qt_menu.nib')
        print 'Copying Qt resources ...'
        shutil.copytree(src, dst)
        src = 'App.icns'
        dst = os.path.join('dist', 'LogView.app', 'Contents', 'Resources', 'App.icns')
        print 'Copying icon ...'
        shutil.copyfile(src, dst)
else:
    src = 'logview.ico'
    dst = os.path.join('dist', appname, src)
    shutil.copyfile(src, dst)
