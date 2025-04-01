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

from typing import Tuple
from pathlib import Path
import subprocess
import sys
import os

from Shared.certoraUtils import is_windows


def run_shell_file(script: str, workdir: Path) -> Tuple[int, str, str]:
    """
    Runs a shell script whose results are to be analyzed by the caller
    @param script: the name of the shell script to run
    @param workdir: the working directory to run from
    @return: A tuple with the exit code, stdout, and stderr

    """
    if is_windows():
        """
        Windows is incredibly tricky in CI.
        First, it does not interpret correctly the env set to python3. It requires running with `python`.
        So we assume our run script contains of a single command - a call to certoraRun/certoraRun.py,
        strips out the certoraRun argument, and replaces it with CERTORARUN.
        In non-CI envs, we will call certoraRun.py as usual with python3.
        """
        contents = []
        # assumes the script is a single command
        with open(workdir / script, 'r') as script_contents:
            for l in script_contents.readlines():
                contents += l.strip().split(" ")

        if "CI" in os.environ:
            python = "python"
            certorarun = os.environ["CERTORARUN"]
        else:
            python = "python3"
            certorarun = "certoraRun.py"
        args = [python, certorarun] + contents[1:]
    else:
        args = ["bash", script]

    pipes = subprocess.Popen(args, cwd=str(workdir), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_err = pipes.communicate()
    # for some reason, certoraRun outputs errors to stdout, so returning both
    return pipes.returncode, std_out.strip().decode(sys.getfilesystemencoding()), std_err.strip().decode(
        sys.getfilesystemencoding())
