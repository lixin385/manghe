# app.py
import streamlit as st

# 设置手机友好布局
st.set_page_config(page_title="意象盲盒答题", layout="centered")

# ----------------题库设置----------------
questions = [
    {
        "cate": "颜色",
        "title": "你偏爱哪一种色调？",
        "options": ["清冷月白", "沉郁赭红", "远山青黛"]
    },
    {
        "cate": "诗句",
        "title": "哪一句诗句最打动你？",
        "options": ["孤舟蓑笠翁，独钓寒江雪", "春风又绿江南岸", "大漠孤烟直，长河落日圆"]
    },
    {
        "cate": "意象",
        "title": "更喜欢哪一种古典意象？",
        "options": ["梧桐", "明月", "落花"]
    }
]

# 盲盒结果（这里img填入你上传到图床后的图片在线地址）
# 盲盒结果（直接读取仓库里的本地图片）
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
    }
]

# 页面状态记忆
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "sum_score" not in st.session_state:
    st.session_state.sum_score = 0

step = st.session_state.current_q

if step < len(questions):
    q = questions[step]
    st.subheader(f"第{step+1}题｜{q['cate']}")
    st.write(q["title"])
    user_choice = st.radio("请选择：", q["options"])
    if st.button("确认，下一题"):
        # 根据选项累加分数
        st.session_state.sum_score += q["options"].index(user_choice)
        st.session_state.current_q += 1
        st.rerun()
else:
    st.header("🎁 你的意象盲盒已开启！")
    score = st.session_state.sum_score
    # 根据总分匹配盲盒
    if score <= 2:
        res = box_result[0]
    elif score <=5:
        res = box_result[1]
    else:
        res = box_result[2]
    st.subheader(res["name"])
    st.write(res["desc"])
    st.image(res["img"])
    if st.button("🔄 重新玩一次"):
        st.session_state.current_q = 0
        st.session_state.sum_score = 0
        st.rerun()
