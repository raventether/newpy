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

class NewtonStructs:
	def __init__(self):
		pass

# struct NewtonCollisionInfoRecord
class NewtonCollisionInfoRecord_structType(Structure):
	_fields_ = [
	]
	
	def __init__(self):
		pass
		
# struct NewtonJointRecord
class NewtonJointRecord_structType(Structure):
	_fields_ = [
	]
	
	def __init__(self):
		pass
		
# struct NewtonUserMeshCollisionCollideDesc
class NewtonUserMeshCollisionCollideDesc_structType(Structure):
	_fields_ = [
	]
	
	def __init__(self):
		pass
		
# struct NewtonWorldConvexCastReturnInfo
class NewtonWorldConvexCastReturnInfo_structType(Structure):
	_fields_ = [
	]
	
	def __init__(self):
		pass
	
# struct NewtonUserMeshCollisionRayHitDesc
class NewtonUserMeshCollisionRayHitDesc_structType(Structure):
	_fields_ = [
	]
	
	def __init__(self):
		pass
	
# struct NewtonHingeSliderUpdateDesc
class NewtonHingeSliderUpdateDesc_structType(Structure):
	_fields_ = [
		('m_accel', c_float),
		('m_minFriction', c_float),
		('m_maxFriction', c_float),
		('m_timestep', c_float),
	]

	def __init__(self):
		pass

if '__main__' == __name__:
	pass
	