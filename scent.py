from sniffer.api import * # import the really small API
import os, termstyle

# you can customize the pass/fail colors like this
pass_fg_color = termstyle.green
pass_bg_color = termstyle.bg_default
fail_fg_color = termstyle.red
fail_bg_color = termstyle.bg_default

# this gets invoked on every file that gets changed in the directory. Return
# True to invoke any runnable functions, False otherwise.
#
# This fires runnables only if files ending with .py extension and not prefixed
# with a period.
@file_validator
def py_files(filename):
    # dir_name is the full path to the directory of the file that changed
    dir_path = os.path.dirname(filename)
    return filename.endswith('.py') and not dir_path.startswith('.') and not dir_path.endswith('/tmp') and not dir_path.endswith('/script')

# This gets invoked for verification. This is ideal for running tests of some sort.
# For anything you want to get constantly reloaded, do an import in the function.
#
# sys.argv[0] and any arguments passed via -x prefix will be sent to this function as
# it's arguments. The function should return logically True if the validation passed
# and logicially False if it fails.
#
# This example simply runs nose.
@runnable
def execute_nose(*args):
    import nose
    return nose.run(argv=list(args))
