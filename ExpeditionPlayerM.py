import PlaceM
import ManM
class ExpeditionPlayer:
	def __init__(self,iPlaceCount):
		self._Places = []		
		self._Day = 0
		self._Places.append(PlaceM.Place(9999,0))
		for ii in range(1,iPlaceCount+1):
			self._Places.append(PlaceM.Place(0,ii))
		self._PlaceNumber = iPlaceCount
	def SetMen(self,iMen):
		self._Men = iMen
		
	def DumpStatistics(self):
		for Place in self._Places:
			print "Place %2d has %2d supplies" % (Place.GetDistance(),Place.GetSupplyStat())
		
		return
	def RunOneDay(self):
		print "--------Day %2d--------------------------" % self._Day
		for Man in self._Men:
			RC = Man.RunOneDay()
			#Man.GetStat()
			if not RC:
				print "Error while travelling"
				return False
		self._Day += 1
		return True
		
	def GetPlace(self,iPlaceNo):
		if iPlaceNo < len(self._Places):
			return self._Places[iPlaceNo]
		else: 
			return None
		
ExpeditionPlayerInstance = ExpeditionPlayer(6)
Men = []
Repeat= 3
Men.append( ManM.Man(1,ManM.PorterToPlace1Pattern,Repeat-1,ExpeditionPlayerInstance))
Men.append( ManM.Man(2,ManM.PorterToPlace1Pattern,Repeat-1,ExpeditionPlayerInstance))
Men.append( ManM.Man(3,ManM.PorterToPlace1Pattern,Repeat,ExpeditionPlayerInstance))
Men.append( ManM.Man(4,ManM.PorterToPlace1Pattern,Repeat,ExpeditionPlayerInstance))

Men.append( ManM.Man(8,ManM.PorterToPlace2Pattern,1,ExpeditionPlayerInstance))
Men.append( ManM.Man(9,ManM.PorterToPlace2Pattern,1,ExpeditionPlayerInstance))

Men.append( ManM.Man(12,ManM.PorterToPlace3Pattern,1,ExpeditionPlayerInstance))
Men.append( ManM.Man(13,ManM.PorterToPlace3Pattern,1,ExpeditionPlayerInstance))

Men.append( ManM.Man(14,ManM.PorterToPlace4Pattern,1,ExpeditionPlayerInstance))

Men.append( ManM.Man(15,ManM.Traveller,1,ExpeditionPlayerInstance))

ExpeditionPlayerInstance.SetMen(Men)
for i in range(12):	
	RC = ExpeditionPlayerInstance.RunOneDay()
	ExpeditionPlayerInstance.DumpStatistics()
	if not RC:
		print "Error while travelling , stop simulation"
		break	
	
