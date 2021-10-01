import discord
import asyncio, random, os, 

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('-디지봇 도움말 준비 중')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "?롤덤이 안녕":
        await message.channel.send("안녕")

    if message.content == "?롤덤이 ㅎㅇ":
        await message.channel.send("안녕")

    if message.content == "?롤덤이 잘가":
        await message.channel.send("잘 가")
  
    if message.content == "?롤덤이 잘 가":
        await message.channel.send("잘 가")



    if message.content == "찌뚜유튜브":
        embed = discord.Embed(title="찌뚜 유튜브 채널", description="https://www.youtube.com/c/찌뚜유튜븝", color=0x00ff00)
        embed.set_footer(text="구독과 좋아요 부탁드려요")
        await message.channel.send(embed=embed)

    if message.content == "-디지봇 도움말":
        embed = discord.Embed(title="디지봇 사용방법", description=" :bulb: Tip : 밑에 있는 도움말을 보고 이용해주세요 :D", color=0x17164D)
        embed.add_field(name=":newspaper: 봇 패치노트", value=" ``?롤덤노트`` ", inline=False)
        embed.add_field(name=":page_with_curl: 일반 명령어", value=" ``?롤덤이 일반`` ", inline=False)
        embed.add_field(name=":page_with_curl: 추첨 명령어", value=" ``?롤덤이 추첨 안내`` ", inline=False)
        embed.add_field(name=":earth_asia: 문의 명령어", value=" ``?롤덤이 문의`` ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)

    if message.content == "?롤덤이 추첨 안내":
        embed = discord.Embed(title="롤랜덤이 사용방법", description=" :bulb: Tip : 밑에 있는 도움말을 보고 이용해주세요 :D", color=0x17164D)
        embed.add_field(name=":newspaper: 전체 추첨 명령어", value=" ``?롤덤이 챔피언 전체 추천`` ", inline=False)
        embed.add_field(name=":newspaper: 포지션 별 추첨 명령어", value=" ``?롤덤이 챔피언 암살자 추천`` , ``?롤덤이 챔피언 메이지 추천`` , ``?롤덤이 챔피언 전사 추천`` , ``?롤덤이 챔피언 서포터 추천`` ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)

    if message.content == "?롤덤이 암살자 목록":
        embed = discord.Embed(title="암살자 목록", description="출처 : 리그 오브 레전드 나무위키", color=0x9c0d06)
        embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA5MjNfMTQ5/MDAxNjMyMzkzODMyMzg1.kejiRlROo9cwl3qFrdIvACBnYYHSHw72kx6CTWFHcFIg.cmO5nkJ2cawK_T2yngs9CXnLCMJHsoMK14jpN92hjUYg.PNG.jjiddoo3003/%EC%95%94%EC%82%B4%EC%9E%90.png?type=w966")
        await message.channel.send(embed=embed)


    if message.content == "?롤덤이":
        embed = discord.Embed(title="롤랜덤이 사용방법", description=" :bulb: Tip : 밑에 있는 도움말을 보고 이용해주세요 :D", color=0x17164D)
        embed.add_field(name="?롤덤이 도움말을 사용 해주세요", value=" ``또는 ?롤덤이 문의`` ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)

    if message.content == "?롤덤이 추첨":
        embed = discord.Embed(title="롤랜덤이 추첨 명령어", description=" :bulb: Tip : 밑에 있는 도움말을 보고 이용해주세요 :D", color=0x17164D)
        embed.add_field(name="?롤덤이 도움말을 사용 해주세요", value=" ``또는 ?롤덤이 문의`` ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)
        

    if message.content == "?롤덤노트":
        embed = discord.Embed(title=":newspaper: 롤덤 노트 0.1 ver", description=" **```수정일 : 2021_09_16 롤덤이 봇 바뀐 점을 알려드립니다.```**", color=0x17164D)
        embed.add_field(name=":repeat: 바뀐 점", value=" :tools: 개발자 이야기 : **``` 롤 랜덤 봇 롤덤이가 2021_09_16 에 시작 되었습니다. 이 봇은 단순 제작자가 파이썬 공부 하기 위해서 호기심을 갖다가 만들어진 것 입니다. 관심있는 것 또한 리그오브레전드 이기에 만들게 되었습니다.```** ", inline=False)
        embed.add_field(name=":birthday: 롤덤이 탄생....!!", value=" **```롤덤이 탄생일은 2021_09_16```** ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)


    if message.content == "- 일반":
        embed = discord.Embed(title="롤랜덤이 일반 명령어", description=" :bulb: Tip : 밑에 있는 도움말을 보고 이용해주세요 :D", color=0x17164D)
        embed.add_field(name=":page_with_curl: 일반 명령어", value=" ``?롤덤이 포지션 추천 `` ", inline=False)
        embed.add_field(name=":repeat_one: 추천 명령어", value=" ``?롤덤이 포지션 추천 , ?롤덤이 라인 추천 `` ", inline=False)
        embed.add_field(name=":page_with_curl: 일반 명령어", value=" ``?롤덤이 포지션 추천 `` ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)





access_token = os.environ['BOT_TOKEN']
client.run(access_token)

