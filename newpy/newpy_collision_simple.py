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

class NewtonCollisionSimple:
	def __init__(self):
		pass

	# NewtonCreateNull
	def createNull(self):
		return self.dl.NewtonCreateNull(self.world)
	
	# NewtonCreateSphere
	def createSphere(self, radX, radY, radZ, shapeId = 0, m = None):
		collision = 0
		if m == None:
			collision = self.dl.NewtonCreateSphere(self.world, c_float(radX), c_float(radY), c_float(radZ), c_int(shapeId), c_int(0))
		else:
			DataType = c_float * 16
			matrix = DataType(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[13], m[14], m[15])
			collision = self.dl.NewtonCreateSphere(self.world, c_float(radX), c_float(radY), c_float(radZ), c_int(shapeId), pointer(matrix))
		return collision
		
	# NewtonCreateBox
	def createBox(self, dx, dy, dz, shapeId = 0, m = None):
		collision = 0
		if m == None:
			collision = self.dl.NewtonCreateBox(self.world, c_float(dx), c_float(dy), c_float(dz), c_int(shapeId), c_int(0))
		else:
			DataType = c_float * 16
			matrix = DataType(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[13], m[14], m[15])
			collision = self.dl.NewtonCreateBox(self.world, c_float(dx), c_float(dy), c_float(dz), c_int(shapeId), pointer(matrix))
		return collision
	
	# NewtonCreateCone
	def createCone(self, radius, height, shapeId = 0, m = None):
		collision = 0
		if m == None:
			collision = self.dl.NewtonCreateCone(self.world, c_float(radius), c_float(height), c_int(shapeId), c_int(0))
		else:
			DataType = c_float * 16
			matrix = DataType(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[13], m[14], m[15])
			collision = self.dl.NewtonCreateCone(self.world, c_float(radius), c_float(height), c_int(shapeId), pointer(matrix))
		return collision
	
	# NewtonCreateCapsule
	def createCapsule(self, radius, height, shapeId = 0, m = None):
		collision = 0
		if m == None:
			collision = self.dl.NewtonCreateCapsule(self.world, c_float(radius), c_float(height), c_int(shapeId), c_int(0))
		else:
			DataType = c_float * 16
			matrix = DataType(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[13], m[14], m[15])
			collision = self.dl.NewtonCreateCapsule(self.world, c_float(radius), c_float(height), c_int(shapeId), pointer(matrix))
		return collision
	
	# NewtonCreateCylinder
	def createCylinder(self, radius, height, shapeId = 0, m = None):
		collision = 0
		if m == None:
			collision = self.dl.NewtonCreateCylinder(self.world, c_float(radius), c_float(height), c_int(shapeId), c_int(0))
		else:
			DataType = c_float * 16
			matrix = DataType(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[13], m[14], m[15])
			collision = self.dl.NewtonCreateCylinder(self.world, c_float(radius), c_float(height), c_int(shapeId), pointer(matrix))
		return collision
	
	# NewtonCreateChamferCylinder
	def createChamferCylinder(self, radius, height, shapeId = 0, m = None):
		collision = 0
		if m == None:
			collision = self.dl.NewtonCreateChamferCylinder(self.world, c_float(radius), c_float(height), c_int(shapeId), c_int(0))
		else:
			DataType = c_float * 16
			matrix = DataType(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[13], m[14], m[15])
			collision = self.dl.NewtonCreateChamferCylinder(self.world, c_float(radius), c_float(height), c_int(shapeId), pointer(matrix))
		return collision
	
	# NEWTON_API NewtonCollision* NewtonCreateConvexHull (const NewtonWorld* newtonWorld, int count, const dFloat* vertexCloud, int strideInBytes, dFloat tolerance, int shapeID, const dFloat *offsetMatrix);
	# NEWTON_API NewtonCollision* NewtonCreateConvexHullFromMesh (const NewtonWorld* newtonWorld, const NewtonMesh* mesh, dFloat tolerance, int shapeID);
	# NEWTON_API NewtonCollision* NewtonCreateConvexHullModifier (const NewtonWorld* newtonWorld, const NewtonCollision* convexHullCollision);
	# NEWTON_API void NewtonConvexHullModifierGetMatrix (const NewtonCollision* convexHullCollision, dFloat* matrix);
	# NEWTON_API void NewtonConvexHullModifierSetMatrix (const NewtonCollision* convexHullCollision, const dFloat* matrix);
	# NEWTON_API int NewtonCollisionIsTriggerVolume(const NewtonCollision* convexCollision);
	# NEWTON_API void NewtonCollisionSetAsTriggerVolume(const NewtonCollision* convexCollision, int trigger);
	# NEWTON_API unsigned NewtonCollisionGetUserID (const NewtonCollision* convexCollision);
	# NEWTON_API int NewtonConvexHullGetFaceIndices (const NewtonCollision* convexHullCollision, int face, int* faceIndices);
	# NEWTON_API dFloat NewtonConvexCollisionCalculateVolume (const NewtonCollision* convexCollision);
	# NEWTON_API void NewtonConvexCollisionCalculateInertialMatrix (const NewtonCollision* convexCollision, dFloat* inertia, dFloat* origin);	
	# NEWTON_API void NewtonCollisionMakeUnique (const NewtonWorld* newtonWorld, const NewtonCollision* collision);

	# NewtonReleaseCollision
	def releaseCollision(self, collision):
		self.dl.NewtonReleaseCollision(self.world, collision)

	# NEWTON_API int NewtonAddCollisionReference (const NewtonCollision* collision);
		
if '__main__' == __name__:
	pass
	