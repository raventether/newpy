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
from newpy_structs import *

class NewtonCallbacks:
	def __init__(self):
		# NewtonAllocMemory
		self.allocMemory_callbackList = []
		# NewtonFreeMemory
		self.freeMemory_callbackList = []
		# NewtonDestroyWorld
		self.destroyWorld_callbackList = []
		# NewtonGetTicksCountCallback
		self.getTicksCountCallback_callbackList = []
		# NewtonSerialize
		self.serialize_callbackList = []
		# NewtonDeserialize
		self.deserialize_callbackList = []
		# NewtonUserMeshCollisionDestroyCallback
		self.userMeshCollisionDestroyCallback_callbackList = []
		# NewtonUserMeshCollisionCollideCallback
		self.userMeshCollisionCollideCallback_callbackList = []
		# NewtonUserMeshCollisionRayHitCallback
		self.userMeshCollisionRayHitCallback_callbackList = []
		# NewtonUserMeshCollisionGetCollisionInfo
		self.userMeshCollisionGetCollisionInfo_callbackList = []
		# NewtonUserMeshCollisionGetFacesInAABB
		self.userMeshCollisionGetFacesInAABB_callbackList = []
		# NewtonCollisionTreeRayCastCallback
		self.collisionTreeRayCastCallback_callbackList = []
		# NewtonTreeCollisionCallback
		self.treeCollisionCallback_callbackList = []
		# NewtonBodyDestructor
		self.bodyDestructor_callbackList = []
		# NewtonBodyLeaveWorld
		self.bodyLeaveWorld_callbackList = []
		# NewtonApplyForceAndTorque
		self.applyForceAndTorque_callbackList = []
		# NewtonSetTransform
		self.setTransform_callbackList = []
		# NewtonIslandUpdate
		self.islandUpdate_callbackList = []
		# NewtonGetBuoyancyPlane
		self.getBuoyancyPlane_callbackList = []
		# NewtonWorldRayPrefilterCallback
		self.worldRayPrefilterCallback_callbackList = []
		# NewtonWorldRayFilterCallback
		self.worldRayFilterCallback_callbackList = []
		# NewtonOnAABBOverlap
		self.onAABBOverlap_callbackList = []
		# NewtonContactsProcess
		self.contactsProcess_callbackList = []
		# NewtonBodyIterator
		self.bodyIterator_callbackList = []
		# NewtonJointIterator
		self.jointIterator_callbackList = []
		# NewtonCollisionIterator
		self.collisionIterator_callbackList = []
		# NewtonBallCallBack
		self.ballCallBack_callbackList = []
		# NewtonHingeCallBack
		self.hingeCallBack_callbackList = []
		# NewtonSliderCallBack
		self.sliderCallBack_callbackList = []
		# NewtonUniversalCallBack
		self.universalCallBack_callbackList = []
		# NewtonCorkscrewCallBack
		self.corkscrewCallBack_callbackList = []
		# NewtonUserBilateralCallBack
		self.userBilateralCallBack_callbackList = []
		# NewtonUserBilateralGetInfoCallBack
		self.userBilateralGetInfoCallBack_callbackList = []
		# NewtonConstraintDestructor
		self.constraintDestructor_callbackList = []
		
	# NewtonAllocMemory
	# typedef void* (*NewtonAllocMemory) (int sizeInBytes);
	allocMemory_callbackType = CFUNCTYPE(c_void_p, c_int)

	# NewtonFreeMemory
	# typedef void (*NewtonFreeMemory) (void *ptr, int sizeInBytes);
	freeMemory_callbackType = CFUNCTYPE(None, c_void_p, c_int)

	# NewtonDestroyWorld
	# typedef void (*NewtonDestroyWorld) (const NewtonWorld* newtonWorld);
	destroyWorld_callbackType = CFUNCTYPE(None, c_int)

	# NewtonGetTicksCountCallback
	# typedef unsigned (*NewtonGetTicksCountCallback) ();
	getTicksCountCallback_callbackType = CFUNCTYPE(c_uint)
	
	# NewtonSerialize
	# typedef void (*NewtonSerialize) (void* serializeHandle, const void* buffer, int size);
	serialize_callbackType = CFUNCTYPE(None, c_void_p, c_void_p, c_int) 
	
	# NewtonDeserialize
	# typedef void (*NewtonDeserialize) (void* serializeHandle, void* buffer, int size);
	deserialize_callbackType = CFUNCTYPE(None, c_void_p, c_void_p, c_int)
	
	# NewtonUserMeshCollisionDestroyCallback
	# typedef void (*NewtonUserMeshCollisionDestroyCallback) (void* userData);
	userMeshCollisionDestroyCallback_callbackType = CFUNCTYPE(None, c_int)
	
	# NewtonUserMeshCollisionCollideCallback
	# typedef void (*NewtonUserMeshCollisionCollideCallback) (NewtonUserMeshCollisionCollideDesc* collideDescData);
	
	# NewtonUserMeshCollisionRayHitCallback
	# typedef dFloat (*NewtonUserMeshCollisionRayHitCallback) (NewtonUserMeshCollisionRayHitDesc* lineDescData);
	
	# NewtonUserMeshCollisionGetCollisionInfo
	# typedef void (*NewtonUserMeshCollisionGetCollisionInfo) (void* userData, NewtonCollisionInfoRecord* infoRecord);
	
	# NewtonUserMeshCollisionGetFacesInAABB
	# typedef int (*NewtonUserMeshCollisionGetFacesInAABB) (void* userData, const dFloat* p0, const dFloat* p1, const dFloat** vertexArray, int* vertexCount, int* vertexStrideInBytes, const int* indexList, int maxIndexCount, const int* userDataList);
	
	# NewtonCollisionTreeRayCastCallback
	# typedef dFloat (*NewtonCollisionTreeRayCastCallback) (dFloat interception, dFloat* normal, int faceId, void* usedData);
	collisionTreeRayCastCallback_callbackType = CFUNCTYPE(c_float, c_float, c_float * 3, c_int, c_int)
	
	# NewtonTreeCollisionCallback
	# typedef void (*NewtonTreeCollisionCallback) (const NewtonBody* bodyWithTreeCollision, const NewtonBody* body, int faceID, int vertexCount, const dFloat* vertex, int vertexStrideInBytes); 
	treeCollisionCallback_callbackType = CFUNCTYPE(None, c_int, c_int, c_int, c_int, POINTER(c_float), c_int)

	# NewtonBodyDestructor
	# typedef void (*NewtonBodyDestructor) (const NewtonBody* body);
	bodyDestructor_callbackType = CFUNCTYPE(None, c_int)
	
	# NewtonBodyLeaveWorld
	# typedef void (*NewtonBodyLeaveWorld) (const NewtonBody* body, int threadIndex);
	bodyLeaveWorld_callbackType = CFUNCTYPE(None, c_int, c_int)
	
	# NewtonApplyForceAndTorque
	# typedef void (*NewtonApplyForceAndTorque) (const NewtonBody* body, dFloat timestep, int threadIndex);
	applyForceAndTorque_callbackType = CFUNCTYPE(None, c_int, c_float, c_int)
	
	# NewtonSetTransform
	# typedef void (*NewtonSetTransform) (const NewtonBody* body, const dFloat* matrix, int threadIndex);
	setTransform_callbackType = CFUNCTYPE(None, c_int, POINTER(c_float * 16), c_int)
	
	# NewtonIslandUpdate
	# typedef int (*NewtonIslandUpdate) (const void* islandHandle, int bodyCount);
	islandUpdate_callbackType = CFUNCTYPE(c_int, c_int, c_int)
	
	# NewtonGetBuoyancyPlane
	# typedef int (*NewtonGetBuoyancyPlane) (const int collisionID, void *context, const dFloat* globalSpaceMatrix, dFloat* globalSpacePlane);
	getBuoyancyPlane_callbackType = CFUNCTYPE(c_int, c_int, c_int, c_float * 16, c_float * 4)
	
	# NewtonWorldRayPrefilterCallback
	# typedef unsigned (*NewtonWorldRayPrefilterCallback)(const NewtonBody* body, const NewtonCollision* collision, void* userData);
	worldRayPrefilterCallback_callbackType = CFUNCTYPE(c_uint, c_int, c_int, c_int)
	
	# NewtonWorldRayFilterCallback
	# typedef dFloat (*NewtonWorldRayFilterCallback)(const NewtonBody* body, const dFloat* hitNormal, int collisionID, void* userData, dFloat intersectParam);
	worldRayFilterCallback_callbackType = CFUNCTYPE(c_float, c_int, c_float * 3, c_int, c_int, c_float)
	
	# NewtonOnAABBOverlap
	# typedef int  (*NewtonOnAABBOverlap) (const NewtonMaterial* material, const NewtonBody* body0, const NewtonBody* body1, int threadIndex);
	onAABBOverlap_callbackType = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int)
	
	# NewtonContactsProcess
	# typedef void (*NewtonContactsProcess) (const NewtonJoint* contact, dFloat timestep, int threadIndex);
	contactsProcess_callbackType = CFUNCTYPE(None, c_int, c_float, c_int)
	
	# NewtonBodyIterator
	# typedef void (*NewtonBodyIterator) (const NewtonBody* body);
	bodyIterator_callbackType = CFUNCTYPE(None, c_int)
	
	# NewtonJointIterator
	# typedef void (*NewtonJointIterator) (const NewtonJoint* joint);
	jointIterator_callbackType = CFUNCTYPE(None, c_int)
	
	# NewtonCollisionIterator
	# typedef void (*NewtonCollisionIterator) (void* userData, int vertexCount, const dFloat* faceArray, int faceId);
	collisionIterator_callbackType = CFUNCTYPE(None, c_int, c_int, POINTER(c_float), c_int)
	
	# NewtonBallCallBack
	# typedef void (*NewtonBallCallBack) (const NewtonJoint* ball, dFloat timestep);
	ballCallBack_callbackType = CFUNCTYPE(None, c_int, c_float)
	
	# NewtonHingeCallBack
	# typedef unsigned (*NewtonHingeCallBack) (const NewtonJoint* hinge, NewtonHingeSliderUpdateDesc* desc);
	hingeCallBack_callbackType = CFUNCTYPE(c_uint, c_int, POINTER(NewtonHingeSliderUpdateDesc_structType))
	
	# NewtonSliderCallBack
	# typedef unsigned (*NewtonSliderCallBack) (const NewtonJoint* slider, NewtonHingeSliderUpdateDesc* desc);
	sliderCallBack_callbackType = CFUNCTYPE(c_uint, c_int, POINTER(NewtonHingeSliderUpdateDesc_structType))
	
	# NewtonUniversalCallBack
	# typedef unsigned (*NewtonUniversalCallBack) (const NewtonJoint* universal, NewtonHingeSliderUpdateDesc* desc);
	universalCallBack_callbackType = CFUNCTYPE(c_uint, c_int, POINTER(NewtonHingeSliderUpdateDesc_structType))
	
	# NewtonCorkscrewCallBack
	# typedef unsigned (*NewtonCorkscrewCallBack) (const NewtonJoint* corkscrew, NewtonHingeSliderUpdateDesc* desc);
	corkscrewCallBack_callbackType = CFUNCTYPE(c_uint, c_int, POINTER(NewtonHingeSliderUpdateDesc_structType))
	
	# NewtonUserBilateralCallBack
	# typedef void (*NewtonUserBilateralCallBack) (const NewtonJoint* userJoint, dFloat timestep, int threadIndex);
	userBilateralCallBack_callbackType = CFUNCTYPE(None, c_int, c_float, c_int)
	
	# NewtonUserBilateralGetInfoCallBack
	# typedef void (*NewtonUserBilateralCallBack) (const NewtonJoint* userJoint, dFloat timestep, int threadIndex);
	
	# NewtonConstraintDestructor
	# typedef void (*NewtonConstraintDestructor) (const NewtonJoint* me);
	constraintDestructor_callbackType = CFUNCTYPE(None, c_int)

if '__main__' == __name__:
	pass
	