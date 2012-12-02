class FixtureGroup(object):
	fixtures = []

class Fixture(object):
	address = 1
	controls = []
	
	def getState(self):
		channels = [None] * 512
		for control in self.controls:
			for offset, value in control.getLevels():
				if(value is None):
					continue
				channels[address + offset] = value
		return (address, channels)
	
	def addControl(control):
		self.controls.append(control)

class RGBControl(object):
	red_offset = 0
	green_offset = 1
	blue_offset = 2
	red_level = 0
	green_level = 0
	blue_level = 0
	
	def setColor(self, hex):
		pass
	
	def configureRGBOffsets(self, r, g, b):
		self.red_offset = r
		self.green_offset = g
		self.blue_offset = b
	
	def getState(self):
		rgb = [None] * 512
		rgb[self.red_offset] = self.red_level
		rgb[self.green_offset] = self.green_level
		rgb[self.blue_offset] = self.blue_level
		return rgb

class XYControl(object):
	has_fine_control = False
	x_offset = 0
	xfine_offset = None
	y_offset = 1
	xfine_offset = None
	x_level = 0
	xfine_level = 0
	y_level = 0
	xfine_level = 0
	
	def setPosition(self, x, y):
		pass
	
	def configureXYOffsets(self, x, y, xfine=None, yfine=None):
		self.has_fine_control = (xfine is None and yfine is None)
		if(self.has_fine_control):
			self.xfine_offset = xfine
			self.yfine_offset = yfine
		self.x_offset = x
		self.y_offset = y
	
	def getState(self):
		xy = [None] * 512
		xy[self.x_offset] = self.x_level
		xy[self.y_offset] = self.y_level
		if(self.has_fine_control):
			xy[self.xfine_offset] = self.xfine_level
			xy[self.yfine_offset] = self.yfine_level
		return xy

class StrobeControl(object):
	strobe_offset = 4
	strobe_value = 0
	
	def configureStrobeOffset(self, strobe):
		self.strobe_offset = strobe
	
	def setStrobe(self, value):
		self.strobe_value = value

	def getState(self):
		return [
			(self.strobe_offset, self.strobe_value)
		]

class ProgramControl(object):
	program_offset = 5
	program_speed_offset = 4
	program_macros = dict()
	
	def setMacro(self, label, value, speed):
		self.program_macros[label] = (value, speed)
	
	def configureProgramOffset(self, program):
		self.program_offset = program

	def setProgram(self, program):
		pass

class IntensityControl(object):
	intensity_offset = 6
	intensityfine_offset = None

#example code
fixture.setColor('#fff')
fixture.setPosition(0.5, 0.2)
fixture.setIntensity(0.9)
fixture.strobeSpeed(10) #ms?
fixture[0].setColor('#f00') # subfixtures
fixture.setMacro('short-fade')

