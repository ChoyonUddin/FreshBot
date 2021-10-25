import sys
from InformationVariables import BasementUserIds
def func():
    print(BasementUserIds.get('Fresh'))
func()

'''
async def roast(ctx,user):
    if ctx.author == bot.user:
        return
    else:
        newuser = bot.get_user(user)
        await ctx.send(newuser)
        
        await ctx.send(f"Fuck you {user.mention}")
    
'''