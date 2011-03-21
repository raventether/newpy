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

class NewtonBody:
	def __init__(self):
		self.body_userData = {}
	
	# NewtonCreateBody
	# NEWTON_API NewtonBody* NewtonCreateBody (const NewtonWorld* newtonWorld, const NewtonCollision* collision);
	def createBody(self, collision):
		return self.dl.NewtonCreateBody(self.world, collision)
	
	# NewtonDestroyBody
	# NEWTON_API void  NewtonDestroyBody(const NewtonWorld* newtonWorld, const NewtonBody* body);
	def destroyBody(self, body):
		self.dl.NewtonDestroyBody(self.world, body)
		
	# NewtonBodyAddForce
	# NEWTON_API void  NewtonBodyAddForce (const NewtonBody* body, const dFloat* force);
	def bodyAddForce(self, body, forceX, forceY, forceZ):
		force = VectorType(forceX, forceY, forceZ)
		self.dl.NewtonBodyAddForce(body, pointer(force))
	
	# NewtonBodyAddTorque
	# NEWTON_API void  NewtonBodyAddTorque (const NewtonBody* body, const dFloat* torque);
	def bodyAddTorque(self, body, torqueX, torqueY, torqueZ):
		torque = VectorType(torqueX, torqueY, torqueZ)
		self.dl.NewtonBodyAddTorque(body, pointer(torque))
	
	# NewtonBodyCalculateInverseDynamicsForce
	# NEWTON_API void  NewtonBodyCalculateInverseDynamicsForce (const NewtonBody* body, dFloat timestep, const dFloat* desiredVeloc, dFloat* forceOut);
	def bodyCalculateInverseDynamicsForce(self, body, timestep, desiredVelocX, desiredVelocY, desiredVelocZ):
		desiredVeloc = VectorType(desiredVelocX, desiredVelocY, desiredVelocZ)
		forceOut = VectorType(0., 0., 0.)
		self.dl.NewtonBodyCalculateInverseDynamicsForce(body, c_float(timestep), pointer(desiredVeloc), pointer(forceOut))
		return forceOut
	
	# NewtonBodySetMatrix
	# NEWTON_API void  NewtonBodySetMatrix (const NewtonBody* body, const dFloat* matrix);
	def bodySetMatrix(self, body, m):
		matrix = MatrixType(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[13], m[14], m[15])
		self.dl.NewtonBodySetMatrix(body, pointer(matrix))
	
	# NewtonBodySetMatrixRecursive
	# NEWTON_API void  NewtonBodySetMatrixRecursive (const NewtonBody* body, const dFloat* matrix);
	def bodySetMatrixRecursive(self, body, m):
		matrix = MatrixType(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8], m[9], m[10], m[11], m[12], m[13], m[14], m[15])
		self.dl.NewtonBodySetMatrixRecursive(body, pointer(matrix))
		
	# NewtonBodySetMassMatrix
	# NEWTON_API void  NewtonBodySetMassMatrix (const NewtonBody* body, dFloat mass, dFloat Ixx, dFloat Iyy, dFloat Izz);
	def bodySetMassMatrix(self, body, mass, ix, iy, iz):
		self.dl.NewtonBodySetMassMatrix(body, c_float(mass), c_float(ix), c_float(iy), c_float(iz))
	
	# NewtonBodySetMaterialGroupID
	# NEWTON_API void  NewtonBodySetMaterialGroupID (const NewtonBody* body, int id);
	def bodySetMaterialGroupID(self, body, id):
		self.dl.NewtonBodySetMaterialGroupID(body, c_int(id))
	
	# NewtonBodySetContinuousCollisionMode
	# NEWTON_API void  NewtonBodySetContinuousCollisionMode (const NewtonBody* body, unsigned state);
	def bodySetContinuousCollisionMode(self, body, state):
		self.dl.NewtonBodySetContinuousCollisionMode(body, c_uint(state))
	
	# NewtonBodySetJointRecursiveCollision
	# NEWTON_API void  NewtonBodySetJointRecursiveCollision (const NewtonBody* body, unsigned state);
	def bodySetJointRecursiveCollision(self, body, state):
		self.dl.NewtonBodySetJointRecursiveCollision(body, c_uint(state))
	
	# NewtonBodySetOmega
	# NEWTON_API void  NewtonBodySetOmega (const NewtonBody* body, const dFloat* omega);
	def bodySetOmega(self, body, ox, oy, oz):
		omega = VectorType(ox, oy, oz)
		self.dl.NewtonBodySetOmega(body, pointer(omega))
			
	# NewtonBodySetVelocity
	# NEWTON_API void  NewtonBodySetVelocity (const NewtonBody* body, const dFloat* velocity);
	def bodySetVelocity(self, body, velX, velY, velZ):
		vel = VectorType(velX, velY, velZ)
		self.dl.NewtonBodySetVelocity(body, pointer(vel))

	# NewtonBodySetForce
	# NEWTON_API void  NewtonBodySetForce (const NewtonBody* body, const dFloat* force);
	def bodySetForce(self, body, fx, fy, fz):
		force = Vector4Type(fx, fy, fz, 1.0)
		self.dl.NewtonBodySetForce(body, pointer(force))

	# NewtonBodySetTorque
	# NEWTON_API void  NewtonBodySetTorque (const NewtonBody* body, const dFloat* torque);
	def bodySetTorque(self, body, tx, ty, tz):
		torque = VectorType(tx, ty, tz)
		self.dl.NewtonBodySetTorque(body, pointer(torque))

	# NewtonBodySetCentreOfMass
	# NEWTON_API void  NewtonBodySetCentreOfMass  (const NewtonBody* body, const dFloat* com);
	def bodySetCentreOfMass(self, body, offsetX, offsetY, offsetZ):
		offset = VectorType(offsetX, offsetY, offsetZ)
		self.dl.NewtonBodySetCentreOfMass(body, pointer(offset))
	
	# NewtonBodySetLinearDamping
	# NEWTON_API void  NewtonBodySetLinearDamping (const NewtonBody* body, dFloat linearDamp);
	def bodySetLinearDamping(self, body, linearDamp):
		self.dl.NewtonBodySetLinearDamping(body, c_float(linearDamp))
	
	# NewtonBodySetAngularDamping
	# NEWTON_API void  NewtonBodySetAngularDamping (const NewtonBody* body, const dFloat* angularDamp);
	def bodySetAngularDamping(self, body, angularDamp1, angularDamp2, angularDamp3):
		angularDamp = VectorType(angularDamp1, angularDamp2, angularDamp3)
		self.dl.NewtonBodySetAngularDamping(body, pointer(angularDamp))
	
	# NewtonBodySetUserData
	# NEWTON_API void  NewtonBodySetUserData (const NewtonBody* body, void* userData);
	def bodySetUserData(self, body, userData):
		hashValue = hash(userData)
		self.body_userData[hashValue] = userData
		self.dl.NewtonBodySetUserData(body, hashValue)
	
	# NewtonBodySetCollision
	# NEWTON_API void  NewtonBodySetCollision (const NewtonBody* body, const NewtonCollision* collision);
	def bodySetCollision(self, body, collision):
		self.dl.NewtonBodySetCollision(body, collision)
		
	# NewtonBodyGetSleepState
	# NEWTON_API int  NewtonBodyGetSleepState (const NewtonBody* body);
	def bodyGetSleepState(self, body):
		return self.dl.NewtonBodyGetSleepState(body)
	
	# NewtonBodyGetAutoSleep
	# NEWTON_API int  NewtonBodyGetAutoSleep (const NewtonBody* body);
	def bodyGetAutoSleep(self, body):
		return self.dl.NewtonBodyGetAutoSleep(body)
	
	# NewtonBodySetAutoSleep
	# NEWTON_API void NewtonBodySetAutoSleep (const NewtonBody* body, int state);
	def bodySetAutoSleep(self, body, state):
		self.dl.NewtonBodySetAutoSleep(body, c_int(state))
	
	# NewtonBodyGetFreezeState
	# NEWTON_API int  NewtonBodyGetFreezeState(const NewtonBody* body);
	def bodyGetFreezeState(self, body):
		return self.dl.NewtonBodyGetFreezeState(body)
	
	# NewtonBodySetFreezeState
	# NEWTON_API void NewtonBodySetFreezeState (const NewtonBody* body, int state);
	def bodySetFreezeState(self, body, freezeState):
		self.dl.NewtonBodySetFreezeState(body, c_int(freezeState))
	
	# NewtonBodySetDestructorCallback
	# NEWTON_API void  NewtonBodySetDestructorCallback (const NewtonBody* body, NewtonBodyDestructor callback);
	def bodySetDestructorCallback(self, body, callback):
		cb = self.bodyDestructor_callbackType(callback)
		self.dl.NewtonBodySetDestructorCallback(body, cb)
		self.bodyDestructor_callbackList.append(cb)
	
	# NewtonBodySetTransformCallback
	# NEWTON_API void  NewtonBodySetTransformCallback (const NewtonBody* body, NewtonSetTransform callback);
	def bodySetTransformCallback(self, body, callback):
		cb = self.setTransform_callbackType(callback)
		self.dl.NewtonBodySetTransformCallback(body, cb)
		self.setTransform_callbackList.append(cb)
	
	# NewtonBodySetForceAndTorqueCallback
	# NEWTON_API void  NewtonBodySetForceAndTorqueCallback (const NewtonBody* body, NewtonApplyForceAndTorque callback);
	def bodySetForceAndTorqueCallback(self, body, callback):
		cb = self.applyForceAndTorque_callbackType(callback)
		self.dl.NewtonBodySetForceAndTorqueCallback(body, cb)
		self.applyForceAndTorque_callbackList.append(cb)
			
	# NewtonBodyGetForceAndTorqueCallback
	# NEWTON_API NewtonApplyForceAndTorque NewtonBodyGetForceAndTorqueCallback (const NewtonBody* body);
	def bodyGetForceAndTorqueCallback(self, body):
		return self.dl.NewtonBodyGetForceAndTorqueCallback(body)
	
	# NewtonBodyGetUserData
	# NEWTON_API void* NewtonBodyGetUserData (const NewtonBody* body);
	def bodyGetUserData(self, body):
		hashValue = self.dl.NewtonBodyGetUserData(body)
		return self.body_userData[hashValue]
	
	# NewtonBodyGetWorld
	# NEWTON_API NewtonWorld* NewtonBodyGetWorld (const NewtonBody* body);
	def bodyGetWorld(self, body):
		return self.dl.NewtonBodyGetWorld(body)
	
	# NewtonBodyGetCollision
	# NEWTON_API NewtonCollision* NewtonBodyGetCollision (const NewtonBody* body);
	def bodyGetCollision(self, body):
		return self.dl.NewtonBodyGetCollision(body)
	
	# NewtonBodyGetMaterialGroupID
	# NEWTON_API int   NewtonBodyGetMaterialGroupID (const NewtonBody* body);
	def bodyGetMaterialGroupID(self, body):
		return self.dl.NewtonBodyGetMaterialGroupID(body)
		
	# NewtonBodyGetContinuousCollisionMode
	# NEWTON_API int   NewtonBodyGetContinuousCollisionMode (const NewtonBody* body);
	def bodyGetContinuousCollisionMode(self, body):
		return self.dl.NewtonBodyGetContinuousCollisionMode(body)
		
	# NewtonBodyGetJointRecursiveCollision
	# NEWTON_API int   NewtonBodyGetJointRecursiveCollision (const NewtonBody* body);
	def bodyGetJointRecursiveCollision(self, body):
		return self.dl.NewtonBodyGetJointRecursiveCollision(body)
			
	# NewtonBodyGetMatrix
	# NEWTON_API void  NewtonBodyGetMatrix(const NewtonBody* body, dFloat* matrix);
	def bodyGetMatrix(self, body):
		matrix = MatrixType(0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.)
		self.dl.NewtonBodyGetMatrix(body, pointer(matrix))
		return matrix
			
	# NewtonBodyGetRotation
	# NEWTON_API void  NewtonBodyGetRotation(const NewtonBody* body, dFloat* rotation);
	def bodyGetRotation(self, body):
		angles = VectorType(0., 0., 0.)
		self.dl.NewtonBodyGetRotation(body, pointer(angles))
		return angles
	
	# NewtonBodyGetMassMatrix
	# NEWTON_API void  NewtonBodyGetMassMatrix (const NewtonBody* body, dFloat* mass, dFloat* Ixx, dFloat* Iyy, dFloat* Izz);
	def bodyGetMassMatrix(self, body):
		mass = c_float(0.)
		ix = c_float(0.)
		iy = c_float(0.)
		iz = c_float(0.)
		self.dl.NewtonBodyGetMassMatrix(body, pointer(mass), pointer(ix), pointer(iy), pointer(iz))
		return [mass, ix, iy, iz]
	
	# NewtonBodyGetInvMass
	# NEWTON_API void  NewtonBodyGetInvMass(const NewtonBody* body, dFloat* invMass, dFloat* invIxx, dFloat* invIyy, dFloat* invIzz);
	def bodyGetInvMass(self, body):
		invMass = c_float(0.)
		invIx = c_float(0.)
		invIy = c_float(0.)
		invIz = c_float(0.)
		self.dl.NewtonBodyGetInvMass(body, pointer(invMass), pointer(invIx), pointer(invIy), pointer(invIz))
		return [invMass, invIx, invIy, invIz]
		
	# NewtonBodyGetOmega
	# NEWTON_API void  NewtonBodyGetOmega(const NewtonBody* body, dFloat* vector);
	def bodyGetOmega(self, body):
		omega = VectorType(0., 0., 0.)
		self.dl.NewtonBodyGetOmega(body, pointer(omega))
		return omega
	
	# NewtonBodyGetVelocity
	# NEWTON_API void  NewtonBodyGetVelocity(const NewtonBody* body, dFloat* vector);
	def bodyGetVelocity(self, body):
		velocity = VectorType(0., 0., 0.)
		self.dl.NewtonBodyGetVelocity(body, pointer(velocity))
		return velocity
	
	# NewtonBodyGetForce
	# NEWTON_API void  NewtonBodyGetForce(const NewtonBody* body, dFloat* vector);
	def bodyGetForce(self, body):
		force = VectorType(0., 0., 0.)
		self.dl.NewtonBodyGetForce(body, pointer(force))
		return force
		
	# NewtonBodyGetTorque
	# NEWTON_API void  NewtonBodyGetTorque(const NewtonBody* body, dFloat* vector);
	def bodyGetTorque(self, body):
		torque = VectorType(0., 0., 0.)
		self.dl.NewtonBodyGetTorque(body, pointer(torque))
		return torque
	
	# NewtonBodyGetForceAcc
	# NEWTON_API void  NewtonBodyGetForceAcc(const NewtonBody* body, dFloat* vector);
	def bodyGetForceAcc(self, body):
		forceAcc = VectorType(0., 0., 0.)
		self.dl.NewtonBodyGetForceAcc(body, pointer(forceAcc))
		return forceAcc
	
	# NewtonBodyGetTorqueAcc
	# NEWTON_API void  NewtonBodyGetTorqueAcc(const NewtonBody* body, dFloat* vector);
	def bodyGetTorqueAcc(self, body):
		torqueAcc = VectorType(0., 0., 0.)
		self.dl.NewtonBodyGetTorqueAcc(body, pointer(torqueAcc))
		return torqueAcc
	
	# NewtonBodyGetCentreOfMass
	# NEWTON_API void  NewtonBodyGetCentreOfMass (const NewtonBody* body, dFloat* com);
	def bodyGetCentreOfMass(self, body):
		centerOfMass = VectorType(0., 0., 0.)
		self.dl.NewtonBodyGetCentreOfMass(body, pointer(centerOfMass))
		return centerOfMass
	
	# NewtonBodyGetLinearDamping
	# NEWTON_API dFloat NewtonBodyGetLinearDamping (const NewtonBody* body);
	def bodyGetLinearDamping(self, body):
		return self.dl.NewtonBodyGetLinearDamping(body)
	
	# NewtonBodyGetAngularDamping
	# NEWTON_API void  NewtonBodyGetAngularDamping (const NewtonBody* body, dFloat* vector);
	def bodyGetAngularDamping(self, body):
		angularDamping = VectorType(0., 0., 0.)
		self.dl.NewtonBodyGetAngularDamping(body, pointer(angularDamping))
		return angularDamping
	
	# NewtonBodyGetAABB
	# NEWTON_API void  NewtonBodyGetAABB (const NewtonBody* body, dFloat* p0, dFloat* p1);
	def bodyGetAABB(self, body):
		point0 = VectorType(0., 0., 0.)
		point1 = VectorType(0., 0., 0.)
		self.dl.NewtonBodyGetAABB(body, pointer(point0), pointer(point1))
		return point0, point1
	
	# NewtonBodyGetFirstJoint
	# NEWTON_API NewtonJoint* NewtonBodyGetFirstJoint (const NewtonBody* body);
	def bodyGetFirstJoint(self, body):
		return self.dl.NewtonBodyGetFirstJoint(body)
	
	# NewtonBodyGetNextJoint
	# NEWTON_API NewtonJoint* NewtonBodyGetNextJoint (const NewtonBody* body, const NewtonJoint* joint);
	def bodyGetNextJoint(body, joint):
		return self.dl.NewtonBodyGetNextJoint(body, joint)
	
	# NewtonBodyGetFirstContactJoint
	# NEWTON_API NewtonJoint* NewtonBodyGetFirstContactJoint (const NewtonBody* body);
	def bodyGetFirstContactJoint(self, body):
		return self.dl.NewtonBodyGetFirstContactJoint(body)
	
	# NewtonBodyGetNextContactJoint
	# NEWTON_API NewtonJoint* NewtonBodyGetNextContactJoint (const NewtonBody* body, const NewtonJoint* contactJoint);
	def bodyGetNextContactJoint(self, body, joint):
		return self.dl.NewtonBodyGetNextContactJoint(body, joint)
	
	# NewtonContactJointGetFirstContact
	# NEWTON_API void* NewtonContactJointGetFirstContact (const NewtonJoint* contactJoint);
	def contactJointGetFirstContact(self, joint):
		return self.dl.NewtonContactJointGetFirstContact(joint)
	
	# NewtonContactJointGetNextContact
	# NEWTON_API void* NewtonContactJointGetNextContact (const NewtonJoint* contactJoint, void* contact);
	def contactJointGetNextContact(self, joint, contact):
		return self.dl.NewtonContactJointGetNextContact(joint, contact)
	
	# NewtonContactJointGetContactCount
	# NEWTON_API int NewtonContactJointGetContactCount(const NewtonJoint* contactJoint);
	def contactJointGetContactCount(self, joint):
		return self.dl.NewtonContactJointGetContactCount(joint)
	
	# NewtonContactJointRemoveContact
	# NEWTON_API void NewtonContactJointRemoveContact(const NewtonJoint* contactJoint, void* contact); 
	def contactJointRemoveContact(self, joint, contact):
		self.dl.NewtonContactJointRemoveContact(joint, contact)
	
	# NewtonContactGetMaterial
	# NEWTON_API NewtonMaterial* NewtonContactGetMaterial (const void* contact);
	def contactGetMaterial(self, contact):
		return self.dl.NewtonContactGetMaterial(contact)
	
	# NewtonBodyAddBuoyancyForce
	# NEWTON_API void  NewtonBodyAddBuoyancyForce (const NewtonBody* body, dFloat fluidDensity,  dFloat fluidLinearViscosity, dFloat fluidAngularViscosity, const dFloat* gravityVector, NewtonGetBuoyancyPlane buoyancyPlane, void *context);
	#def bodyAddBuoyancyForce(body, fluidDensity, fluidLinearViscosity, fluidAngularViscosity, gravityVectorX, gravityVectorY, gravityVectorZ, 

	# NewtonBodyAddImpulse
	# NEWTON_API void NewtonBodyAddImpulse (const NewtonBody* body, const dFloat* pointDeltaVeloc, const dFloat* pointPosit);
	def bodyAddImpulse(self, body, pointDeltaVelocX, pointDeltaVelocY, pointDeltaVelocZ, pointPositX, pointPositY, pointPositZ):
		pointDeltaVeloc = VectorType(pointDeltaVelocX, pointDeltaVelocY, pointDeltaVelocZ)
		pointPosit = VectorType(pointPositX, pointPositY, pointPositZ)
		self.dl.NewtonBodyAddImpulse(body, pointer(pointDeltaVeloc), pointer(pointPosit))
	
if '__main__' == __name__:
	pass
	