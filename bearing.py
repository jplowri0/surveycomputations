import numpy as np

#this function computes the bearing between coordinates.
#https://stackoverflow.com/questions/31735499/calculate-angle-clockwise-between-two-points
def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

#This functions converts bearings from DEC to DMS.
#https://stackoverflow.com/questions/2579535/convert-dd-decimal-degrees-to-dms-degrees-minutes-seconds-in-python
def decdeg2dms(dd):
   is_positive = dd >= 0
   dd = abs(dd)
   minutes,seconds = divmod(dd*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if is_positive else -degrees
   return (degrees,minutes,seconds)

#defining the parameters.
#SCIMs Database
scims1 = (651414.544, 6431456.404)
scims2 = (651184.932, 6431496.121)

#Suvery observations
local1 = (651414.584, 6431456.367)
local2 = (651184.981, 6431496.1)

#computing the bearing - in decimal.
scimsBearingDec=angle_between(scims1, scims2)
localBearingDec=angle_between(local1, local2)

#compute the delta coordinates. This is a tuple subtraction.
#https://www.geeksforgeeks.org/python-how-to-get-subtraction-of-tuples/
delta1 = tuple(map(lambda i, j: i - j, local1, scims1))
delta2 = tuple(map(lambda i, j: i - j, local2, scims2))

#converts the bearings from decimal to DMS.
scimsBearingDMS=decdeg2dms(scimsBearingDec)
localBearingDMS=decdeg2dms(scimsBearingDec)

#This prints the bearing as decimal.
print("Bearing between SCIMs Points: " + str(scimsBearingDMS))
print("Bearing between Survey Points: " + str(localBearingDMS))

#This prints the delta between the SCIMs and Survey point.
print("Delta 1 = " + str(delta1))
print("Delta 2 = " + str(delta2))



#Things to iron out:

#Bearing computations are the same.
#how to user enter the parameters.
#import a csv with the parameters
#clean up bearing output.
#Distance between points.
