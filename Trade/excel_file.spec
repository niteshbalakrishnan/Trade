# -*- mode: python -*-

block_cipher = None


a = Analysis(['excel_file.py'],
             pathex=['C:\\Phython Projects\\Trade\\Trade'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='excel_file',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='ndowed')
