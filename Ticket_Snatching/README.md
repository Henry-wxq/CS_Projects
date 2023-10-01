# Ticket_Snatching

This repository is aimed at showing my method in snatching concert/exhibition tickets.

****
## Content
* [Aspiration](#Aspiration)
* [General_Procedure](#General_Procedure)
* [Different_Websites](#Different_Websites)
* [Verification](#Verification)

****
## Aspiration
During the summer vacation in 2023, after my cousin finished her university entrance exam, we went to one of the greatest places in Guangdong province to enjoy a hot spring. (I couldn't remember the location now, but i will post it later)

In the second night, we when to play the Chinese 8 ball billiards. But my younger cousin was really upset for unsuccessfully snatching a ticket for the comic exhibition she love the most. So the idea of writing a ticket snatching program to give to her as a present came into my mind.

****
## General_Procedure
1. Get User Info: Build a interactive program for user to type their information used to login in. **Make sure not to store the personal information, which means once the procedure end, the information should be removed.**
2. Use the appropriate program: Different website will have different login and ticket snatching process. We need to match the appropriate program with what the User input. 
3. Stop the Automatic Prohibition: Since we want our program to be fully automatic, we will use the automatic package in Python, which, without pretend, can be recognized by Google Chrome.
4. Auto Login: We will use the information obtained from step 1 help us to do the auto login. And go to the ticket snatching page immediately after auto login.
5. Check the Status: Since we will do the login several minutes before the tickets release, we need to check the snatching button frequently.
6. Snatching: Once the 'Snaching' button exists, we need to click it. Then the general procedure ends and the finally achieve the goal.

****
## Different_Websites
Since the program is initially designed for my younger cousin, we will start from some popular Chinese ticket snatching website then generalize it to the international. We will make some Android and ios apps as well.

****
## Verification
From the experience in daily life, we recognize 90%, there will be a verification action after clicking the login button. Therefore, in order to pass it, we will train our own model based on different websites to recoginze the code and pass the verification.

