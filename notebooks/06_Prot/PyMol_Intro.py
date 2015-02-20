import __main__
#__main__.pymol_argv = [ 'pymol', '-qc'] # Quiet and no GUI
import pymol
pymol.finish_launching()

pymol.cmd.fetch('1TUP')
pymol.cmd.disable('all')
pymol.cmd.enable('1TUP')
#pymol.cmd.bg_color('white')
pymol.cmd.png('/tmp/1TUP.png')
pymol.cmd.hide('all')
pymol.cmd.show('cartoon')
#pymol.cmd.hide('cartoon', '/1TUP//E')
#pymol.cmd.hide('cartoon', '/1TUP//F')
#pymol.cmd.show('ribbon', '/1TUP//E')
#pymol.cmd.show('ribbon', '/1TUP//F')
#pymol.cmd.quit()
