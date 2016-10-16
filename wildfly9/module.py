from osv.modules.api import *
from osv.modules.filemap import FileMap
from osv.modules import api

require('lua')
require('ncurses')
require('libedit')
require_running('httpserver')

usr_files = FileMap()
usr_files.add('${OSV_BASE}/modules/cli').to('/cli') \
        .include('cli.so') \
        .include('cli.lua') \
        .include('lib/**') \
        .include('commands/**')

api.require('java')
api.require('cli')

#full = api.run('/cli/cli.so')
#default = full
default = api.run('/cli/cli.so')
