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
import os
from newpy_body import *
from newpy_callbacks import *
from newpy_collision_simple import *
from newpy_structs import *
from newpy_types import *
from newpy_world import *

class Newton(NewtonBody, NewtonCallbacks, NewtonCollisionSimple, NewtonStructs, NewtonTypes, NewtonWorld):
	def __init__(self):
		# get shared / dynamic library instance
		if sys.platform == 'darwin':
			self.dl = CDLL('./libNewton.dylib')
		elif os.name == 'posix':
			self.dl = CDLL('./libNewton.so')
		elif os.name == 'nt':
			self.dl = CDLL('./newton.dll')
		
		# initialize newton world
		self.world = self.dl.NewtonCreate(c_int(), c_int())
		
		# call parents' constructors
		NewtonBody.__init__(self)
		NewtonCallbacks.__init__(self)
		NewtonCollisionSimple.__init__(self)
		NewtonStructs.__init__(self)
		NewtonTypes.__init__(self)
		NewtonWorld.__init__(self)
	
	def __del__(self):
		# destroy all bodies and newton world
		self.dl.NewtonDestroyAllBodies(self.world)
		self.dl.NewtonDestroy(self.world)

if '__main__' == __name__:
	pass
	