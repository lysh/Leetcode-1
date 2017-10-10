class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        Hours=[["0"],["1","2","4","8"],["3","5","9","6","10"],["7","11"]]
        Minutes=[["00"],["01","02","04","08","16","32"],["03","05","09","17","33","06","10","18","34","12","20","36","24","40","48"],["07","11","19","35","13","21","37","25","41","49","14","22","38","26","42","50","28","44","52","56"],["15","23","39","27","43","51","29","45","53","57","30","46","54","58"],["31","47","55","59"]]
        List=[]

        for h in range(num+1):
        	m=num-h
        	if(m>5 or h>3):
        		continue
        	for j in Hours[h]:
        		for k in Minutes[m]:
        			List.append(j+":"+k)
       	return List


print(Solution().readBinaryWatch(0))


        