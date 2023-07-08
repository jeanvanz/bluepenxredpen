import cx_Freeze
executables=[
    cx_Freeze.Executable(script='main.py',icon='bluepen.ico')
]
cx_Freeze.setup(
    name='Bluepen x Redpen',
    options={
        'build_exe':{
            'packages':['pygame'],
            'include_files':[
                'bg.png',
                'bluepen.png',
                'redpen.png',
                'cupid.mp3',
                'bluepen.ico'
            ]
        }
    },executables=executables
)
# python gerasetup.py build
# python gerasetup.py bdist_msi