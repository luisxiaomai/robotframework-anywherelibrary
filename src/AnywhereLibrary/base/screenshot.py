import os
import robot
from keywordgroup import KeywordGroup
from util import *

class Screenshot(KeywordGroup):

    def __init__(self):
        self._screenshot_index = 0

    # Public
    def capture_page_screenshot(self, filename=None):
        """Takes a screenshot of the current page and embeds it into the log.

        *filename* argument specifies the name of the file to write the
        screenshot into. If no `filename` is given, the screenshot is saved into file
        `selenium-screenshot-<counter>.png` under the directory where
        the Robot Framework log file is written into. The `filename` is
        also considered relative to the same directory, if it is not
        given in absolute format.

        """
        path, link = self._get_screenshot_paths(filename)

        if hasattr(Util.driver, 'get_screenshot_as_file'):
          Util.driver.get_screenshot_as_file(path)
        else:
          Util.driver.save_screenshot(path)

        # Image is shown on its own row and thus prev row is closed on purpose
        self._html('</td></tr><tr><td colspan="3"><a href="%s">'
                   '<img src="%s" width="800px"></a>' % (link, link))

    # Private

    def _get_screenshot_paths(self, filename):
        if not filename:
            self._screenshot_index += 1
            if Util.device=='common':
                filename = '%s-screenshot-%d.png' % (Util.platform,self._screenshot_index)
            else:
                filename = '%s(%s)-screenshot-%d.png' % (Util.platform,Util.device,self._screenshot_index)
        else:
            filename = filename.replace('/', os.sep)
        logdir = self._get_log_dir()
        path = os.path.join(logdir, filename)
        link = robot.utils.get_link_path(path, logdir)
        return path, link
