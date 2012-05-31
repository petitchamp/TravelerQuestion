import ExpeditionPlayerM
class Man:
	# 3 numbers: place, action (dump/take | 0/1), number
	def __init__(self, iId,iActionList):
		self._ActionList = []
		self._ActionList.append((1,0,2))
		self._ExpeditionPlayer = ExpeditionPlayerM.ExpeditionPlayerInstance
		self._Place = 0
		self._Supply = 4
		self._Day = 0
		self._Id = 0
		self._MissionEnded = False
		return

	# Take supply from place
	def TakeSupply(self, iNumber):
		self._ExpeditionPlayer.GetPlace(self._Place).GiveSupply(iNumber)
		return
	# Dump supply to place
	def DumpSupply(self, iNumber):
		self._ExpeditionPlayer.GetPlace(self._Place).GetSupply(iNumber)
		return

	# Run one day action
	# - take supply from place D day if needed
	# - Go to place of D+1 day
	# - dump supply to current place D+1 day if needed
	# - death condition: if supply equals to 0 and mission not finished , action of next day 
	
	def RunOneDay(self):
		if self._MissionEnded == True:
			return True
		
		if self._Day <= len(self._ActionList):
			DailyAction = self._ActionList[self._Day] 
		
			#Go to today's destination
			if  DailyAction[0]-self._Place == 1 :
				self._Place = DailyAction[0]
			else:
				print "Error: Man %2d is in place %d, destination %d is too far to go" , (self._Id,self._Place,DailyAction[0])
				return False

			#Action
			if DailyAction[1] == 0: ## dump food
				TakeSupply(DailyAction[2]):
			elif DailyAction[1] == 1: ## take food
				DumpSupply(DailyAction[2]):
			
			#Increment counter
			self._Day +=1
			self._Supply -= 1
			
			if self._Day > len(self._ActionList):
				_MissionEnded = True
				return _MissionEnded
				
			elif self._Supply == 0 :
				print "Fatal : Man %2d : I still have mission tomorrow , but I have no supply, so I die tomorrow" , _Id
				return False
			return True	
		else:
			print "Error: man id: %d have no action for day %d", (self._Id,self._Day)
			return False
		
	def GetStat(self):
		print "Man No.%2d Supply: %1d Day: %2d Mission Ended: %s" (self._Id, self._Day, self._MissionEnded? "Yes" : "No")		
