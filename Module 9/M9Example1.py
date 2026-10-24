#Iana Vasileva  CIS160 B65   M9Ex1    10/24/26
#Write a function that receives points and redemption code and computes rewards points. Display points, redemption code and rewards points.
#Display points, redemption code and rewards points.
reward_points=0

#Define function
def compute_rewards_points(points,redemp_code):
   if redemp_code=="X":
       reward_points=points*3
   elif redemp_code=="C":
       reward_points=points*2
   else:
       reward_points=points*1.5
   return reward_points

#Input
points=int(input("Enter the number of points:"))
redemp_code=str(input("Enter the redemption code:")).upper()

# Compute rewards points
reward_points = compute_rewards_points(points, redemp_code)

#Display result
print("Points:",points)
print("Redemption code:",redemp_code)
print("Reward points:",reward_points)
