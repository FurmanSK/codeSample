from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
# use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "codeSample"
default_task = "publish"


@init
def set_properties(project):
    project.depends_on_requirements("requirements.txt")
