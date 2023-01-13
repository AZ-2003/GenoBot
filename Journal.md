# GenoBot Journal Entry  
 
## Entry 1  
**Entry Date: 20th December 2022**  
First steps towards creating Geno have been made as Geno now exists on the server and is capable of responding to the basic calls. It was deemed as challenging as contraray to the tutorial videos which used an external IDE (ripl.it), I made it clear that I wamted to use VS Code such that I can be capable of having a more *authentic* path (and therefore a path full of challenges and inconveniences and lots of figuring out )  
A prominent challenge was dealing with the token; doing it in VS code required the usage of the ` dotenv ` package such that it can read the environment variables and to obtain the token for the bot to run.  
An interesting observation is that the names of the functions cannot be changed which makes me wonder if they are part of the Discord API (therefore they must have a consistent nomenclature)  
  
Key aspects to focus for next time:<ul>  
<li>Refer the Documentation such that you can better understand the functions and keywords involved and therefore help better plan future improvments. </li>
<li>Refer to the Google Calender API (if any) to help connect the Bot to Google Calender such that we can use the Bot to plan events.</li>  
<li>Create a Documentation Style and remain consistent with it. </li></ul>    

***

## Entry 2  
**Entry Date: 28th December 2022**   
#### *This is an updated style of the Journal Entry*
Progress made:<ul>
    <li> Created a subsiduiary file - `Geno0.py` - to handle variables and helper functions</li>
    <li> Geno is now capable of entering and exiting Voice Channels</li>
    <li> Created a new instance that can accomodate both events and commands </li>
    <li> Created a GitHub Repo for the project </li></ul>
Key Takeaways:<ul>  
    <li> Discord Commands require the usage of Context - ` ctx ` for short -to operate  
    (Definitely need to get a better understanding of Context)</li>
    <li> `await Bot.process_commands(message)` is the line that was used to avoid a collision caused between event calls and commands - that and establishing a unified instance: now called `Bot`</li>
    <li> There are slight differences betwwen OOP in Python and OOP in Java and C++ </li>
    <li> Still need a better understanding of intents </li></ul>
Moving Forward: <ul>
    <li> Ensuring that Geno only responds to *Me* (Probably should be the first thing to do after finishing this entry)</li>
    <li> Testing the Spotify API to allow Geno to play either of the options (whichever is more promising):<ul>
        <li> Playing Prominent playlists of my choosing - ex: RAM, Take Tsubo (maybe a personalized playlist)</li>
        <li> Playing from the Liked Songs section </li>
        <li> Playing from songs I specify - like Pancake (not the best option) </li></ul>
    <li> Let Geno tell the time  on any designated city of any country</li></ul>  
  
***
## Entry3
**Entry Date: 13th January 2023**
Progress made:<ul>
    <li> Tested the Google Calender API (test file to be posted) and set up a Google working environment</li>
    <li> Lots of "behind the scenes" work involving the communication between the Discord & Google Calender API</li></ul>
Key Takeaways:<ul>
    <li> Heavy Security for using the Google Calender API which might be a possible challenge to go through in order to allow Geno to operate on the Calender( it is doable) </li> </ul>
Moving Forward:<ul>
    <li> Finish setting up and testing the Google Calender API and a helper function file for Geno to use </li></ul>  
***



    


