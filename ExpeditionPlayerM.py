import PlaceM
import ManM
class ExpeditionPlayer:
	def __init__(self,iPlaceCount):
		self._Places = []
		self._Mans = []
		self._Places.append(PlaceM.Place(9999,0))
		for ii in range(1,iPlaceCount+1):
			self._Places.append(PlaceM.Place(0,ii))
		self._PlaceNumber = iPlaceCount
	def SetMans(self,iMans):
		self._Mans = iMans
		
	def DumpStatistics(self):
		for Place in self._Places:
			print "Place %2d has %2d supplies" % (Place.GetDistance(),Place.GetSupplyStat())
		return
	def RunOneDday(self):
		return
	def Consolidation(self):
		return
	def GetPlace(self,iPlaceNo):
		if iPlaceNo < len(self._Places):
			return self._Places[iPlaceNo]
		else: 
			return None
		
ExpeditionPlayerInstance = ExpeditionPlayer(6)
ManOne = ManM.Man(1,ManM.PorterToPlace1Pattern,6,ExpeditionPlayerInstance)
for i in range(5):	
	ManOne.RunOneDay()
	ManOne.GetStat()
