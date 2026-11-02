import streamlit as st

# 页面设置，适配手机
st.set_page_config(page_title="意象盲盒答题", layout="centered")
st.title("🎨 意象诗句盲盒")

# ========== 8组意象结果（i1 ~ i8） ==========
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

# ========== 答题状态初始化 ==========
if "result_index" not in st.session_state:
    st.session_state.result_index = 0
if "finished" not in st.session_state:
    st.session_state.finished = False

if not st.session_state.finished:
    st.subheader("回答题目，抽取属于你的专属意象")

    # 三道选择题，保存选项列表，用来获取选中序号
    opt1 = ["清冷蓝紫", "温润暖黄", "苍茫大地色", "朦胧青绿色"]
    opt2 = ["孤舟寒雪", "山间明月", "长河落日", "雾里春山"]
    opt3 = ["安静独处", "自在漫游", "热烈奔赴", "温柔松弛"]

    q1 = st.radio("❶ 你更偏爱哪一类色调？", opt1)
    q2 = st.radio("❷ 读到诗句，你更偏爱哪一种意境？", opt2)
    q3 = st.radio("❸ 内心向往的生活状态？", opt3)

    if st.button("✨开启意象盲盒"):
        # 获取每一题选中的索引（0开始）
        idx1 = opt1.index(q1)
        idx2 = opt2.index(q2)
        idx3 = opt3.index(q3)
        # 叠加计算，保证组合更多，可以覆盖0~7全部8个索引
        total = idx1 * 16 + idx2 * 4 + idx3
        st.session_state.result_index = total % 8
        st.session_state.finished = True
        st.rerun()

else:
    selected = box_result[st.session_state.result_index]
    st.header("🎁 你的意象盲盒已开启！")
    st.subheader(selected["name"])
    st.write(selected["desc"])
    st.image(selected["img"])

    if st.button("🔄 重新玩一次"):
        st.session_state.finished = False
        st.rerun()