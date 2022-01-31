The Bible Reading Challenge Bot
---

>Bot by: [Revival-Library.com](https://revival-library.com) | The Bible Reading Challenge was started by [Christ Church](https://biblereading.christkirk.com/) in Moscow Idaho.
[Read More](https://revival-library.com/bible-reading-challenge)...

---
Commands
---
**BRC Commands**

`!join` - Joing the Challenge! You will gain access to additional commands and start recieving XP
>`!checkin` - After completeing each daily reading, use this command to check-in. You'll get some XP and your daily reading streak will increase. If you forget to check-in your reading streak will be reset. The higher your reading streak, the more XP you will earn daily.

>`!stats` - Will display your total XP gained and current reading streak.

>`!leaderboard` - Displays a list of challengers who have the highest reading streak.

**Reading Plan Commands**

`!day` - Displays the daily reading plan with links to the blue letter bible app.
> This is a work in progress. Currently an admin has to post this in a dedicated channel manually each day. In the future there will be an automatic post option, and the abiblity to toggle auto post on/off.


---
Admin Commands
---
`Still need to make these available to admins only. Or role specific etc.`

`allUsers` - Displays a list of all users in the database.

#
**God Bless <3**
 
**- Revival-Library**

#

** (IGNORE THIS) Example Code Block **
```python
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")
```