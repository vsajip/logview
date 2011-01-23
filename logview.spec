# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'), os.path.join(HOMEPATH,'support/useUnicode.py'), 'logview.py'],
             pathex=[os.getcwd()])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.%s/logview' % sys.platform, 'logview'),
          debug=False,
          strip=False,
          upx=True,
          console=1 )
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist', 'logview'))
if sys.platform.startswith('darwin'):
    app = BUNDLE(coll, name=os.path.join('dist', 'LogView.app'), version='0.1')
    if 'QtCore' in [t[0] for t in a.binaries]:
        print 'Copying Qt resources ...'
        import shutil
        src = '/Library/Frameworks/QtGui.framework/Versions/4/Resources/qt_menu.nib'
        dst = os.path.join('dist', 'LogView.app', 'Contents', 'Resources', 'qt_menu.nib')
        shutil.copytree(src, dst)
        src = 'App.icns'
        dst = os.path.join('dist', 'LogView.app', 'Contents', 'Resources', 'App.icns')
        shutil.copyfile(src, dst)
