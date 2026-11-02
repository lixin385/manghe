import streamlit as st

# 页面基础设置，适配手机
st.set_page_config(page_title="意象诗句盲盒", layout="centered")
st.title("🎨 意象诗句盲盒测试")

# ===================== 8组意象结果（i1~i8全部用上）=====================
box_result = [
    {
        "name": "寒江孤雪",
        "desc": "清冷孤寂，万籁无声的水墨意境",
        "img": "i1.jpg"
    },
    {
        "name": "明月清辉",
        "desc": "月色温柔，安静悠远",
        "img": "i2.jpg"
    },
    {
        "name": "大漠长河",
        "desc": "辽阔苍茫，大气磅礴",
        "img": "i3.jpg"
    },
    {
        "name": "春山雾霭",
        "desc": "草木朦胧，温润松弛",
        "img": "i4.jpg"
    },
    {
        "name": "深海星落",
        "desc": "沉静深邃，藏着无人知晓的浪漫",
        "img": "i5.jpg"
    },
    {
        "name": "云间长风",
        "desc": "自由舒展，无拘无束",
        "img": "i6.jpg"
    },
    {
        "name": "枫林晚渡",
        "desc": "热烈而温柔，暮色缓缓降临",
        "img": "i7.jpg"
    },
    {
        "name": "旷野晨光",
        "desc": "新生的力量，明朗干净",
        "img": "i8.jpg"
    }
]

# ===================== 选择题部分（你可以后续修改题目）=====================
# 使用session_state保存答题状态
if "score" not in st.session_state:
    st.session_state.score = 0
if "finish" not in st.session_state:
    st.session_state.finish = False

if not st.session_state.finish:
    st.subheader("回答下面的题目，抽取属于你的意象")
    q1 = st.radio("❶ 你更喜欢哪一类色调？", ["清冷蓝紫", "温润暖黄", "苍茫大地色", "朦胧青绿色"])
    q2 = st.radio("❷ 读到诗句，你更偏爱？", ["孤舟寒雪", "山间明月", "长河落日", "雾里春山"])
    q3 = st.radio("❸ 内心向往的状态？", ["安静独处", "自在漫游", "热烈奔赴", "温柔松弛"])

    if st.button("开启你的意象盲盒✨"):
        # 根据选择计算分数
        ans_list = [q1,q2,q3]
        score = 0
        for a in ans_list:
            score += len(a)
        # 将分数映射到 0~7，对应8个结果索引
        idx = score % 8
        st.session_state.score = idx
        st.session_state.finish = True
        st.rerun()
else:
    # 展示抽到的盲盒结果
    res = box_result[st.session_state.score]
    st.header("🎁 你的意象盲盒已开启！")
    st.subheader(res["name"])
    st.write(res["desc"])
    st.image(res["img"])

    # 重新游玩按钮，重置状态
    if st.button("🔄 重新玩一次"):
        st.session_state.finish = False
        st.rerun()