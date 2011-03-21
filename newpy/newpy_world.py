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
from newpy_types import *

class NewtonWorld:
	def __init__(self):
		self.world_userData = None

	# NewtonCreate
	# NEWTON_API NewtonWorld* NewtonCreate (NewtonAllocMemory malloc, NewtonFreeMemory mfree);
	# NOTE: see World.__init__ for this function
	
	# NewtonDestroy
	# NEWTON_API void NewtonDestroy (const NewtonWorld* newtonWorld);
	# NOTE: see World.__del__ for this function
	
	# NewtonDestroyAllBodies
	# NEWTON_API void NewtonDestroyAllBodies (const NewtonWorld* newtonWorld);
	# NOTE: see World.__del__ for this function
		
	# NewtonGetMemoryUsed
	# NEWTON_API int NewtonGetMemoryUsed ();
	def getMemoryUsed(self):
		return self.dl.NewtonGetMemoryUsed()
		
	# NewtonUpdate
	# NEWTON_API void NewtonUpdate (const NewtonWorld* newtonWorld, dFloat timestep);
	def update(self, timestep):
		self.dl.NewtonUpdate(self.world, c_float(timestep))
		
	# NewtonInvalidateCache
	# NEWTON_API void NewtonInvalidateCache (const NewtonWorld* newtonWorld);
	def invalidateCache(self):
		self.dl.NewtonInvalidateCache(self.world)
	
	# NewtonCollisionUpdate
	# NEWTON_API void NewtonCollisionUpdate (const NewtonWorld* newtonWorld);
	def collisionUpdate(self):
		self.dl.NewtonCollisionUpdate(self.world)
		
	# NewtonSetSolverModel
	# NEWTON_API void NewtonSetSolverModel (const NewtonWorld* newtonWorld, int model);
	def setSolverModel(self, model):
		self.dl.NewtonSetSolverModel(self.world, c_int(model))
		
	# NewtonSetPlatformArchitecture
	# NEWTON_API void NewtonSetPlatformArchitecture (const NewtonWorld* newtonWorld, int mode);
	def setPlatformArchitecture(self, mode):
		self.dl.NewtonSetPlatformArchitecture(self.world, c_int(mode))
	
	# NewtonGetPlatformArchitecture
	# NEWTON_API int NewtonGetPlatformArchitecture(const NewtonWorld* newtonWorld, char* description);
	def getPlatformArchitecture(self):
		return self.dl.NewtonGetPlatformArchitecture(self.world, c_int(0))
	# TODO: add getting of arch desc for NewtonGetPlatformArchitecture
		
	# NewtonSetMultiThreadSolverOnSingleIsland
	# NEWTON_API void NewtonSetMultiThreadSolverOnSingleIsland (const NewtonWorld* newtonWorld, int mode);
	def setMultiThreadSolverOnSingleIsland(self, mode):
		self.dl.NewtonSetMultiThreadSolverOnSingleIsland(self.world, c_int(mode))
	
	# NewtonGetMultiThreadSolverOnSingleIsland
	# NEWTON_API int NewtonGetMultiThreadSolverOnSingleIsland (const NewtonWorld* newtonWorld);
	def getMultiThreadSolverOnSingleIsland(self):
		return self.dl.NewtonGetMultiThreadSolverOnSingleIsland(self.world)
	
	# NewtonSetPerformanceClock
	# NEWTON_API void NewtonSetPerformanceClock (const NewtonWorld* newtonWorld, NewtonGetTicksCountCallback callback);
	def setPerformanceClock(self, callback):
		cb = self.getTicksCountCallback_callbackType(callback)
		self.dl.NewtonSetPerformanceClock(self.world, cb)
		self.getTicksCountCallback_callbackList.append(cb)
		
	# NewtonReadPerformanceTicks
	# NEWTON_API unsigned NewtonReadPerformanceTicks (const NewtonWorld* newtonWorld, unsigned performanceEntry);
	def readPerformanceTicks(self, performanceEntry):
		return self.dl.NewtonReadPerformanceTicks(self.world, c_uint(performanceEntry))
		
	# NewtonWorldCriticalSectionLock
	# NEWTON_API void NewtonWorldCriticalSectionLock (const NewtonWorld* newtonWorld);
	def worldCriticalSectionLock(self):
		self.dl.NewtonWorldCriticalSectionLock(self.world)
	
	# NewtonWorldCriticalSectionUnlock
	# NEWTON_API void NewtonWorldCriticalSectionUnlock (const NewtonWorld* newtonWorld);
	def worldCriticalSectionUnlock(self):
		self.dl.NewtonWorldCriticalSectionUnlock(self.world)
		
	# NewtonSetThreadsCount
	# NEWTON_API void NewtonSetThreadsCount (const NewtonWorld* newtonWorld, int threads);
	def setThreadsCount(self, threads):
		self.dl.NewtonSetThreadsCount(self.world, c_int(threads))
		
	# NewtonGetThreadsCount
	# NEWTON_API int NewtonGetThreadsCount(const NewtonWorld* newtonWorld);
	def getThreadsCount(self):
		return self.dl.NewtonGetThreadsCount(self.world)
		
	# NewtonSetFrictionModel
	# NEWTON_API void NewtonSetFrictionModel (const NewtonWorld* newtonWorld, int model);
	def setFrictionModel(self, model):
		self.dl.NewtonSetFrictionModel(self.world, c_int(model))
		
	# NewtonSetMinimumFrameRate
	# NEWTON_API void NewtonSetMinimumFrameRate (const NewtonWorld* newtonWorld, dFloat frameRate);
	def setMinimumFrameRate(self, frameRate):
		self.dl.NewtonSetMinimumFrameRate(self.world, frameRate)
	
	# NewtonSetBodyLeaveWorldEvent
	# NEWTON_API void NewtonSetBodyLeaveWorldEvent (const NewtonWorld* newtonWorld, NewtonBodyLeaveWorld callback); 
	def setBodyLeaveWorldEvent(self, callback):
		cb = self.bodyLeaveWorld_callbackType(callback)
		self.dl.NewtonSetBodyLeaveWorldEvent(self.world, cb)
		self.bodyLeaveWorld_callbackList.append(cb)
		
	# NewtonSetWorldSize
	# NEWTON_API void NewtonSetWorldSize (const NewtonWorld* newtonWorld, const dFloat* minPoint, const dFloat* maxPoint); 
	def setWorldSize(self, minX, minY, minZ, maxX, maxY, maxZ):
		min = VectorType(minX, minY, minZ)
		max = VectorType(maxX, maxY, maxZ)
		self.dl.NewtonSetWorldSize(self.world, pointer(min), pointer(max))
		
	# NewtonSetIslandUpdateEvent
	# NEWTON_API void NewtonSetIslandUpdateEvent (const NewtonWorld* newtonWorld, NewtonIslandUpdate islandUpdate); 
	def setIslandUpdateEvent(self, callback):
		cb = self.islandUpdate_callbackType(callback)
		self.dl.NewtonSetIslandUpdateEvent(self.world, cb)
		self.islandUpdate_callbackList.append(cb)
		
	# NewtonWorldForEachJointDo
	# NEWTON_API void NewtonWorldForEachJointDo (const NewtonWorld* newtonWorld, NewtonJointIterator callback);

	# NewtonWorldForEachBodyInAABBDo
	# NEWTON_API void NewtonWorldForEachBodyInAABBDo (const NewtonWorld* newtonWorld, const dFloat* p0, const dFloat* p1, NewtonBodyIterator callback);
	
	# NewtonWorldGetVersion
	# NEWTON_API int NewtonWorldGetVersion (const NewtonWorld* newtonWorld);
	def worldGetVersion(self):
		return self.dl.NewtonWorldGetVersion(self.world)
	
	# NewtonWorldSetUserData
	# NEWTON_API void NewtonWorldSetUserData (const NewtonWorld* newtonWorld, void* userData);
	def worldSetUserData(self, userData):
		self.world_userData = userData
		self.dl.NewtonWorldSetUserData(self.world, 1)
	
	# NewtonWorldGetUserData
	# NEWTON_API void* NewtonWorldGetUserData (const NewtonWorld* newtonWorld);
	def worldGetUserData(self, userData):
		self.dl.NewtonWorldGetUserData(self.world)
		return self.world_userData
	
	# NewtonWorldSetDestructorCallBack
	# NEWTON_API void NewtonWorldSetDestructorCallBack (const NewtonWorld* newtonWorld, NewtonDestroyWorld destructor);
	def worldSetDestructorCallBack(self, callback):
		cb = self.destroyWorld_callbackType(callback)
		self.worldSetDestructorCallBack(self.world, cb)
		self.destroyWorld_callbackList.append(cb)
	
	# NewtonWorldGetDestructorCallBack
	# NEWTON_API NewtonDestroyWorld NewtonWorldGetDestructorCallBack (const NewtonWorld* newtonWorld);
	def worldGetDestructorCallBack(self):
		return self.dl.NewtonWorldGetDestructorCallBack(self.world)
	
	# NewtonWorldRayCast
	# NEWTON_API void NewtonWorldRayCast (const NewtonWorld* newtonWorld, const dFloat* p0, const dFloat* p1, NewtonWorldRayFilterCallback filter, void* userData, NewtonWorldRayPrefilterCallback prefilter);
	
	# NewtonWorldConvexCast
	# NEWTON_API int NewtonWorldConvexCast (const NewtonWorld* newtonWorld, const dFloat* matrix, const dFloat* target, const NewtonCollision* shape, dFloat* hitParam, void* userData, NewtonWorldRayPrefilterCallback prefilter, NewtonWorldConvexCastReturnInfo* info, int maxContactsCount, int threadIndex);
	
	# NewtonWorldGetBodyCount
	# NEWTON_API int NewtonWorldGetBodyCount(const NewtonWorld* newtonWorld);
	def worldGetBodyCount(self):
		return self.dl.NewtonWorldGetBodyCount(self.world)
	
	# NewtonWorldGetConstraintCount
	# NEWTON_API int NewtonWorldGetConstraintCount(const NewtonWorld* newtonWorld);
	def worldGetConstraintCount(self):
		return NewtonWorldGetConstraintCount(self.world)
	
if '__main__' == __name__:
	pass
	