#戳一戳事件仅在ANDROID_PHONE,ANDROID_PAD,IPAD中可用
from graia.ariadne.app import Ariadne
from graia.ariadne.event.mirai import NudgeEvent
from graia.ariadne.message.chain import MessageChain, Plain
from graia.ariadne.message.element import At
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[NudgeEvent]))
async def getup(app: Ariadne, event: NudgeEvent):
   if event.target == 2946761346:
    if event.context_type == "group":
        await app.send_group_message(
            event.group_id,
           MessageChain(MessageChain([At(event.supplicant), Plain(" 再戳老娘就把你手指头掰断！！！！！！！！")]))
        )
    elif event.context_type == "friend":
        await app.send_friend_message(
            event.friend_id,
            MessageChain("再戳打死你！")
        )
