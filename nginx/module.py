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

# Force the cli to be the starting command so we get the nginx bits on the
# image and we can debug the nginx start up
full = api.run('/cli/cli.so')
default = full

#default = api.run('/nginx-osv.so -c /usr/local/nginx/conf/nginx.conf')

