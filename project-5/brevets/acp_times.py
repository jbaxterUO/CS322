"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

#Maps for open and close times, as well as a list of the keys in each to use
#For iterating through in order since you can't iterate through a dict in
#Order without sorting first
min = {
   0: 15,
   200: 15,
   400: 15, 
   600: 11.428,
   1000: 13.333,
}

max = {
   0: 34,
   200 : 32,
   400: 30, 
   600: 28,
   1000: 26,
}

#Fixed end times for brevets of the key length
set_end_tims = {
         200: 13.5,
         300: 20, 
         400: 27,
         600: 40,
         1000: 75
      }

#Known brevet distances
brev_distances = [0, 200, 400, 600, 1000]

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
   """
   hrs = 0
   mins = 0

   if control_dist_km > brevet_dist_km:
      control_dist_km = brevet_dist_km
   
   remaining = control_dist_km

   if remaining != 0:
      i = 1
      while remaining > brev_distances[i]:
         #The i - 1 is referencing the last point, essentially this is
         #Finding the distance since the last fixed control and using the given
         #Rate on that entire segment, like the segment between 200-400
         step_distance = brev_distances[i] - brev_distances[i - 1]
         time = step_distance / max[brev_distances[i - 1]]
         hrs += math.floor(time)
         mins += (time % 1) * 60
         i+= 1
      
      #After each segment that has a fixed length is done add the segment that
      #Might not align on a control point well, applies even when 0 segments have been
      #Added like in the case of values under 200
      step_distance = remaining - brev_distances[i - 1]
      time = step_distance / max[brev_distances[i - 1]]
      hrs += math.floor(time)
      mins += (time % 1) * 60

 
   return arrow.get(brevet_start_time).shift(hours=hrs, minutes=round(mins))


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
   """

   hrs = 0
   mins = 0

   if control_dist_km > brevet_dist_km:
      control_dist_km = brevet_dist_km

   remaining = control_dist_km
   #If control is at 0km
   if remaining == 0:
      hrs = 1
   #Special case where control is less than 60 km
   elif remaining <= 60:
      hrs = 1
      mins = (remaining / 20) * 60
   #Special case where control is the end of the brevet, has fixed end times
   elif control_dist_km == brevet_dist_km:
      hrs = set_end_tims[control_dist_km]
   else:
      i = 1
      while remaining > brev_distances[i]:
         #The i - 1 is referencing the last point, essentially this is
         #Finding the distance since the last fixed control and using the given
         #Rate on that entire segment, like the segment between 200-400
         step_distance = brev_distances[i] - brev_distances[i - 1]
         time = step_distance / min[brev_distances[i - 1]]
         hrs += math.floor(time)
         mins += (time % 1) * 60
         i+= 1

      
      #After each segment that has a fixed length is done add the segment that
      #Might not align on a control point well, applies even when 0 segments have been
      #Added like in the case of values under 200
      step_distance = remaining - brev_distances[i - 1]
      time = step_distance / min[brev_distances[i - 1]]
      hrs += math.floor(time)
      mins += (time % 1) * 60
      print(f"Time: {time} = step: {step_distance} / rate {min[brev_distances[i - 1]]}")
      
   return arrow.get(brevet_start_time).shift(hours=hrs, minutes= round(mins))
