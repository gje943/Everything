import random
def euromillionsSimulator(main_numbers, lucky_stars):
   years = 0
   weeks = 0
   possible_main_nums = [i for i in range(1, 51)]
   possible_lucky_stars = [i for i in range(1, 13)]
   print("Starting euromillions simulation......")
   while True:
      weeks += 1
      x = random.sample(possible_main_nums, 5)
      y = random.sample(possible_lucky_stars, 2)
      if set(x).issubset(main_numbers) and \
         set(y).issubset(lucky_stars):
         if years > 0:
            print("Congratulations, you've won! It only took you", years, "years! while buying 4 tickets per week")
         else:
            print("Congratulations, you've won! It only took you", weeks, "weeks! That was fast!!")
         print("Restarting simulation.....")
         years = 0
         weeks = 0            
      if not weeks%208:
         years += 1
         if not years%1000:
            print(years, "years have passed...you still haven't won!!")

euromillionsSimulator([12,43,8,32,38], [4,11])