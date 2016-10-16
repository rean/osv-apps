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

'''
_catalina_base = "/usr/tomcat"
_catalina_home = _catalina_base
_catalina_tmpdir = _catalina_base + "/temp"

_classpath = [_catalina_home + "/bin/bootstrap.jar"]

_logging_config = [
    "-Djava.util.logging.config.file=%s/conf/logging.properties" % _catalina_base,
    "-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager"
]
_classpath.append("%s/bin/tomcat-juli.jar" % _catalina_base)

default_old = api.run_java(
        classpath=_classpath,
        args=_logging_config + [
            "-Dcatalina.base=%s" % _catalina_base,
            "-Dcatalina.home=%s" % _catalina_base,
            "-Djava.io.tmpdir=%s" % _catalina_tmpdir,
            "org.apache.catalina.startup.Bootstrap", "start"
        ])
'''
default = api.run('/cli/cli.so')
