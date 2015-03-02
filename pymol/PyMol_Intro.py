import pymol
pymol.pymol_argv = [ 'pymol', '-qc'] #  Quiet / no GUI
from pymol import cmd
pymol.finish_launching()

cmd.fetch('1TUP', async=False)
cmd.disable('all')
cmd.enable('1TUP')
#cmd.bg_color('white')
cmd.hide('all')
cmd.show('cartoon')
cmd.hide('cartoon', '/1TUP//E')
cmd.hide('cartoon', '/1TUP//F')
cmd.show('ribbon', '/1TUP//E')
cmd.show('ribbon', '/1TUP//F')
cmd.select('zinc', 'name zn')
cmd.show('sphere', 'zinc')
cmd.png('1TUP.png', width=1980, height=1080, quiet=0, ray=1, prior=False)
cmd.quit()
