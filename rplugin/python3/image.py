import neovim
from subprocess import Popen, PIPE
import os
import json
import time
import pynvim as nvim
from pynvim import autocmd

# nvim.autocmd(show_image(), 'BufNew')

@neovim.plugin
class NeotagsPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim
        self.working_dir = os.environ.get('XDG_RUNTIME_DIR', os.path.expanduser("~") or None)
        self.process = Popen(['ueberzug', 'layer', '--silent'], cwd=self.working_dir,
                                stdin=PIPE, universal_newlines=True)

    def log(self, string):
        self.nvim.command(f'echo "{string}"')

    def execute(self, **kwargs):
        self.process.stdin.write(json.dumps(kwargs) + '\n')
        self.process.stdin.flush()

    @neovim.autocmd('BufEnter', pattern='*')
    def show_image(self):
        print("called show image")
        self.nvim.command("let imagefile = expand('%:p')")
        imagefile = self.nvim.eval("imagefile")
        width = self.nvim.current.window.width
        height = self.nvim.current.window.height

        x_offset = self.nvim.current.window.col
        y_offset = self.nvim.current.window.row
        self.execute(
                action='add',
                identifier=f'{imagefile}',
                x=x_offset,
                y=y_offset,
                max_width=width,
                max_height=height,
                path=imagefile
            )

    @neovim.autocmd('BufWipeout', pattern='*')
    @neovim.autocmd('TabLeave', pattern='*')
    @neovim.autocmd('BufHidden', pattern='*')
    def remove_image(self):
        # self.log("called remove image")
        self.nvim.out_write('called remove')
        self.nvim.command("let imagefile = expand('%:p')")
        imagefile = self.nvim.eval("imagefile")
        self.log(imagefile)
        self.execute(action='remove', identifier=f'{imagefile}')
