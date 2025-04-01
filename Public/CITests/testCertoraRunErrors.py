#!/usr/bin/env python3

#     The Certora Prover
#     Copyright (C) 2025  Certora Ltd.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, version 3 of the License.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import unittest
import os
from pathlib import Path
import sys

# Add the path to the Test directory to the system path
test_dir_path = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(test_dir_path))

# Add the path to the scripts directory to the system path
scripts_dir_path = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir_path))
from CITests.testCertoraRunUtils import run_shell_file

if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <TestEVM path> <CITests path>")
    sys.exit(1)

TestEVM_path = sys.argv[1]
CITests_path = sys.argv[2]
os.environ["CERTORA_TEST_DATA_DIRECTORY"] = f"{CITests_path}/test_data"


class TestErrorMessages(unittest.TestCase):

    def test_imports(self) -> None:
        cwd = Path.cwd()
        # Making sure we see certoraRun.py for the runner scripts
        os.environ["PATH"] = os.environ["PATH"] + f":{cwd / 'scripts'}"
        workdir = Path(TestEVM_path) / "PythonScripts" / "ImportTypo"
        exitcode, stdout, stderr = run_shell_file("errRun.sh", workdir)
        msg = stdout.replace("\n", "").replace("\r", "")  # stdout contains new lines
        self.assertNotEqual(0, exitcode)
        expected = "do not import existing .spec"
        if expected not in msg:
            print("Expected: ", expected)
            print("Actual: ", msg)
        self.assertTrue(expected in msg)
        self.assertTrue("settup.spec" in msg)


if __name__ == '__main__':
    test_argv = [f"{sys.argv[1]}, {sys.argv[2]}"]
    unittest.main(argv=test_argv, exit=False)
