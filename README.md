# SpaceInvaders-from-TokyoEdTech-by-PedroElizalde
Hi! This is a little summary of what this whole thing is about (I'm not very good at speaking English, so sorry if there is something grammatically wrong ; ])

1)  The original idea and bases from this scripts where taken from the YouTube channel: 'TokyoEdTech' (Thanks for the tutorials :))
    Please check out his channel it has amazing tutorials!
                                      https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg

***************************************************************************************************************************************************
2) I'm having problems with making the enemy to shoot me back. I made the function call 'fire_missile', I assign the key 'm' to call it every time I press it and it works fine. Bassically, this is what the function does: First, it search for a random enemy, looks after the 'x' and 'y' coordinates. Then, if the 'y' coordinate is lower than 300: It plays a sound effect, sets the position of the missile on the same place than the coordinates of the enemy (To simulate that it shoots) and finnaly shows the missile turtle (because it was hidden). Otherwise, if the 'y' coordinate is higher than 300, it repeat the function until an enemy shoots.
        
   What I want to do, is make the enemy to shoot me back every 5 seconds. But, every time I call the function with a time delay it doesn't work.
   I tried by importing 'threading' and do:
   
          threading.Timer(5.0, fire_missile).start()
	  
   However still doesn't work. I even made a function that count from 0 to 5 in five seconds and then call 'fire_missile' without succeeding.
   
   Hope you have any idea of what I should do!
   
   ***************************************************************************************************************************************************
   P.D: Check the YouTube channel I mentioned before!
