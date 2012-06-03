import PlaceM
from collections import deque
#Man action definition
Nothing, Dump, Take = range(3)

PorterToPlace1Pattern=[(1,Dump,2),(0,Take,4)]
				
PorterToPlace2Pattern=[(1,Take,1),(2,Dump,2)]

class Man:
	# 3 numbers: place, action (dump/take | 0/1), number
	def __init__(self, iId, iActionPattern, iRepeatNum, iExpeditionPlayer):
		self._ActionList = deque()## take initial 4 days' supply from base
		self._ActionList.append((0,Take,5))
		
		for i in range(iRepeatNum):
			for (place,action,number) in iActionPattern:
				self._ActionList.append((place,action,number))
		#print self._ActionList
		self._ExpeditionPlayer = iExpeditionPlayer
		self._Place = -1
		self._Supply = 0
		self._Day = 0
		self._Id = iId
		self._MissionEnded = False
		return

	# Take supply from place
	def TakeSupply(self, iNumber):
		if iNumber <= 0 :
			print "[Man::TakeSupply Error] Wrong argument %d" % iNumber
			return 0
		Supply = self._ExpeditionPlayer.GetPlace(self._Place).ProvideSupply(iNumber)
		self._Supply += Supply
		return Supply
		
	# Dump supply to place
	def DumpSupply(self, iNumber):
		if iNumber <= 0:
			print "[Man::TakeSupply Error] Wrong argument %d" % iNumber
			return -1
		elif iNumber > self._Supply:
			print "[Man::DumpSupply Error] Man %d has only %d supply but is asked to dump %d supply on day %d" % (self._Id, self._Supply, iNumber, self._Day)
			return -1
		else:	
			self._ExpeditionPlayer.GetPlace(self._Place).ReceiveSupply(iNumber)
			self._Supply -= iNumber
			return 0

	# Run one day action
	# - take supply from place D day if needed
	# - Go to place of D+1 day
	# - dump supply to current place D+1 day if needed
	# - death condition: if supply equals to 0 and mission not finished , action of next day 
	
	def RunOneDay(self):
		if self._MissionEnded == True:
			print "Man %d is in place %d mission finished" % (self._Id,self._Place)
			return True		
		else:
			try :
				TodayAction = self._ActionList.popleft() 
				#print TodayAction
				#Go to today's destination
				if  abs((TodayAction[0]-self._Place)) <= 1 :
					self._Place = TodayAction[0]
				else:
					self.GetStat()
					print "Error: Man %d is in place %d, destination %d is too far to go" % (self._Id,self._Place,TodayAction[0])
					return False
				#Action
				if TodayAction[2] < 0:
					print "[Man::RunOneDay Error] Illigal take/dump number %d" %  TodayAction[2]
					return False
				elif TodayAction[1] == Take: ## dump food
					if self.TakeSupply(TodayAction[2]) == 0:
						print "[Man::RunOneDay Error] Man %2d failed to dump food on day %2d" % (self._Id, self._Day)
						return False
				elif TodayAction[1] == Dump: ## take food
					if self.DumpSupply(TodayAction[2]) < 0:
						print "[Man::RunOneDay Error] Man %2d failed to take food from place %d on day %2d" % (self._Id, self._Place, self._Day)
						return False
				#Increment counter
				self._Day +=1
				self._Supply -= 1
				if self._Day >= len(self._ActionList):
					self._MissionEnded = True
					return self._MissionEnded
				elif self._Supply == 0 :
					print "Fatal : Man %2d : I still have mission tomorrow , but I have no supply, so I die tomorrow" %( self._Id)
					return False
				return True	
			except IndexError:
				print "Error: man id: %d have no more action for day %d", (self._Id,self._Day)
				return False
		
	def GetStat(self):
		print "Man No.%2d Place:%2d Supply:%2d Day:%2d Mission Ended: %s" % (  self._Id, self._Place, self._Supply,self._Day, (self._MissionEnded and "Yes" or "No"))
	def GetInfo(self):
		return ( self._Id,self._Place,self._Supply)