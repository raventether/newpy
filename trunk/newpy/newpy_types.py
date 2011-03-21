#!/usr/bin/env python
# -*- coding: utf-8 -*-

# newpy - Newton Game Dynamics FFI-binding for Python language
# Copyright (C) 2009 Timur Ruziev aka resurtm
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ctypes import *

class NewtonTypes:
	def __init__(self):
		pass

# type for using 3 floats size vector
VectorType = c_float * 3

# type for using 4 floats size vector
Vector4Type = c_float * 4

# type for using matrices with 4 x 4 float size (16 total floats)
MatrixType = c_float * 16
		
if '__main__' == __name__:
	pass
	