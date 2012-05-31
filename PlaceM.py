class Place:
	def __init__(self, iInitialSupply, iDistance):
		self._Supplies = iInitialSupply  # local food supply 
		self._Distance = iDistance # distance from the start point, counted in day-walk.
	def GiveSupply(self,iSupplyNumber):
		self._Supplies -= iSupplyNumber
	def GetSupply(self,iSupplyNumber):
		self._Supplies += iSupplyNumber
		return 
	def GetDistance(self):
		return self._Distance		

