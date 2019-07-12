"""
以下为设置界面元素信息
"""
# 搜索按钮
from selenium.webdriver.common.by import By

search_btn = By.ID, 'com.android.settings:id/search'
# 输入框
search_input = By.ID, 'android:id/search_src_text'
# 返回按钮
back_btn = By.CLASS_NAME, 'android.widget.ImageButton'
