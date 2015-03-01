import pymol
from pymol import cmd
#pymol.pymol_argv = [ 'pymol', '-qc'] #  Quiet / no GUI
pymol.finish_launching()

cmd.fetch('1TUP', async=False)
cmd.disable('all')
cmd.enable('1TUP')
#cmd.bg_color('white')
cmd.png('/tmp/1TUP.png')
cmd.hide('all')
cmd.show('cartoon')
cmd.hide('cartoon', '/1TUP//E')
cmd.hide('cartoon', '/1TUP//F')
cmd.show('ribbon', '/1TUP//E')
cmd.show('ribbon', '/1TUP//F')
cmd.select('zinc', 'name zn')
cmd.show('sphere', 'zinc')
cmd.mset(1, 60)
cmd.frame(1)
cmd.mview()
cmd.set_view((-0.175534308,   -0.331560850,   -0.926960170,
             0.541812420,     0.753615797,   -0.372158051,
             0.821965039,    -0.567564785,    0.047358301,
             0.000000000,     0.000000000, -249.619018555,
             58.625568390,   15.602619171,   77.781631470,
             196.801528931, 302.436492920,  -20.000000000), animate=2)

cmd.frame(60)
cmd.mplay()
#cmd.set_view((-0.175534308,   -0.331560850,   -0.926960170,
#              0.541812420,    0.753615797,   -0.372158051,
#              0.821965039,   -0.567564785,    0.047358301,
#              -0.000067875,    0.000017881, -249.615447998,
#              54.029174805,   26.956727982,   77.124832153,
#             196.801528931,  302.436492920,  -20.000000000), animate=1)
#cmd.set_view((-0.175534308,   -0.331560850,   -0.926960170,
#              0.541812420,    0.753615797,   -0.372158051,
#              0.821965039,   -0.567564785,    0.047358301,
#              -0.000067875,    0.000017881,  -55.406421661,
#              54.029174805,   26.956727982,   77.124832153,
#              2.592475891,  108.227416992,  -20.000000000), animate=2)
cmd.mpng('ble')

#cmd.quit()
