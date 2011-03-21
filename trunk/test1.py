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

import random
import pygame
import pygame.locals
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from newpy import *

def bodyForceAndTorqueCallback(body, timestep, threadIndex):
	Application.newton.bodySetForce(body, 0., -9.8, 0.)
	Application.newton.bodySetTorque(body, 0., 0., 0.)
	
def setTransformCallback(body, matrix, threadIndex):
	pass

class Application:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('newpy v0.01')
		pygame.display.set_mode((800, 600), pygame.locals.HWSURFACE | pygame.locals.OPENGL | pygame.locals.DOUBLEBUF)
		
		glutInit()
		
		glClearColor(0., 0., 0., 1.)
		glClearDepth(1.)
		glEnable(GL_DEPTH_TEST)
		
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		
		# create and show some information about newton
		Application.newton = newpy.Newton()
		print 'NGD version: %s' % Application.newton.worldGetVersion()
		print 'NGD memory usage: %s' % Application.newton.getMemoryUsed()
		
		# create dynamic boxes bodies
		self.bodyBoxes = []
		for counter in xrange(100):
			collision = Application.newton.createBox(1., 1., 1.)
			bodyBox = Application.newton.createBody(collision)
			Application.newton.releaseCollision(collision)
			Application.newton.bodySetMassMatrix(bodyBox, 1., 1., 1., 1.)
			Application.newton.bodySetMatrix(bodyBox, [ 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., random.uniform(-0.6, 0.6), counter * 1.01 + 2., random.uniform(-0.6, 0.6), 1. ])
			
			Application.newton.bodySetLinearDamping(bodyBox, 0.)
			Application.newton.bodySetAngularDamping(bodyBox, 0., 0., 0.)
			
			Application.newton.bodySetForceAndTorqueCallback(bodyBox, bodyForceAndTorqueCallback)
			Application.newton.bodySetTransformCallback(bodyBox, setTransformCallback)
			self.bodyBoxes.append(bodyBox)
		
		# create static ground body
		collision = Application.newton.createBox(1000., 1., 1000.)
		self.bodyGround = Application.newton.createBody(collision)
		Application.newton.releaseCollision(collision)
		Application.newton.bodySetMassMatrix(self.bodyGround, 0., 0., 0., 0.)
		
	def __del__(self):
		del Application.newton
		
	def _handleEvents(self):
		for e in pygame.event.get():
			if e.type == pygame.locals.QUIT:
				self.stopMainLoop()
				
	def startMainLoop(self):
		self._mainLoopActive = True
		#Application.newton.update(0.0)
		
		while self._mainLoopActive:
			# events
			self._handleEvents()
			
			# rendering
			glViewport(0, 0, 800, 600)
			glClear(GL_COLOR_BUFFER_BIT)
			glClear(GL_DEPTH_BUFFER_BIT)
			
			glMatrixMode(GL_PROJECTION)
			glLoadIdentity()
			gluPerspective(70., 800. / 600., 4., 10000.)
			
			glMatrixMode(GL_MODELVIEW)
			glLoadIdentity()
			gluLookAt(7., 24., 12., 0., 0., 0., 0., 1., 0.)
			
			# draw dynamic boxes
			for bodyBox in self.bodyBoxes:
				glPushMatrix()
				glMultMatrixf(Application.newton.bodyGetMatrix(bodyBox))
				glScalef(1., 1., 1.)
				glutSolidCube(1.)
				glPopMatrix()
			
			# draw static ground body
			glPushMatrix()
			glScalef(20., 1., 20.)
			glutSolidCube(1.)
			glPopMatrix()
			
			glFlush()
			pygame.display.flip()
			
			# physics
			Application.newton.update(0.1)
		
	def stopMainLoop(self):
		self._mainLoopActive = False
		
if '__main__' == __name__:
	# try to use psyco accelerations
	try:
		import psyco
		psyco.full()
		print 'Psyco detected -- using Psyco'
	except ImportError:
		print 'Psyco is not detected -- not using Psyco'

	# app code
	application = Application()
	application.startMainLoop()
	del application
	