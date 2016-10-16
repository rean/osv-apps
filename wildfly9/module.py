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

# To run use:
# sudo scripts/run.py -n -v -V -e "java.so -cp .:/usr/wildfly/jboss-modules.jar:/usr/wildfly/modules/system/layers/base/org/jboss/logmanager/main/jboss-logmanager-2.0.0.Final.jar -D[Standalone] -Djava.util.logging.manager=org.jboss.logmanager.LogManager -Djava.net.preferIPv4Stack=true -Djboss.modules.system.pkgs=org.jboss.byteman -Djava.awt.headless=true -Dorg.jboss.boot.log.file=/usr/wildfly/standalone/log/server.log -Dlogging.configuration=file:/usr/wildfly/standalone/configuration/logging.properties -Djboss.home.dir=/usr/wildfly -Djboss.server.base.dir=/usr/wildfly/standalone -Djboss.bind.address=0.0.0.0 -jar /usr/wildfly/jboss-modules.jar -mp /usr/wildfly/modules org.jboss.as.standalone"
