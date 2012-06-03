class Place:
	def __init__(self, iInitialSupply, iDistance):
		self._Supplies = iInitialSupply  # local food supply 
		self._Distance = iDistance # distance from the start point, counted in day-walk.
	
	# Man dump supply to place
	def ReceiveSupply(self,iSupplyNumber):
		self._Supplies += iSupplyNumber
		
	# Place provide supply to man
	def ProvideSupply(self,iSupplyNumber):
		if iSupplyNumber > self._Supplies:
			return 0
		else:
			self._Supplies -= iSupplyNumber
			return iSupplyNumber
	def GetDistance(self):
		return self._Distance
	def GetSupplyStat(self):
		return self._Supplies

