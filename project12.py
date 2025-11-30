import streamlit as st

st.set_page_config(page_title='✨ Vương quốc mô hình ✨', page_icon=':sparkles:')

with st.sidebar:
    st.title('🏰 Vương quốc mô hình')
    st.header('👋 Chào mừng bạn đến Vương quốc mô hình!')
    st.image('mohinh.jpg')
    st.write('🧸 Chúng tôi chuyên bán các mô hình nhân vật hoạt hình chất lượng. '
             '📦 Luôn cập nhật và đa dạng sản phẩm. '
             '💯 Cam kết sự hài lòng của khách hàng với dịch vụ chuyên nghiệp. '
             '🌟 Hãy đến và khám phá thế giới mô hình tại Vương quốc mô hình!')
    st.write('🏠 Địa chỉ cửa hàng: Trái đất')
    st.write('📞 Điện thoại liên hệ: 09-0900-9000')

st.title('✨ Vương quốc mô hình ✨')
col1, col2, col3 = st.columns(3)

with col1:
    b1 = st.button('🐉 Dragon Ball')
with col2:
    b2 = st.button('🍥 Naruto')
with col3:
    b3 = st.button('🏴‍☠️ One Piece')

if b1:
    st.header('🐉 Danh sách mô hình Dragon Ball')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('goku.jpg', caption='⚡ Goku Ultra Instinct - Mã số: 001')
    with col5:
        st.image('vegeta.jpg', caption='🔥 Vegeta Super Saiyan - Mã số: 002')
    with col6:
        st.image('piccolo.jpg', caption='💚 Piccolo - Mã số: 003')

if b2:
    st.header('🍥 Danh sách mô hình Naruto')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('naruto.jpg', caption='🍜 Uzumaki Naruto - Mã số: 001')
    with col5:
        st.image('sasuke.jpg', caption='🌌 Uchiha Sasuke - Mã số: 002')
    with col6:
        st.image('kakashi.jpg', caption='📖 Hatake Kakashi - Mã số: 003')

if b3:
    st.header('🏴‍☠️ Danh sách mô hình One Piece')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('luffy.jpg', caption='👒 Monkey D. Luffy - Mã số: 001')
    with col5:
        st.image('zoro.jpg', caption='⚔️ Roronoa Zoro - Mã số: 002')
    with col6:
        st.image('sanji.jpg', caption='🍳 Vinsmoke Sanji - Mã số: 003')

st.header('🛒 Đặt hàng')
with st.form('Đơn đặt hàng'):
    topics = ('🐉 Dragon Ball', '🍥 Naruto', '🏴‍☠️ One Piece')
    option_topic = st.selectbox('🎯 Chủ đề mô hình', topics)

    codes = ('001', '002', '003')
    option_code = st.selectbox('🔢 Mã số mô hình', codes)

    nums = st.slider('📦 Số lượng bạn muốn đặt:', 0, 10, 0)

    name = st.text_input('👤 Họ và tên')
    phone = st.text_input('📞 Số điện thoại liên hệ')
    address = st.text_input('🏠 Địa chỉ giao hàng')

    bill = {
        'Loại mô hình:': option_topic,
        'Mã số:': option_code,
        'Số lượng:': nums,
        'Họ tên khách hàng:': name,
        'Số điện thoại liên hệ:': phone,
        'Địa chỉ giao hàng:': address
    }

    submitted = st.form_submit_button("✅ Xác nhận")
    if submitted:
        st.header('📋 Bạn đã chọn:')
        for x, y in bill.items():
            st.write(x, y)

print_bill = st.checkbox('🖨️ In hoá đơn')
if print_bill:
    ans = ''
    for x in bill:
        ans += str(x) + ' ' + str(bill[x]) + '\n'
    st.download_button('💾 In hoá đơn', ans, file_name='hoadon.txt')